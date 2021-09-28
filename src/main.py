import numpy as np
from preprocessing import *
from removeLines import *
from ContourDetection import *
from detection.shapes_detection import detect_shapes
img_dir ="input/8.jpeg"
adjustPrespective,approxContour,grayImg = GetMaxContour(img_dir)
warpedImg = grayImg
if(adjustPrespective):
    warpedImg = warpedPrespective(grayImg,approxContour)
shadowFreeImg = RemoveShadow(warpedImg,True)
binarizedImg = Binarize(shadowFreeImg,True)
filledImg = FloodFromCorners(binarizedImg.astype(np.uint8).copy(),True)
contourdImg,filtered_contoures = getClosedShapes(filledImg,True)
shapes_no = seperateShapes(filtered_contoures , contourdImg , binarizedImg)
shapes = detect_shapes(shapes_no)
print(shapes)