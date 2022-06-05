import math
import os
import numpy as np
import cv2 as cv
from skimage.util import invert
from skimage.morphology import dilation


def get_shape_features(img):
    # white shape with black background
    contours = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    shape_contour = contours[0]
    for c in contours:
        if cv.contourArea(c) > cv.contourArea(shape_contour):
            shape_contour = c
    #get the convex hull    
    hull = cv.convexHull(shape_contour)
    #draw it
    drawing = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    #draw contour
    cv.drawContours(drawing, [shape_contour], 0, (0, 255, 0), 1)
    #draw hull
    cv.drawContours(drawing, [hull], 0, (0, 0, 255), 1)
    #show(drawing)
    #get the max rectangle inside the shape
    rotated_rect = cv.minAreaRect(shape_contour)
    rotated_box = cv.boxPoints(rotated_rect)
    rotated_box = np.int0(rotated_box)
    cv.drawContours(drawing, [rotated_box], 0, (0, 0, 255), 1)

    straight_rect = cv.boundingRect(shape_contour)
    cv.rectangle(drawing, (straight_rect[0], straight_rect[1]), (straight_rect[0] + straight_rect[2], straight_rect[1] + straight_rect[3]), (0, 255, 0), 1)
    #show(drawing)
    ellipse = cv.fitEllipse(shape_contour)
    cv.ellipse(drawing,ellipse,(0,255,0),2)
    
    #show(drawing)

    contour_area = cv.contourArea(shape_contour)
    hull_area = cv.contourArea(hull)
    contour_area = hull_area
    rect_area = cv.contourArea(rotated_box)
    rect_solidity = contour_area / rect_area
    straight_rect_area = straight_rect[2] * straight_rect[3]
    straight_rect_solidity = contour_area / straight_rect_area
    ellipse_area = (math.pi * ellipse[1][0] * ellipse[1][1]) / 4
    ellipse_solidity = contour_area / ellipse_area
    print("Contour area: ", contour_area)
    print("Rect area: ", rect_area)
    print("Rect solidity: ", rect_solidity)
    print("Straight rect area: ", straight_rect_area)   
    print("Straight rect solidity: ", straight_rect_solidity)
    print("Ellipse area: ", ellipse_area)
    print("Ellipse solidity: ", ellipse_solidity)

    shape=""
    if rect_solidity > 0.8 and straight_rect_solidity > 0.8 and ellipse_solidity < 0.95:
        shape='rectangle'
    elif rect_solidity > 0.6 and straight_rect_solidity < 0.6 and ellipse_solidity < 0.95:
        shape='diamond'
    else:
        shape='oval'
    return shape

    





def show(img):
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()



def fillHole(img):
    #thresholded image
    #show(img)
    im_th = img
    im_floodfill = im_th.copy()
    h, w = im_th.shape[:2]
    ##print(h,w)
    ##print(im_th.shape)
    mask = np.zeros((h+2, w+2), np.uint8)
    #show(mask)
    #show(im_floodfill)
    cv.floodFill(im_floodfill, mask, (0, 0), 255)
    #show(im_floodfill)
    im_floodfill_inv = cv.bitwise_not(im_floodfill)
    #show(im_floodfill_inv)
    im_out = im_th | im_floodfill_inv
    smoothed_img = cv.medianBlur(im_out,7)
    #show(smoothed_img)
    return smoothed_img

def convex_hull(image):
    chull = fillHole(image)
    contours = cv.findContours(chull, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    contour = contours[0]
    for c in contours:
        if cv.contourArea(c) > cv.contourArea(contour):
            contour = c

    empty_img = np.zeros((chull.shape[0], chull.shape[1]), dtype=np.uint8)
    contourImg = cv.drawContours(empty_img, [contour], 0, (255, 255, 255), 1)
    contourImg = fillHole(contourImg)
    #show(contourImg)
    return get_shape_features(contourImg)
 

    
    
 
#gray scale img with white background
def get_features(img):
    img = cv.resize(img, (256, 256)) 
    img = cv.copyMakeBorder(img,5,5,5,5,cv.BORDER_CONSTANT,value=[255,255,255]) 
    #show(img)     
    img = invert(img)
    #show(img)
    img = dilation(img,np.ones((5,5)))
    #show(img)
    shape = convex_hull(img)

    return shape


def detect_shapes(shapes_no):
    shapes = []
    for i in range(shapes_no):
        path = './output/shape'+str(i)+'.png'
        img = cv.imread(path)
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        shape = get_features(gray_img)
        shapes.append(shape)
            
    return shapes


#detect_shapes(12)