import numpy as np
import cv2 as cv
import math
from skimage.morphology import dilation
from .path_points import *
from .utility import fillHole
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

    final_paths=[]
    for path in ret_paths:
        if(check_direct_path(path,entities,entity,relations,relation)):
            final_paths.append(path)
    return final_paths


def getMaxBorders(points_cont):
    points = points_cont.copy()
    min_x = np.min(points[:,1])
    max_x = np.max(points[:,1])
    min_y = np.min(points[:,0])
    max_y = np.max(points[:,0])
    center = (max_y+min_y)//2,(max_x+min_x)//2
    rights = np.where(points[:,1]>center[1])
    rights = points[rights]

    lefts = np.where(points[:,1]<center[1])
    lefts = points[lefts]
    tops = np.where(points[:,0]<center[0])
    tops = points[tops]
    bottoms = np.where(points[:,0]>center[0])
    bottoms = points[bottoms]


    max_right = rights[np.argmax(rights[:,1])]
    max_left = lefts[np.argmin(lefts[:,1])]
    max_top = tops[np.argmin(tops[:,0])]
    max_bottom = bottoms[np.argmax(bottoms[:,0])]  
    return max_right,max_left,max_top,max_bottom
        
def get_paths(p2,binarized_img,center,contour,entity,r,e):
    pathed_img = binarized_img.copy()    
    points = contour[0]
    max_right,max_left,max_top,max_bottom = getMaxBorders(points)
    p1s = [max_right,max_left,max_right,max_left,max_top,max_bottom]
    paths=[]
    for i in range(6):
        bfs_input = pathed_img.copy()
        bfs_input[p1s[i][1]][p1s[i][0]]=150
        bfs_input[p2[0][1]][p2[0][0]]=150
        pathed_img,path,is_found = BFS(p1s[i],p2[0],pathed_img.copy(),contour[0],entity[0])
        if(is_found):
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
    cv.drawContours(empty, [contour], -1, (255,255,255),  1)
    empty = dilation(empty,np.ones((10,10),np.uint8))
    contour = get_contour(empty)
    if relation:
        relation["contour_cardinality"] = contour
    if entity:
        entity["contour_cardinality"] = contour
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
            entity["self"]=False
            entity["participation"]="partial"
            if len(relation["entities"])==1:
                entity["self"]=True
            if((len(paths)==1 and not entity["self"]) or (entity["self"] and len(paths)==2)):
                entity["participation"]="partial"
            elif((len(paths)==2 and not entity["self"]) or (entity["self"] and len(paths)==4)):
                entity["participation"]="full"

            entity.pop("relations",None)
            rel_paths.extend(paths)
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
            relations[bounding_box_str]["entities"].append(entity.copy())
            relations[bounding_box_str].update({
                "idx":relation["idx"],
                "name":relation["name"],
                "contour":relation["contour"],
                "bounding_box":relation["bounding_box"]
            })

    detect_participation(relations,binarizedImg)
    return relations


def distance_tuble(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
def get_correct_path_point(path,center_relation):
    dist = [distance_tuble(p,center_relation) for p in path]
    return path[np.argmin(dist)]

        
def cardinality(relations,img,binarizedImg):
    count = 0
    img=255-img
    binarizedImg = binarizedImg.astype(np.uint8)
    for relation in relations.values():
        x,y,w,h = relation["bounding_box"]
        rows = [p[0] for p in relation["contour_cardinality"][0]]
        cols = [p[1] for p in relation["contour_cardinality"][0]]
        img[cols,rows]=255
        binarizedImg[cols,rows]=255
        for path in relation["paths"]:
            rows = [p[0] for p in path]
            cols = [p[1] for p in path]
            img[rows,cols]=255 

        c2 = 0
        contour = []
        for point in relation["contour_cardinality"][0]:
            contour.append([point[1],point[0]])
        contour = np.array(contour)
        max_right,max_left,max_top,max_bottom = getMaxBorders(contour)
     
        for entity in relation["entities"]:
            centerX = x + w//2
            centerY = y + h//2
            iterations=1
            if entity["self"]:
                iterations=2
            for i in range(iterations):
                if entity.get("paths") and len(entity["paths"])>i:
                    pathX,pathY = get_correct_path_point(entity["paths"][i],(centerY,centerX))
                else:
                    entity["cardinality"]="N"  
                    entity["uncertain"]=True
                    continue  
                borderPoint = detectDirectionPath((pathX,pathY),(centerY,centerX),w,h,max_right,max_left,max_top,max_bottom,count,c2)
                y_wind = borderPoint[0]
                x_wind = borderPoint[1]
                cardinality_img = img.copy()
                cardinality_img[y_wind][x_wind]=150
                wind_width = w
                wind_height = h
                x_wind = x_wind-int(0.5*w)
                y_wind = y_wind-int(0.5*h)
                if x_wind<0:
                    x_wind=0
                if y_wind<0:
                    y_wind=0
                if x_wind+wind_width>img.shape[1]:
                    wind_width = img.shape[1]-x_wind
                if y_wind+wind_height>img.shape[0]:
                    wind_height = img.shape[0]-y_wind
                
                window = binarizedImg[y_wind:y_wind+wind_height,x_wind:x_wind+wind_width].copy()
                entity["cardinality"]=get_relation_cardinality(window)
                c2 += 1
           
        count+=1
    return relations


def get_relation_cardinality(cardinality_img):
    cardinality_img = 255 - cardinality_img
    contours = cv.findContours(cardinality_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    cardinality_img = 255 - cardinality_img
    for contour in contours:
        x,y,w,h= cv.boundingRect(contour)
        textImage = cardinality_img[y:y+h,x:x+w].copy()
        textImage = cv.copyMakeBorder(textImage, 2, 2, 2, 2,  cv.BORDER_CONSTANT, None, (255,255,255))
        custom_config = r'--oem 3 --psm 6'
        extractedText = pytesseract.image_to_string(textImage,config=custom_config)
        if extractedText == "\x0c":
            extractedText = ""
        else:
            extractedText = extractedText.split('\n')[0]
        
        if "N" in extractedText:
            return "N"
        elif "M" in extractedText:
            return "M"
        elif "1" in extractedText:
            return "1"
    return "N"


def detectDirectionPath (pathPoint,relCenter,relWidth,relHeight,max_right,max_left,max_top,max_bottom,c1,c2):

    horizontal = abs(pathPoint[1] - relCenter[1])
    vertical = abs(pathPoint[0] - relCenter[0])
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


