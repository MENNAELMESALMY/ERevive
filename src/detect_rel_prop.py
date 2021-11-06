import numpy as np
import cv2 as cv
import math
from skimage.morphology import dilation
from path_points import *
from utility import fillHole
import pytesseract
def check_direct_path(path,entities,orig_entity,relations,orig_relation):
    set_path =set(tuple(x) for x in path)
    for entity in entities:
        if entity["idx"]==orig_entity["idx"]:
            continue
        contour = entity["contour"][0]
        contour = [[point[0],point[1]] for point in contour]
        set_contour = set(tuple([x[1],x[0]]) for x in list(contour))
        if len(set_path.intersection(set_contour))!=0:
            return False
    for relation in relations:
        if relation["idx"]==orig_relation["idx"]:
            continue
        contour = relation["contour"][0]
        contour = [[point[0],point[1]] for point in contour]
        set_contour = set(tuple([x[1],x[0]]) for x in contour)
        if len(set_path.intersection(set_contour))!=0:
            return False
    return True

def filter_paths(paths,entities,entity,relations,relation,img):
    ret_paths=[]
    paths = sorted(paths, key=lambda x: len(x))

    k=0
    for path in paths:
        empty = img.copy()
        for point in path:
            empty[point[0]][point[1]]=150
        cv.imwrite("path_bef_"+str(entity["idx"])+"_"+str(relation["idx"])+"_"+str(k)+".png",empty)
        k+=1
    false_indicies=[]
    ret_paths=[]
    for i in range(0,len(paths)):
        if not i in false_indicies:
            ret_paths.append(paths[i])        
        for j in range(i+1,len(paths)):
            if j>=len(paths):
                continue
            path1 = set(tuple(x) for x in paths[i])
            path2 = set(tuple(x) for x in paths[j])
            intersection = path1.intersection(path2)
            shortest = list(path1)
            if len(intersection)/len(shortest)>=0.5:
                false_indicies.append(j)

    k=0
    for path in ret_paths:
        empty = img.copy()
        for point in path:
            empty[point[0]][point[1]]=150
        cv.imwrite("path_between_"+str(entity["idx"])+"_"+str(relation["idx"])+"_"+str(k)+".png",empty)
        k+=1
    final_paths=[]
    for path in ret_paths:
        if(check_direct_path(path,entities,entity,relations,relation)):
            final_paths.append(path)
    return final_paths


def getMaxBorders(points):
    min_x = np.min(points[:,0])
    max_x = np.max(points[:,0])
    min_y = np.min(points[:,1])
    max_y = np.max(points[:,1])
    center = (max_x+min_x)//2,(max_y+min_y)//2
    rights = np.where(points[:,0]>center[0])
    rights = points[rights]
    lefts = np.where(points[:,0]<center[0])
    lefts = points[lefts]
    tops = np.where(points[:,1]<center[1])
    tops = points[tops]
    bottoms = np.where(points[:,1]>center[1])
    bottoms = points[bottoms]
    max_right = rights[np.argmax(rights[:,0])]
    max_left = lefts[np.argmin(lefts[:,0])]
    max_top = tops[np.argmax(tops[0,:])]
    max_bottom = bottoms[np.argmin(bottoms[0,:])] 
    return max_right,max_left,max_top,max_bottom
        
def get_paths(p2,binarized_img,center,contour,entity,r,e):
    pathed_img = binarized_img.copy()    
    points = contour[0]
    max_right,max_left,max_top,max_bottom = getMaxBorders(points)
    p1s = [max_right,max_left,max_right,max_left,max_top,max_bottom]
    paths=[]
    for i in range(6):
        pathed_img,path,is_found = BFS(p1s[i],p2[0],pathed_img.copy(),contour[0],entity[0])
        if not is_found:
            break
        paths.append(path)
   
    return paths



