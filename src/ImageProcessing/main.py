from time import time
from tracemalloc import start
import numpy as np
from .preprocessing import *
from .remove_lines import *
from .contour_detection import *
from .ShapesClassification.shapes_detection import detect_shapes
from .detect_weak import *
from .SchemaGeneration.connect_components import *
from .detect_relations_props import *
from .ocr import *
from .DataTypesPrediction.scripts.datatypes_prediction import *
from .SchemaGeneration.schema_generation import *
from .testing import *
import cv2
import os
import timeit
import json


def changeContours(contours, img,idx):
    empty = np.zeros(img.shape,np.uint8)
    cv2.drawContours(empty, [contours], -1, 255, 1)
    actual_contour = np.where(empty==255)
    actual_contour = list(actual_contour)
    contour = list(zip(*actual_contour))
    return  np.array([contour])


def process_image(img_dir):

    pre = img_dir.split('.')[0]
    if "/" in pre: pre = pre.split("/")[-1]
    try:
        start = timeit.default_timer()

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

        finalContours = checkInside(allContours,binarizedImg)
        finalContours =[ cv2.convexHull(c,False) for c in finalContours]


        shapes_no = seperateShapes(finalContours,allContoursImg, binarizedImg)
        im = np.ones(binarizedImg.shape, np.uint8) * 255
        cv2.drawContours(im,finalContours,-1, 0, 1 )
        cv2.imwrite("final_out_shapes/im_final"+pre+".png",im)
        shapes = detect_shapes(shapes_no)
        
        weak = detectWeak(shadowFreeImg,finalContours)

        textArr,isKey = OCR()
        dataTypesArr = predictWordsTypes(textArr)
        textArr, dataTypesArr = addDefaultNames(shapes, textArr, dataTypesArr)

        end = timeit.default_timer()
        total_time = (end-start)
        with open("../timing"+str(pre)+".txt","w+") as file:
            file.write(f"Preprocessing and shape detection time is {str(end-start)} \n")

        start = timeit.default_timer()
        scaled_contours = scale_contours(finalContours[:],1.17)
        connectedComponents,skeleton = connectEntities(scaled_contours,finalContours,binarizedImg,shapes,textArr,weak,isKey,dataTypesArr)
        end = timeit.default_timer()
        total_time += (end-start)
        with open("../timing"+str(pre)+".txt","a+") as file:
            file.write(f"connect components time is {str(end-start)}\n")


        start = timeit.default_timer()
        relations = get_relations(skeleton,connectedComponents)
        end = timeit.default_timer()
        total_time += (end-start)
        with open("../timing"+str(pre)+".txt","a+") as file:
            file.write(f"get relations time is {str(end-start)}\n")

        start = timeit.default_timer()
        relations = cardinality(relations,skeleton,binarizedImg)
        end = timeit.default_timer()
        total_time += (end-start)
        with open("../timing"+str(pre)+".txt","a+") as file:
            file.write(f"Cardinality time is {str(end-start)}\n")
        start = timeit.default_timer()
        connectedComponents = removeContours(connectedComponents)
        relations = removeContoursRelations(relations)
        connectedComponents, shapes_no = addDefaultKey(connectedComponents, shapes_no)


        schema = generateSchema(connectedComponents,relations,shapes_no)
        end = timeit.default_timer()
        total_time += (end-start)
        with open("../timing"+str(pre)+".txt","a+") as file:
            file.write(f"generating schema time is {str(end-start)}\n")
            

        detected_shapes = shapes_statistics(shapes,weak,isKey,relations,total_time,dataTypesArr)

        with open("schema.json", "w") as json_file:
             json.dump(schema, json_file)
        with open("relations.json", "w") as json_file:
             json.dump(relations, json_file)
        os.chdir('./..')
        return schema,detected_shapes

    except Exception as e:

        print(e)
        os.chdir('./..')
        return False
        

