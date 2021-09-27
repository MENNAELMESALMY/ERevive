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
    im2, contours_cv, hierarchy = cv2.findContours(im_filled, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
    #[Next, Previous, First_Child, Parent]
    im_empty = np.ones((hImg, wImg,3), np.uint8) * 255
    i=0
    for cnt in contours_cv:
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
        if(child1Idx != -1 and  hierarchy[child1Idx][0] == -1):
            x1,y1,w1,h1 = cv2.boundingRect(contours_cv[child1Idx])
            if(w1/w >= 0.3):
                cv2.drawContours(im_empty, contours_cv, i, (0,0,0), 1)
        if(not hasChildren and acceptedArea and w/h >= 1.8 and w/h<=8):
            print(w/h,w,h)
            cv2.drawContours(im_empty, contours_cv, i, (0,0,0), 1)

        i+=1
    if(debug):
        cv2.imwrite("contoured.png", im_empty[:,:,0])
    return im_empty[:,:,0]