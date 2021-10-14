import numpy as np
from preprocessing import *
from removeLines import *
from ContourDetection import *
from detection.shapes_detection import detect_shapes
import cv2
img_dir ="input/11.png"
adjustPrespective,approxContour,grayImg = GetMaxContour(img_dir)
warpedImg = grayImg
if(adjustPrespective):
    warpedImg = warpedPrespective(grayImg,approxContour)
shadowFreeImg = RemoveShadow(warpedImg,True)
binarizedImg = Binarize(shadowFreeImg,True)
image_result = binarizedImg.astype(np.uint8).copy()
filledImg = FloodFromCorners(image_result.copy(),True)
contourdImg,filtered_contoures = getClosedShapes(filledImg,True)
filtered_contoures_copy = filtered_contoures.copy() 
opendContourdImg,opened_contours = getOpenedContours(image_result.copy(),filtered_contoures_copy,True)
allContoursImg = 255 - ((255 - opendContourdImg ) + (255 - contourdImg))
allContours = filtered_contoures + opened_contours
im = np.ones(binarizedImg.shape, np.uint8) * 255
hulls=[]
for c in allContours:
    if cv2.contourArea(c) >= 700:
        #print(cv2.contourArea(c))
        hulls.append(cv2.convexHull(c, False))

getDerived(image_result.copy(),hulls.copy())
hulls = scale_contours(hulls,0.95)
cv2.drawContours(im,hulls,-1, 0, 1 )
cv2.imwrite("im_hull.png",im)
cv2.imwrite("allContoursImg.png",allContoursImg)
##############################################################
shapes_no = seperateShapes( hulls,allContoursImg, binarizedImg)
shapes = detect_shapes(shapes_no)
print(shapes)
