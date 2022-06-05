import numpy as np
from ImageProcessing.preprocessing import *
from ImageProcessing.removeLines import *
from ContourDetection import *
from detection.shapes_detection import detect_shapes
from ImageProcessing.detectWeak import *
from ImageProcessing.connectComponents import *
from ImageProcessing.detect_rel_prop import *
from ImageProcessing.OCR import *
from dataTypesPrediction.scripts.dataTypePrediction import *
from schema_generation import *
import cv2
import os


def changeContours(contours, img,idx):
    empty = np.zeros(img.shape,np.uint8)
    cv2.drawContours(empty, [contours], -1, 255, 1)
    #cv2.imwrite("/home/menna/Downloads/GP/src/debug_"+str(idx)+".png", empty)
    actual_contour = np.where(empty==255)
    actual_contour = list(actual_contour)
    contour = list(zip(*actual_contour))
    return  np.array([contour])


img_dirs =["24.png"]

#dirs = os.listdir('input')
#for idx,img_dir in enumerate(dirs):
#print("starting..................",img_dir)
for idx,img_dir in enumerate(img_dirs):
    print("processing img"+str(idx))
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


    allContours,_ = removeOutliers(allContours,True,hImg,wImg,allContours) #outliers by area
    allContours,_ = removeOutliers(allContours,False,hImg,wImg,allContours) #outliers by aspect ratio

    allContours = scale_contours(allContours,0.95)
    allContours = [h for h in allContours if not isOverlapped(h,allContours)]
    getDerived(image_result.copy(),allContours.copy())

    cv2.drawContours(im,allContours,-1, 0, 1 )
    cv2.imwrite("final_out_shapes/im_hull"+pre+".png",im)
    ##############################################################

    finalContours = checkInside(allContours,binarizedImg)
    finalContours =[ cv2.convexHull(c,False) for c in finalContours]


    shapes_no = seperateShapes(finalContours,allContoursImg, binarizedImg)
    im = np.ones(binarizedImg.shape, np.uint8) * 255
    cv2.drawContours(im,finalContours,-1, 0, 1 )
    cv2.imwrite("final_out_shapes/im_final"+pre+".png",im)
    #print(shapes_no)
    shapes = detect_shapes(shapes_no)

    weak = detectWeak(shadowFreeImg,finalContours)

    textArr,isKey = OCR()
    #print(textArr)
    #print(isKey)

    dataTypesDic , dataTypesArr = predictWordsTypes(textArr)
    #print(dataTypesDic)

    scaled_contours = scale_contours(finalContours[:],1.17)
    connectedComponents,skeleton = connectEntities(scaled_contours,finalContours,binarizedImg,shapes,textArr,weak,isKey,dataTypesArr)

    print("///////////////////////////////////////////")
    print(textArr,isKey)
    
    relations = get_relations(skeleton,connectedComponents)
    relations = cardinality(relations,skeleton,binarizedImg)
    print("///////////////////////////////////////////")
    #connectEntities(finalContours,binarizedImg,shapes)
    connectedComponents = removeContours(connectedComponents)

    #print(connectedComponents)
    
    relations = removeContoursRelations(relations)

    print("///////////////////////////////////////////")
    #print(relations)

    schema = generateSchema(connectedComponents,relations,shapes_no)

    print("///////////////////////////////////////////")
    #print(relations)

    print("///////////////////////////////////////////")
    print(schema)

    # #print(shapes)
    # for i,w in enumerate(weak):
    #     if w:
    #         #print(i)
    # #print(weak)
