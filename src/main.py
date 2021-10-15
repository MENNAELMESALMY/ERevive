import numpy as np
from preprocessing import *
from removeLines import *
from ContourDetection import *
from detection.shapes_detection import detect_shapes
import cv2

def detectWeakHelper(img):
    h,w = img.shape
    countStartZerosVer = []
    #countStartZerosH = 0
    img = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, None, value = 255)
    #vertical
    for j in range(w+10):
        countCol=0
        for i in range(h-1):
            if(img[i,j]==255 and img[i+1,j]==0):
                countCol+=1
        countStartZerosVer.append(countCol)

    # for i in range(w-1):
    #     if(img[int(h/2+5),i]==255 and img[int(h/2+5),i+1]==0):
    #         countStartZerosH+=1
    countAllVer = sum([1 for i in countStartZerosVer if i >=3])
    return countAllVer/len(countStartZerosVer) >= 0.5

def detectWeak(img,contours,shapes):
    bin_img = (img >180)*255
    bin_img = bin_img.astype(np.uint8)
    isWeak = []
    i=0
    hImg,wImg = img.shape
    for c,s in zip(contours,shapes):
        x,y,w,h = cv2.boundingRect(c)
        w = min(x+w+15,wImg)
        h = min(y+h+15,hImg)
        x = max(0,x-15)
        y = max(0,y-15)

        c_small = scale_contours([c.copy()],0.65)
        cv2.drawContours(bin_img,c_small,-1,255,-1)
        imgContour = bin_img[y:h,x:w]
        cv2.imwrite('bin_img'+str(i)+'.png',imgContour)
        i+=1
        isWeak.append(detectWeakHelper(imgContour))
        
    return isWeak


img_dir ="input/16.jpeg"
adjustPrespective,approxContour,grayImg = GetMaxContour(img_dir)
warpedImg = grayImg
if(adjustPrespective):
    warpedImg = warpedPrespective(grayImg,approxContour)
shadowFreeImg = RemoveShadow(warpedImg,True)
binarizedImg = Binarize(shadowFreeImg,True)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
image_result = binarizedImg.astype(np.uint8).copy()
#image_result = cv2.erode(image_result, kernel,iterations=4)

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
hulls = [h for h in hulls if not isOverlapped(h,hulls)]
cv2.drawContours(im,hulls,-1, 0, 1 )
cv2.imwrite("im_hull.png",im)
cv2.imwrite("allContoursImg.png",allContoursImg)
##############################################################
shapes_no = seperateShapes( hulls,allContoursImg, binarizedImg)
shapes = detect_shapes(shapes_no)
weak = detectWeak(shadowFreeImg,hulls,shapes)
print(shapes)
print(weak)