def get_contour(img):
    chull = fillHole(img)
    contours = cv.findContours(chull, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    contour = contours[0]
    for c in contours:
        if cv.contourArea(c) > cv.contourArea(contour):
            contour = c
    empty = np.zeros(img.shape,np.uint8)
    cv.drawContours(empty, [contour], -1, 255,  cv.FILLED)
    actual_contour = np.where(empty==255)
    actual_contour = list(actual_contour)
    actual_contour.reverse()
    contour = list(zip(*actual_contour))
    return  np.array([contour])

def filter_points(contourOrig,binarizedImgOrig,relation=None,entity=None):
    contour_points = []
    binarizedImg = binarizedImgOrig.copy()
    contour = contourOrig.copy()

    empty = np.zeros(binarizedImg.shape,np.uint8)
    cv.drawContours(empty, [contour], -1, (255,255,255), 1)
    empty = dilation(empty,np.ones((10,10),np.uint8))
    contour = get_contour(empty)
    if relation:
        relation["contour_cardinality"] = contour

    for points in contour:
        for point in points:
            if binarizedImg[point[1]][point[0]] == 0:
                continue
            contour_points.append(list(point))
    
    return np.array([contour_points])


def detect_participation(relations,edges):
    for relation in relations.values():
        for entity in relation["entities"]:
            relation["contour"] = filter_points(relation["contour"].copy(),edges.copy(),relation)
            entity["contour"] = filter_points(entity["contour"].copy(),edges.copy(),entity=entity)
 
    for relation in relations.values():
        rel_paths=[]
        for entity in relation["entities"]:
        
            entity_point = np.random.randint(0,len(entity["contour"]))
            entity_point = entity["contour"][entity_point]

            paths = get_paths(entity_point,edges,relation["bounding_box"],relation["contour"],entity["contour"],relation["idx"],entity["idx"])
            paths = filter_paths(paths,relation["entities"],entity,relations.values(),relation,edges)
            if(len(paths)==1):
                entity["participation"]="partial"
            elif(len(paths)==2):
                entity["participation"]="full"

            entity.pop("relations",None)
            p=0
            for path in paths:
                rel_paths.append(path)
                edges_test = (edges.copy())
                for point in path:   
                    edges_test[point[0]][point[1]]=150
                cv.imwrite("pathed_final"+str(entity["idx"])+"_"+str(relation["idx"])+"_"+str(p)+".png",edges_test)
                p+=1
            entity["paths"] = paths
        relation["paths"] = rel_paths.copy()
            
def get_relations(binarizedImg,entities):
    relations = {}
    for entity in entities:
        for relation in entity["relations"]:
            bounding_box_str = str(relation["bounding_box"])
            if relations.get(bounding_box_str) is None:
                relations[bounding_box_str] = {
                    "entities":[]
                }
            relations[bounding_box_str]["entities"].append(entity)
            relations[bounding_box_str].update({
                "idx":relation["idx"],
                "name":relation["name"],
                "contour":relation["contour"],
                "bounding_box":relation["bounding_box"]
            })

    detect_participation(relations,binarizedImg)
    return relations


def cardinality(relations,img):
    count = 0
    img=255-img
    for relation in relations.values():
        x,y,w,h = relation["bounding_box"]
        rows = [p[0] for p in relation["contour_cardinality"][0]]
        cols = [p[1] for p in relation["contour_cardinality"][0]]
        img[cols,rows]=255
        for path in relation["paths"]:
            rows = [p[0] for p in path]
            cols = [p[1] for p in path]
            img[rows,cols]=255 

        ## get point[0] of path of relation to determine the direction from relation
        ## get the most left,right,top or bottom of relation according to the
        ## direction of path detected
        ## take a proper window to include cardinalities of relation 
        c2 = 0
        for entity in relation["entities"]:
            centerX = x + w//2
            centerY = y + h//2
            pathX,pathY = entity["paths"][0][0]
            borderPoint = detectDirectionPath((pathX,pathY),(centerY,centerX),w,h,relation["contour_cardinality"][0])

            cardinality_img = img.copy()
            #cardinality_img[borderPoint[1]][borderPoint[0]] = 150
            black_img = np.zeros(img.shape)
            cardinality_img[pathX][pathY] = 150
            black_img[pathX][pathY] = 150
            cv.imwrite("card_black"+ str(count) + str(c2) + ".png",black_img)
            cv.imwrite("card"+ str(count) + str(c2) + ".png",cardinality_img)
            c2 += 1
     


        ######################### old method of detecting cardinalities from expanding window of relation #########
        # width = 2*w
        # height = 2*h
        # x = x-int(0.5*w)
        # y = y-int(0.5*h)
        # if x<0:
        #     x=0
        # if y<0:
        #     y=0
        # if x+width>img.shape[1]:
        #     width = img.shape[1]-x
        # if y+height>img.shape[0]:
        #     height = img.shape[0]-y
        # cardinality_img = img.copy()
        # cardinality_img = img[y:y+height,x:x+width].copy()



        #cv.imwrite("card"+ str(count) + ".png",cardinality_img)
        #relation["cardinality"] = get_relation_cardinality(cardinality_img,relation,count)

        # if two contours minimum found
        # img[y:y+height,x:x+width]= 150
        # cv.imwrite("card_rel_path"+ str(count) + ".png",img)
        ##############################################################################
        count+=1

def distance(p1,p2):
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

def between(p1,p2,p3):
    return math.isclose(distance(p1,p3)+distance(p2,p3),distance(p1,p2),rel_tol=0.5)

def get_relation_cardinality(cardinality_img,relation,count):
    contours = cv.findContours(cardinality_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    cardinalities=[]
    cardinalities_text=[]
    number_of_cards = len(relation["entities"])

    if len(contours) < number_of_cards:
        print("Error in detecting cardinalities")
        return
    elif len(contours)==number_of_cards:
        cardinalities.extend(contours)
    else:
        contours = sorted(contours, key=lambda x: cv.contourArea(x))
        cardinalities.extend(contours[0:number_of_cards])
    x,y,w,h = relation["bounding_box"]
    center_relation = (x+w//2,y+h//2)
    cardinalities_text = classify_cardinalities(cardinalities,cardinality_img,count)

    ################### donot forget to uncomment this block#####################
    # for i in range(number_of_cards):
    #     x1,y1,w1,h1= cv.boundingRect(cardinalities[i])
    #     center_cardinality = (x1+w1//2,y1+h1//2)
    #     for entity in relation["entities"]:
    #         x2,y2,w2,h2= cv.boundingRect(entity)
    #         center_entity = (x2+w2//2,y2+h2//2)
    #         if between(center_relation,center_entity,center_cardinality):
    #             entity["cardinality"]=cardinalities_text[i]
    #             break
    ##############################################################################
            
def classify_cardinalities(cardinalities,cardinality_img,count):
    # iterate for each image send and classify the cardinalities return (array)
    card_list = []
    c1 = count
    c2 = 0
    print(cardinalities)
    for img in cardinalities:
        x,y,w,h= cv.boundingRect(img)
        cardinality_img[x:x+h,y:y+w] = 150
        cv.imwrite("test_card" + str(count) + "_" + str(c2) + ".png",cardinality_img)
        card_image = cardinality_img[x:x+h,y:y+w]
        cv.imwrite("final_card" + str(count) + "_" + str(c2) + ".png",card_image)
        c2 += 1
        custom_config = r'--oem 3 --psm 6'
        extractedText = pytesseract.image_to_string(card_image,config=custom_config)
        if extractedText == "\x0c":
            extractedText = ""
        else:
            extractedText = extractedText.split('\n')[0]
        card_list.append(extractedText)

    print(card_list)
    return card_list

############## to determine whether there are square or rectangle contours in window ######
def noCardinalitiesContours (windowImg):
    contours = cv.findContours(windowImg, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    # return true if cardinalities still not with in image and false otherwise
    countCard = 0
    for contour in contours:
        perimeter = cv.arcLength(contour, True)
        corners = cv.approxPolyDP(contour, 0.04 * perimeter, True)
        if len(corners) == 4:
            x, y, w, h = cv.boundingRect(corners)
            aspectRatio = w / float(h)
            print(aspectRatio)
            if (aspectRatio >= 0.95 or aspectRatio <= 1.05) :
                countCard += 1

    if countCard < 2:
        return True
    else:
        return False


def detectDirectionPath (pathPoint,relCenter,relWidth,relHeight,relationContour):
    vertical = abs(pathPoint[0] - relCenter[0])
    horizontal = abs(pathPoint[1] - relCenter[1])
    max_right,max_left,max_top,max_bottom = getMaxBorders(relationContour)
    print("horizontal",horizontal)
    print("vertical",vertical)
    print("relWidth",relWidth)
    print("relHeight",relHeight)
    if horizontal > vertical:
        if pathPoint[1] > relCenter[1]:
            ##right
            return max_right
        else:
            ##left
            return max_left
    else:
        if pathPoint[0] > relCenter[0]:
            ##bottom
            return max_bottom
        else:
            ##top
            return max_top





######### problems ##########
'''
1- contours send is wrong so it cut cardinalties in wrong way
2- points on path not correct (we get points on path to detect the direction from
which we will form the window of cardinalities)
'''