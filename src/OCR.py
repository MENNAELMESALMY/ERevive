import pytesseract
import cv2
import numpy as np
import skimage.io as io
import os

#################### Detect Keys ######################################
def keyDetection(image):
    
    ######### getting all contours in image ###############
    contours , _ = cv2.findContours(image , cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  

    ########### detect contour of line #############
    #1- the most bottom contour
    #2- width > 1/2 of image
    bottom = 0
    lineIndex = 0
    index = 0
    keyFound = False

    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        
        if y > image.shape[0]//2 and w > image.shape[1]//4 and h < image.shape[0]//4:
            lineIndex = index
            keyFound = True
        index+=1

    ############# delete contour of line #############
    if keyFound == True:
        x,y,w,h = cv2.boundingRect(contours[lineIndex])
        image[y:y+h,x:x+w] = 255
    return keyFound,image


#################### Reading text files ###############################
def OCR():
    os.chdir('./output')
    #print(os.getcwd())
    textArr = []
    numFiles = 0
    isKey = []
    keyFound = False

    for count, f in enumerate(os.listdir()):
        f_name, f_ext = os.path.splitext(f)
        if (f_name[0:4] == "text") and (int(f_name[4:]) > numFiles):
            numFiles = int(f_name[4:])

    for i in range (numFiles+1):
            image = cv2.imread("./text" + str(i) + ".png")
            image = 255 - image

            greyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            threshold , binarizedImage = cv2.threshold(greyImage , 150 , 255 , cv2.THRESH_BINARY)

            outImg = np.ones((image.shape),np.uint8)
            keyFound,outImg = keyDetection(binarizedImage)
            isKey.append(keyFound)

            custom_config = r'--oem 3 --psm 6'
            extractedText = pytesseract.image_to_string(outImg,config=custom_config)
            if extractedText == "\x0c":
                extractedText = ""
            else:
                extractedText = extractedText.split('\n')[0]
            textArr.append(extractedText)
            
    return textArr,isKey
