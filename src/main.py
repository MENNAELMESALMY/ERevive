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
filledImg = FloodFromCorners(binarizedImg.astype(np.uint8).copy(),True)
contourdImg,filtered_contoures = getClosedShapes(filledImg,True)
image_result = binarizedImg.astype(np.uint8).copy()
opendContourdImg,opened_contours = getOpenedContours(image_result,filtered_contoures,True)
allContoursImg = 255 - ((255 - opendContourdImg ) + (255 - contourdImg))
allContours = filtered_contoures + opened_contours
print(len(allContours))
cv2.imwrite("allContoursImg.png",allContoursImg)
###############################
shapes_no = seperateShapes( allContours ,allContoursImg, binarizedImg)
shapes = detect_shapes(shapes_no)
print(shapes)