from skimage import io
import numpy as np
import sys
import cv2 as cv
from matplotlib import pyplot as plt
from skimage.util import invert
from skimage.morphology import dilation
from max_rect import get_max_rect, max_triangle
from  min_bounding_rect import *






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
    im_floodfill_inv = cv.bitwise_not(im_floodfill)
    im_out = im_th | im_floodfill_inv
    smoothed_img = cv.medianBlur(im_out,7)

    return smoothed_img

def convex_hull(image):
    chull = fillHole(image)
    contours = cv.findContours(chull, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    contour = contours[0]
    for c in contours:
        if cv.contourArea(c) > cv.contourArea(contour):
            contour = c
    Ach = cv.contourArea(contour)
    Alq,rect = get_max_rect(chull)
    contour = np.swapaxes(contour,0,1)
    contour  =contour[0]
    (rot_angle, area, width, height, center_point, corner_points) = minBoundingRect(contour)
    Aer = area
    Atr,p1,p2,p3 = max_triangle(contour)
    
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
    elif features[0]>0.7 and features[1] >0.55 and features[2]>0.6:
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
        shapes.append(shape)
            
    return shapes
        



