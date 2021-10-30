import numpy as np
from preprocessing import *
from removeLines import *
from ContourDetection import *
from detection.shapes_detection import detect_shapes
from detectWeak import *
from connectComponents import *
import cv2
import os



img_dir ="24.png"

dirs = os.listdir('input')
print(dirs)
#for idx,img_dir in enumerate(dirs):
pre = img_dir.split('.')[0]
img_dir = 'input/'+ img_dir

adjustPrespective,approxContour,grayImg = GetMaxContour(img_dir)
warpedImg = grayImg
if(adjustPrespective):
    warpedImg = warpedPrespective(grayImg,approxContour)
shadowFreeImg = RemoveShadow(warpedImg,True)
binarizedImg = Binarize(shadowFreeImg,True)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
image_result = binarizedImg.astype(np.uint8).copy()
hImg,wImg = image_result.shape
imgArea = hImg*wImg
filledImg = FloodFromCorners(image_result.copy(),True)
contourdImg,filtered_contoures = getClosedShapes(filledImg,True)
filtered_contoures_copy = filtered_contoures.copy() 
opendContourdImg,opened_contours = getOpenedContours(image_result.copy(),filtered_contoures_copy,True)
allContoursImg = 255 - ((255 - opendContourdImg ) + (255 - contourdImg))
allContours = filtered_contoures + opened_contours
im = np.ones(binarizedImg.shape, np.uint8) * 255
hulls=[cv2.convexHull(c, False) for c in allContours]
hulls = removeOutliers(hulls,True,hImg,wImg) #outliers by area
hulls = removeOutliers(hulls,False,hImg,wImg) #outliers by aspect ratio

hulls = scale_contours(hulls,0.95)
hulls = [h for h in hulls if not isOverlapped(h,hulls)]
getDerived(image_result.copy(),hulls.copy())

cv2.drawContours(im,hulls,-1, 0, 1 )
cv2.imwrite("final_out_shapes/im_hull"+pre+".png",im)
##############################################################
shapes_no,finalContours = seperateShapes(hulls,allContoursImg, binarizedImg)
im = np.ones(binarizedImg.shape, np.uint8) * 255
cv2.drawContours(im,finalContours,-1, 0, 1 )
cv2.imwrite("final_out_shapes/im_final"+pre+".png",im)
print(shapes_no)
shapes = detect_shapes(shapes_no)
weak = detectWeak(shadowFreeImg,hulls,shapes)
connectedComponents = connectEntities(scale_contours(finalContours,1.17),binarizedImg,shapes)
#connectEntities(finalContours,binarizedImg,shapes)


# print(shapes)
# for i,w in enumerate(weak):
#     if w:
#         print(i)
# print(weak)
