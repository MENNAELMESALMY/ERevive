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
    im_empty = np.ones((hImg, wImg,3), np.uint8) * 255
    i=0
    filtered_contoures = []
    for cnt in contours_cv:
        if hierarchy[i][3] != -1:
            i+=1
            continue

        #contours that has at least two children
        x,y,w,h = cv2.boundingRect(cnt)
        acceptedArea = h<=150 and w <=300 and h>=7 and w>20
        child1Idx = hierarchy[i][2]
        hasChildren = child1Idx != -1 and  hierarchy[child1Idx][0] != -1
        if(hasChildren and acceptedArea):
            child2Idx = hierarchy[child1Idx][0]
        #this two children are close (letters)
        #check area
        if(hasChildren and acceptedArea):
            #print((w*h)/area)
            x1,y1,w1,h1 = cv2.boundingRect(contours_cv[child1Idx])
            x2,y2,w2,h2 = cv2.boundingRect(contours_cv[child2Idx])
            if(sqrt((x1-x2)**2+((y1-y2)**2)) <= 200):
                cv2.drawContours(im_empty, contours_cv, i, (0,0,0), 1)
                filtered_contoures.append(cnt)
                i+=1
                continue
                
        if(child1Idx != -1 and  hierarchy[child1Idx][0] == -1):
            x1,y1,w1,h1 = cv2.boundingRect(contours_cv[child1Idx])
            if(w1/w >= 0.3):
                cv2.drawContours(im_empty, contours_cv, i, (0,0,0), 1)
                filtered_contoures.append(cnt)
                i+=1
                continue
                
        if(not hasChildren and acceptedArea and w/h >= 1.8 and w/h<=8):
            print(w/h,w,h)
            filtered_contoures.append(cnt)
            cv2.drawContours(im_empty, contours_cv, i, (0,0,0), 1)
            i+=1
            continue
            

        i+=1
    if(debug):
        cv2.imwrite("contoured.png", im_empty[:,:,0])

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
def getOpenedContours(img,closed_contours=[],debug = False):
    closed_contours = scale_contours(closed_contours,1.2)
    cv2.drawContours(img,closed_contours,-1, 255,-1 )
    contours, hierarchy = cv2.findContours(255 - img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_parent = np.ones(img.shape, np.uint8) * 255
    parentContours =[]
    for i,cnt in enumerate(contours):
        x,y,w,h = cv2.boundingRect(cnt)
        if not isOverlapped(cnt,contours) and hierarchy[0,i,3]==-1 and h>10 and w>15 and w/h>1.5 and w/h<4:
            parentContours.append(cnt)

    cv2.drawContours(img_parent,parentContours,-1, 0, -1 )
    img_parent = 255 - img_parent 
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    dilated = cv2.dilate(img_parent,kernel,iterations=3)
    edges = cv2.Canny(dilated, 0, 84, apertureSize=3)
    #get child contours and draw hull
    img_inner_contour = np.ones(img.shape, np.uint8) * 255
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = [cnt for i,cnt in enumerate(contours) if isOverlapped(cnt,contours) ]
    cv2.drawContours(img_inner_contour,contours,-1, 0, 1 )
    eroded = cv2.erode(img_inner_contour,kernel,iterations=3)
    contours, hierarchy = cv2.findContours(255-eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    opened_contours = np.ones(img.shape, np.uint8) * 255

    cv2.drawContours(opened_contours,contours,-1, 0, 1 )
    if(debug):
        cv2.imwrite("contoured_img.png",img)
        cv2.imwrite("img_parent.png",img_parent)
        cv2.imwrite("dilated.png",dilated)
        cv2.imwrite("edges.png",edges)
        cv2.imwrite("img_inner_contour.png",img_inner_contour)
        cv2.imwrite("eroded.png",eroded)
        cv2.imwrite("opened_contours.png",opened_contours)
    return opened_contours,contours

