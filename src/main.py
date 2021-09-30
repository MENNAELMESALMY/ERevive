import numpy as np
from preprocessing import *
from removeLines import *
from ContourDetection import *

img_dir ="input/8.jpeg"
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
shapes_no = seperateShapes(filtered_contoures , contourdImg , binarizedImg)
