import numpy as np
from preprocessing import *
from removeLines import *
from ContourDetection import *
from detection.shapes_detection import detect_shapes
import cv2
img_dir ="input/12.png"
adjustPrespective,approxContour,grayImg = GetMaxContour(img_dir)
warpedImg = grayImg
if(adjustPrespective):
    warpedImg = warpedPrespective(grayImg,approxContour)
shadowFreeImg = RemoveShadow(warpedImg,True)
binarizedImg = Binarize(shadowFreeImg,True)
filledImg = FloodFromCorners(binarizedImg.astype(np.uint8).copy(),True)
contourdImg,filtered_contoures = getClosedShapes(filledImg,True)
image_result = binarizedImg.astype(np.uint8).copy()
opendContourdImg,opened_contours = getOpenedContours(image_result,filtered_contoures.copy(),True)
allContoursImg = 255 - ((255 - opendContourdImg ) + (255 - contourdImg))
allContours = filtered_contoures + opened_contours
im = np.ones(binarizedImg.shape, np.uint8) * 255
hulls=[]
for c in allContours:
    hulls.append(cv2.convexHull(c, False))
hulls = scale_contours(hulls,0.9)
hull_filtered=[]
for hull in hulls:
    x,y,w,h = cv2.boundingRect(hull)
    print(w*h)
    if(w*h>=200):
        hull_filtered.append(hull)
cv2.drawContours(im,hull_filtered,-1, 0, 1 )
cv2.imwrite("im_hull.png",im)
cv2.imwrite("allContoursImg.png",allContoursImg)
##############################################################
shapes_no = seperateShapes( hull_filtered,allContoursImg, binarizedImg)
shapes = detect_shapes(shapes_no)
