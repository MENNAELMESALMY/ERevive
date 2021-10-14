import numpy as np
import cv2
from math import sqrt

#remove lines function
def FloodFromCorners(im_th,debug=False):
    hImg, wImg = im_th.shape[:2]
    mask = np.zeros((hImg+2, wImg+2), np.uint8)
    im_floodfill = 255 - im_th
    ##################Flood fill corners#####
    cv2.floodFill(im_floodfill, mask, (0,0), 255)
    cv2.floodFill(im_floodfill, mask, (wImg-1,0), 255)
    cv2.floodFill(im_floodfill, mask, (0,hImg-1), 255)
    cv2.floodFill(im_floodfill, mask, (wImg-1,hImg-1), 255)
    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    if(debug):
        cv2.imwrite("Inverted_Floodfilled_Image.png", im_floodfill_inv)
        cv2.imwrite("Floodfilled_Image.png", im_floodfill)
    return im_floodfill_inv


######################cv contours#########
def getClosedShapes(im_filled,debug=False):
    hImg, wImg = im_filled.shape
    contours_cv, hierarchy = cv2.findContours(im_filled, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
    #[Next, Previous, First_Child, Parent]
    cnt_hull = [cv2.convexHull(cnt,False) for cnt in contours_cv]
    im_empty = np.ones((hImg, wImg,3), np.uint8) * 255
    im_empty2 = np.ones((hImg, wImg,3), np.uint8) * 255
    failed1 = np.ones((hImg, wImg,3), np.uint8) * 255
    failed2 = np.ones((hImg, wImg,3), np.uint8) * 255
    failed3 = np.ones((hImg, wImg,3), np.uint8) * 255
    filtered_contoures = []
    for cnt,heir in zip(cnt_hull,hierarchy):
        if heir[3] != -1:
            continue

        #contours that has at least two children
        x,y,w,h = cv2.boundingRect(cnt)
        acceptedArea = h<=1000 and w <=1000 and h>=7 and w>20
        child1Idx = heir[2]
        hasChildren = child1Idx != -1 and  hierarchy[child1Idx][0] != -1
        if(hasChildren and acceptedArea):
            child2Idx = hierarchy[child1Idx][0]
        #this two children are close (letters)
        #check area
        
        if(hasChildren and acceptedArea):
            #print((w*h)/area)
            x1,y1,w1,h1 = cv2.boundingRect(contours_cv[child1Idx])
            x2,y2,w2,h2 = cv2.boundingRect(contours_cv[child2Idx])
            print("dist:",sqrt((x1-x2)**2+((y1-y2)**2)))
            if(sqrt((x1-x2)**2+((y1-y2)**2)) <= 400):
                cv2.drawContours(im_empty, [cnt], -1, (0,0,0), 1)
                filtered_contoures.append(cnt)
                continue
        else:
            #print('cond1',hasChildren,acceptedArea,h,w)
            cv2.drawContours(failed1, [cnt], -1, (0,0,0), 1) 

        
        if(child1Idx != -1 and  hierarchy[child1Idx][0] == -1):
            x1,y1,w1,h1 = cv2.boundingRect(contours_cv[child1Idx])
            
            if(w1/w >= 0.3):
                cv2.drawContours(im_empty, [cnt], -1, (0,0,0), 1)
                filtered_contoures.append(cnt)
                continue
        else:
            x1,y1,w1,h1 = cv2.boundingRect(contours_cv[child1Idx])
           # print('cond2',w1/w >= 0.3)
            cv2.drawContours(failed2, [cnt], -1, (0,0,0), 1) 

        if(not hasChildren and acceptedArea and w/h >= 1.2 and w/h<=8):
            print(w/h,w,h)
            filtered_contoures.append(cnt)
            cv2.drawContours(im_empty, [cnt], -1, (0,0,0), 1)
            continue
        else:
            print('cond3',hasChildren,acceptedArea,w/h >= 1.8 , w/h<=8,w,h) 
            cv2.drawContours(failed3, [cnt], -1, (0,0,0), 1) 

    cv2.drawContours(im_empty2, cnt_hull, -1, (0,0,0), 1)
    if(debug):
        cv2.imwrite("contoured.png", im_empty[:,:,0])
        cv2.imwrite("contoured_not_filtered.png", im_empty2)
        cv2.imwrite("failed1.png", failed1)
        cv2.imwrite("failed2.png", failed2)
        cv2.imwrite("failed3.png", failed3)


    return im_empty[:,:,0] , filtered_contoures


#handling opened contours

# find center of gravity from the moments:
def scale_contours(contours, scale):
    """Shrinks or grows an array of contours by the given factor (float). 
    Returns the resized array of contours"""
    for idx,contour in enumerate(contours):
        moments = cv2.moments(contour)
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
            and abs(Xmid-cXmid)<= abs(Xmax-Xmin)/8 
            and abs(Ymid-cYmid)<=10
            ):
            return True
    return False


def getOpenedContours(img,closed_contours=[],debug = False):
    closed_contours = scale_contours(closed_contours,1.15)
    cv2.drawContours(img,closed_contours,-1, 255,-1 )
    contours, hierarchy = cv2.findContours(255 - img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_parent = np.ones(img.shape, np.uint8) * 255
    parentContours =[ cnt for cnt in contours if not isOverlapped(cnt,contours)]

    cv2.drawContours(img_parent,parentContours,-1, 0, -1 )
    img_parent = 255 - img_parent 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    dilated = cv2.dilate(img_parent,kernel,iterations=3)
    #dilated = cv2.morphologyEx(img_parent, cv2.MORPH_CLOSE, kernel,iterations=4)
    edges = cv2.Canny(dilated, 0, 200, apertureSize=3)
    #get child contours and draw hull
    img_inner_contour = np.ones(img.shape, np.uint8) * 255
    contours,_ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cnt for cnt in contours if isOverlapped(cnt,contours) ]
    print(len(contours))
    contours = [cnt for cnt in contours if not isOverlapped_middle(cnt,contours) ]
    print(len(contours))
    cv2.drawContours(img_inner_contour,contours,-1, 0, 1 )
    eroded = cv2.erode(img_inner_contour,kernel,iterations=1)
    flooded = FloodFromCorners(eroded)
    flooded = cv2.dilate(flooded,kernel,iterations=3)
    contours,_ = cv2.findContours(flooded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    opened_contours = np.ones(img.shape, np.uint8) * 255
    contours = scale_contours(contours,1.1)
    #contours = [cnt for cnt in contours if not isOverlapped_middle(cnt,contours) ]

    #contours = [cv2.convexHull(cnt,False) for cnt in contours]

    print(len(contours))
    cv2.drawContours(opened_contours,contours,-1, 0, 1 )
    if(debug):
        cv2.imwrite("contoured_img.png",img)
        cv2.imwrite("img_parent.png",img_parent)
        cv2.imwrite("dilated.png",dilated)
        cv2.imwrite("edges2.png",edges)
        cv2.imwrite("img_inner_contour.png",img_inner_contour)
        cv2.imwrite("eroded.png",eroded)
        cv2.imwrite("filled.png",flooded)
        cv2.imwrite("opened_contours.png",opened_contours)
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
        #print(dashedFound)
        if dashedFound > 5:
            print(dashedFound,"found dashed")
            cv2.drawContours(im_dashes,[cnt],-1, 0, 1 )
    cv2.imwrite("im_scaled_down.png",im_scaled_down)
    cv2.imwrite("im_dashes.png",im_dashes)
