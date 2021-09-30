from skimage import io
import numpy as np
import sys
import cv2 as cv
from matplotlib import pyplot as plt
from skimage.util import invert
from skimage.morphology import dilation
from detection.max_rect import get_max_rect, max_triangle
from  detection.min_bounding_rect import *






def show(img):
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()



def fillHole(img):
    #thresholded image
    
    im_th = img
    im_floodfill = im_th.copy()
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
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
    #get the convex hull
    hull = cv.convexHull(contour)
    #draw it
    drawing = np.zeros((chull.shape[0], chull.shape[1], 3), dtype=np.uint8)
    cv.drawContours(drawing, [contour], 0, (0, 255, 0), 1)
    cv.drawContours(drawing, [hull], 0, (0, 0, 255), 1)
    #show(drawing)

    Ach = cv.contourArea(contour)
    empty_img = np.zeros((chull.shape[0], chull.shape[1]), dtype=np.uint8)
    contourImg = cv.drawContours(empty_img, [contour], 0, (255, 255, 255), 1)
    contourImg = fillHole(contourImg)
    #show(contourImg)
    Alq,rect = get_max_rect(contourImg)
    #show(rect)
    contour = np.swapaxes(contour,0,1)
    contour  =contour[0]
    (rot_angle, area, width, height, center_point, corner_points) = minBoundingRect(contour)
    Aer = area
    Atr,p1,p2,p3 = max_triangle(contour)
    line1 = cv.line(drawing, tuple(p1), tuple(p2), (0, 0, 255), 1)
    line2 = cv.line(drawing, tuple(p2), tuple(p3), (0, 0, 255), 1)
    line3 = cv.line(drawing, tuple(p3), tuple(p1), (0, 0, 255), 1)
    #show(drawing)
    #print(Ach,Alq,Aer,Atr)
    rect_feature_1 = Ach/Aer
    rect_feature_2 = Alq/Aer
    oval_feature_1 = Alq/Ach
    diamond_feature_1 = Atr/Ach
    features = [rect_feature_1,rect_feature_2,oval_feature_1,diamond_feature_1]
    return features

    
    
 
#gray scale img with white background
def get_features(img):
    img = cv.resize(img, (256, 256)) 
    img = cv.copyMakeBorder(img,5,5,5,5,cv.BORDER_CONSTANT,value=[255,255,255])   
    img = invert(img)
    img = dilation(img,np.ones((5,5)))
    features = convex_hull(img)
    shape=''
    if features[2] >0.3 and features[2] <0.75 and features[3] <0.46:
        shape='oval'
    elif features[0]>0.7 and features[1] >0.5 and features[2]>0.6 and features[3]<0.52:
        shape='rectangle'
    else:
        shape='diamond'
    return features,shape


def detect_shapes(shapes_no):
    shapes = []
    for i in range(shapes_no):
        path = './output/shape'+str(i)+'.png'
        img = cv.imread(path)
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        features,shape = get_features(gray_img)
        print(features)
        shapes.append(shape)
            
    return shapes


