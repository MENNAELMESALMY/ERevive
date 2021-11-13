import numpy as np
import cv2
from math import sqrt
from scipy import stats

#remove lines function
def FloodFromCorners(im_th,debug=False):
    hImg, wImg = im_th.shape[:2]
    mask = np.zeros((hImg+2, wImg+2), np.uint8)
    im_floodfill = 255 - im_th
    ##################Flood fill corners#####
    cv2.floodFill(im_floodfill, mask, (3,3), 255)
    cv2.floodFill(im_floodfill, mask, (wImg-3,3), 255)
    cv2.floodFill(im_floodfill, mask, (3,hImg-3), 255)
    cv2.floodFill(im_floodfill, mask, (wImg-3,hImg-3), 255)
    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    if(debug):
        cv2.imwrite("Inverted_Floodfilled_Image.png", im_floodfill_inv)
        #cv2.imwrite("Floodfilled_Image.png", im_floodfill)
    return im_floodfill_inv

def removeOutliers(ContourList,Area,hImg,wImg,contours_orig):
    #remove outliers in list
    #by Area of contours list sent
    #or by aspect ratio
    if(len(ContourList)==0):
        #print('no contours')
        return []

    if Area:
        testList = [cv2.contourArea(c) for c in ContourList]
        testH = [ cv2.boundingRect(c)[3] for c in ContourList]
        testW = [cv2.boundingRect(c)[2] for c in ContourList]
        zH = np.abs(stats.zscore(testH))
        zW = np.abs(stats.zscore(testW))

    testList = []
    for c in  ContourList:
        x,y,w,h = cv2.boundingRect(c)
        testList.append(w/h)

    z = np.abs(stats.zscore(testList))
    filtered_hulls =[]
    filtered_contours =[]

    for i,c in  enumerate(ContourList):
        x,y,w,h = cv2.boundingRect(c)
        
        accepedArea = h <= hImg/2.5 and w <= wImg/2.5 and h>10 and w>=20 #and h*w > normalArea
        if not accepedArea:
            continue
        if(z[i]<=3):
          #  #print("width",w)
            if((Area and zH[i] <= 4 and zW[i] <= 4)or (not Area)):
                filtered_hulls.append(c)
                filtered_contours.append(contours_orig[i])
    return filtered_hulls,filtered_contours
    
    


