import numpy as np
from .preprocessing import *
from .removeLines import *
from .ContourDetection import *
from .detection.shapes_detection import detect_shapes
from .detectWeak import *
from .schemaGeneration.connectComponents import *
from .detect_rel_prop import *
from .OCR import *
from .dataTypesPrediction.scripts.dataTypePrediction import *
from .schemaGeneration.schema_generation import *
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

##12,17,40,24,13,14 ,18 are good tests
#img_dirs =["12.png"]#os.listdir("input")
#print(img_dirs)
#dirs = os.listdir('input')
#for idx,img_dir in enumerate(dirs):
#print("starting..................",img_dirs)
#sort the images in the input folder by their name
#img_dirs.sort()
def process_image(img_dir):
    print("starting..................") 
    print(img_dir)
    print("processing img:  "+img_dir)
    pre = img_dir.split('.')[0]
    try:
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
        print("######### Start Shapes Detection #########")
        shapes = detect_shapes(shapes_no)
        
        weak = detectWeak(shadowFreeImg,finalContours)

        textArr,isKey = OCR()
        #print(textArr)
        #print(isKey)
        print("######### Start Types Prediction #########")
        dataTypesArr = predictWordsTypes(textArr)
        #print(dataTypesDic)
        #print(textArr)
        textArr, dataTypesArr = addDefaultNames(shapes, textArr, dataTypesArr)
        #print(textArr)
        #print("????????????????????//")
        print("######### Start Connecting EntdataTypesArrities #########")
        scaled_contours = scale_contours(finalContours[:],1.17)
        connectedComponents,skeleton = connectEntities(scaled_contours,finalContours,binarizedImg,shapes,textArr,weak,isKey,dataTypesArr)
        print("///////////////////////////////////////////")
        print(textArr,isKey)
        print("######### Start Participation #########")
        relations = get_relations(skeleton,connectedComponents)
        print("######### Start Cardinality #########")
        relations = cardinality(relations,skeleton,binarizedImg)
        print("///////////////////////////////////////////")
        #connectEntities(finalContours,binarizedImg,shapes)
        connectedComponents = removeContours(connectedComponents)
        relations = removeContoursRelations(relations)
        connectedComponents, shapes_no = addDefaultKey(connectedComponents, shapes_no)

        print(connectedComponents,relations)
        print("///////////////////////////////////////////")
        #print(relations)

        schema = generateSchema(connectedComponents,relations,shapes_no)

        print("///////////////////////////////////////////")
        #print(relations)

        print("///////////////////////////////////////////")
        #print(schema)
        with open("1.json", "w") as json_file:
             json.dump(schema, json_file)
        #return to the current directory
        os.chdir('./..')
        return schema
    except Exception as e:
        # with open("schema"+pre+".json", "w") as json_file:
        #     json.dump({"error":str(e)}, json_file)
        print(e)
        os.chdir('./..')
        return False
        

    # #print(shapes)
    # for i,w in enumerate(weak):
    #     if w:
    #         #print(i)
    # #print(weak)