######################cv contours#########
def getClosedShapes(im_filled,debug=False):
    hImg, wImg = im_filled.shape
    contours_cv, hierarchy = cv2.findContours(im_filled, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
    #[Next, Previous, First_Child, Parent]
    cnt_hull = [cv2.convexHull(cnt,False) for cnt in contours_cv]

    ##print('0:',len(cnt_hull))
    cnt_hull = [cnt for cnt,heir in zip(cnt_hull,hierarchy) if heir[3] == -1]
    cnt_filtered = [cnt for cnt,heir in zip(contours_cv,hierarchy) if heir[3] == -1]


    im_empty2 = np.ones((hImg, wImg), np.uint8) * 255
    cv2.drawContours(im_empty2, contours_cv, -1,0, 1)

    cnt_hull,cnt_filtered = removeOutliers(cnt_hull,True,hImg,wImg,cnt_filtered) #outliers by area
    cnt_hull,cnt_filtered = removeOutliers(cnt_hull,False,hImg,wImg,cnt_filtered) #outliers by aspect ratio


    im_empty = np.ones((hImg, wImg), np.uint8) * 255
    cv2.drawContours(im_empty, cnt_hull, -1,0, 1)

    im_empty3 = np.ones((hImg, wImg), np.uint8) * 255
    cv2.drawContours(im_empty3, cnt_filtered, -1,0, 1)

    if(debug):
        cv2.imwrite("hulled.png", im_empty)
        cv2.imwrite("contoured.png", im_empty3)
        cv2.imwrite("notFiltered.png", im_empty2)

    return im_empty , cnt_filtered


#handling opened contours

# find center of gravity from the moments:
def scale_contours(contours, scale):
    """Shrinks or grows an array of contours by the given factor (float). 
    Returns the resized array of contours"""
    if not len(contours):
        return []
        
    for idx,contour in enumerate(contours):
        moments = cv2.moments(contour)
        moments["m00"] = max(1,moments["m00"])
        midX = int(round(moments["m10"] / moments["m00"]))
        midY = int(round(moments["m01"] / moments["m00"]))
        mid = np.array([midX, midY])
        contours[idx] = contour - mid
        contours[idx] = (contours[idx] * scale).astype(np.int32)
        contours[idx] = contours[idx] + mid
    return contours

def isOverlapped(c,imgContours):
    cXmin,cYmin,cXmax,cYmax = cv2.boundingRect(c)
    cArea = cXmax * cYmax
    cXmax += cXmin
    cYmax += cYmin
    for imgContour in imgContours:
        Xmin,Ymin,Xmax,Ymax = cv2.boundingRect(imgContour)
        Xmax += Xmin
        Ymax += Ymin
        if(cXmin > Xmin and cXmax < Xmax and cYmin >= Ymin and cYmax <= Ymax):
            return True
    return False

def isOverlapped_middle(c,imgContours):
    cXmin,cYmin,cXmax,cYmax = cv2.boundingRect(c)
    cXmax += cXmin
    cYmax += cYmin
    cXmid = (cXmin+cXmax)/2
    cYmid = (cYmin+cYmax)/2
    for imgContour in imgContours:
        Xmin,Ymin,Xmax,Ymax = cv2.boundingRect(imgContour)
        Xmax += Xmin
        Ymax += Ymin
        Xmid = (Xmin+Xmax)/2
        Ymid = (Ymin+Ymax)/2
        #overlapped and in middle of a contour
        if(cXmin > Xmin and cXmax < Xmax and cYmin >= Ymin and cYmax <= Ymax
            and abs(Xmid-cXmid) <= abs(Xmax-Xmin)/8
            #and ((Xmax-cXmid) >= 10 or (cXmid-Xmin) >= 10)
            and abs(Ymid-cYmid) <= 10
            ):
            ##print("hi",abs(cXmid-Xmax), abs(cXmid-Xmin) )
            return True
    return False


def getOpenedContours(img,closed_contours=[],debug = False):
    #remove closed contours from image by drawing on it with white colour
    closed_contours = scale_contours(closed_contours[:],1.2)
    cv2.drawContours(img,closed_contours,-1, 255,-1 )


    #remove word by removing contours inside the middle of other contours
    contours, _ = cv2.findContours(255 - img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img_all = np.ones(img.shape, np.uint8) * 255
    cv2.drawContours(img_all,contours,-1, 0,1 )

    img_parent = np.ones(img.shape, np.uint8) * 255
    parentContours =[ cnt for cnt in contours if not isOverlapped_middle(cnt,contours)]
    cv2.drawContours(img_parent,parentContours,-1, 0, -1 )


    img_parent = 255 - img_parent 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,4))
    dilated = cv2.dilate(img_parent,kernel,iterations=2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(4,1))
    dilated = cv2.dilate(dilated,kernel,iterations=2)


    #get child contours and draw hull
    img_inner_contour = np.ones(img.shape, np.uint8) * 255
    contours,heirarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(img_inner_contour,contours,-1, 0, 1 )
    #contours = [cnt for cnt in contours if isOverlapped(cnt,contours) ]
    #contours = [cnt for cnt in contours if not isOverlapped_middle(cnt,contours) ]
    contours = [cnt for cnt,h in zip(contours,heirarchy[0]) if h[3] != -1]

    cv2.drawContours(img_inner_contour,contours,-1, 0, 1 )


    eroded = cv2.erode(img_inner_contour,kernel,iterations=1)
    flooded = FloodFromCorners(eroded)
    flooded = cv2.dilate(flooded,kernel,iterations=3)
    contours,_ = cv2.findContours(flooded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    opened_contours = np.ones(img.shape, np.uint8) * 255
    contours = scale_contours(contours,1.1)

    cv2.drawContours(opened_contours,contours,-1, 0, 1 )
    if(debug):
        cv2.imwrite("openedContoursDebug/1contoured_img.png",img_all)
        cv2.imwrite("openedContoursDebug/2img_parent.png",img_parent)
        cv2.imwrite("openedContoursDebug/3dilated.png",dilated)
        cv2.imwrite("openedContoursDebug/4img_inner_contour.png",img_inner_contour)
        cv2.imwrite("openedContoursDebug/5eroded.png",eroded)
        cv2.imwrite("openedContoursDebug/6filled.png",flooded)
        cv2.imwrite("openedContoursDebug/7opened_contours.png",opened_contours)
    return opened_contours,contours

def getDerived(img,contours):
    contours = [c for c in contours if not isOverlapped(c,contours)]
    scaled_up_contours = scale_contours(contours.copy(),1.6)
    scaled_down_contours = scale_contours(contours.copy(),0.85)
    im_dashes = np.ones(img.shape, np.uint8) * 255
    im_scaled_down = np.zeros(img.shape, np.uint8)
    cv2.drawContours(im_scaled_down,scaled_down_contours,-1, 255, -1 )
    img = cv2.bitwise_or(img , im_scaled_down)
    contours, heirarchy= cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    small_contours = []
    for cnt,heir in zip(contours,heirarchy[0]):
        x,y,w,h = cv2.boundingRect(cnt)
        if w<=35 and h<=20 and h>4 and w>4:
            small_contours.append(cnt)

    cv2.drawContours(im_dashes,small_contours,-1, 0, -1 )
            
    for cnt in scaled_up_contours:
        dashedFound = sum([1 for c in small_contours if isOverlapped(c,[cnt])])
        ##print(dashedFound)
        if dashedFound > 5:
            #print(dashedFound,"found dashed")
            cv2.drawContours(im_dashes,[cnt],-1, 0, 1 )
    cv2.imwrite("im_scaled_down.png",im_scaled_down)
    cv2.imwrite("im_dashes.png",im_dashes)
