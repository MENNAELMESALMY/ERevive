from array import array
import numpy as np
import cv2 as cv
import math
from skimage.morphology import dilation
from .path_points import *
from .utility import fillHole
import pytesseract

def check_participation(path,entity,relation,img):
    set_path =set(tuple(x) for x in path)
    entity_contour = entity["contour_participation"][0]
    entity_contour = [[point[0],point[1]] for point in entity_contour]
    set_entity_contour = set(tuple([x[1],x[0]]) for x in list(entity_contour))
    relation_contour = relation["contour_participation"][0]
    relation_contour = [[point[0],point[1]] for point in relation_contour]
    set_relation_contour = set(tuple([x[1],x[0]]) for x in relation_contour)
    direct_path = set_path.difference(set_entity_contour,set_relation_contour)
    direct_path = list(direct_path)
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    if len(direct_path)!=0:
        max_num = min(10,len(direct_path))
        distances = []
        for i in range(0,max_num):
            random_point = direct_path[np.random.randint(0,len(direct_path))]
            closest_point = None
            for direction in directions:
                dis = 1
                while dis<10:
                    if random_point[0]+direction[0]*dis<img.shape[0] and random_point[1]+direction[1]*dis<img.shape[1] and random_point[0]+direction[0]*dis>0\
                         and random_point[1]+direction[1]*dis>0 and img[random_point[0]+direction[0]*dis][random_point[1]+direction[1]*dis]==255:
                        if dis==1:
                            break
                        if closest_point:
                            current_point = [random_point[0]+direction[0]*dis,random_point[1]+direction[1]*dis]
                            if distance_tuble(current_point,random_point)<distance_tuble(random_point,closest_point):
                                closest_point = current_point
                        else:
                            closest_point = [random_point[0]+direction[0]*dis,random_point[1]+direction[1]*dis]
                        break
                    dis+=1
            if closest_point:
                distances.append(distance_tuble(closest_point,random_point))
        if len(distances)>.5*max_num:
            return "full",direct_path
        else:
            return "partial",direct_path

            

    

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
    bfs_input = pathed_img.copy()
    bfs_input[max_right[1]][max_right[0]]=150
    bfs_input[p2[0][1]][p2[0][0]]=150
    pathed_img,path,is_found = BFS(max_right,p2[0],pathed_img.copy(),contour[0],entity[0])
    if(is_found):
        return path
            
    return None



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
    binarizedImg = binarizedImgOrig.copy()
    contour = contourOrig.copy()

    empty = np.zeros(binarizedImg.shape,np.uint8)
    cv.drawContours(empty, [contour], -1, (255,255,255),  1)
    empty = dilation(empty,np.ones((10,10),np.uint8))
    contour = get_contour(empty)

    participation_empty = np.zeros(binarizedImg.shape,np.uint8)
    cv.drawContours(participation_empty, [contour], -1, (255,255,255),  1)
    participation_empty = dilation(participation_empty,np.ones((20,20),np.uint8))
    participation_contour = get_contour(participation_empty)

    if relation:
        relation["contour_cardinality"] = contour
        relation["contour_participation"] = participation_contour
    if entity:
        entity["contour_cardinality"] = contour
        entity["contour_participation"] = participation_contour
    # for points in contour:
    #     for point in points:
    #         if binarizedImg[point[1]][point[0]] == 0:
    #             continue
    #         contour_points.append(list(point))

    # get intersection of contour points and white points in binarizedImg
    contour = contour[0]
    contour = contour[:,[1,0]]
    contour_t = contour.T
    contour_t = list(contour_t)
    contour_t = zip(contour_t[0],contour_t[1])
    contour_t = list(contour_t)
    contour_t = set(contour_t) 
    white_points = np.where(binarizedImg!=0)

    white_points = list(zip(*white_points))
    white_points = np.array(white_points)
    white_points = white_points.T
    white_points = list(white_points)
    white_points = zip(white_points[0],white_points[1])
    white_points = list(white_points)
    white_points = set(white_points)
    
    intersection = contour_t.intersection(white_points)
    intersection = np.array(list(intersection))
    intersection = intersection[:,[1,0]]
    intersection = list(intersection)

    return np.array([intersection])


def detect_participation(relations,edges):
        
    entities_mem ={}
    relations_mem = {}
    
    for relation in relations.values():
        rel_paths=[]
        if relations_mem.get(relation["idx"]) is not None:
            relation["contour"] = relations_mem[relation["idx"]]["contour"].copy()
            relation["contour_participation"] = relations_mem[relation["idx"]]["contour_participation"].copy()
            relation["contour_cardinality"] = relations_mem[relation["idx"]]["contour_cardinality"].copy()
        else:
            relation["contour"] = filter_points(relation["contour"].copy(),edges.copy(),relation)
            relations_mem[relation["idx"]] = {"contour":relation["contour"].copy(),"contour_participation":relation["contour_participation"].copy(),"contour_cardinality":relation["contour_cardinality"].copy()}
        for entity in relation["entities"]:
            if entities_mem.get(entity["idx"]) is not None:
                entity["contour"] = entities_mem[entity["idx"]]["contour"].copy()  
                entity["contour_participation"] = entities_mem[entity["idx"]]["contour_participation"].copy()
                entity["contour_cardinality"] = entities_mem[entity["idx"]]["contour_cardinality"].copy()
            else:
                entity["contour"] = filter_points(entity["contour"].copy(),edges.copy(),entity=entity)
                entities_mem[entity["idx"]] = {"contour":entity["contour"].copy(),"contour_participation":entity["contour_participation"].copy(),"contour_cardinality":entity["contour_cardinality"].copy()}
            entity_point = np.random.randint(0,len(entity["contour"]))
            entity_point = entity["contour"][entity_point]
            paths = []
            direct_paths = []
            path = get_paths(entity_point,edges,relation["bounding_box"],relation["contour"],entity["contour"],relation["idx"],entity["idx"])
            entity["self"]=False
            entity["participation"]="partial"
            direct_path = None
            if(path):
                entity["participation"],direct_path = check_participation(path,entity,relation,edges)
            
                paths.append(path) 
                direct_paths.append(direct_path)
            if len(relation["entities"])==1:
                entity["self"]=True
                if direct_path is not None:
                    selfimg = edges.copy()
                    k=len(direct_path)//2
                    selfimg[direct_path[k][0]][direct_path[k][1]]=0
                    second_path = get_paths(entity_point,selfimg,relation["bounding_box"],relation["contour"],entity["contour"],relation["idx"],entity["idx"])
                    _,second_direct_path = check_participation(second_path,entity,relation,selfimg)
                    direct_paths.append(second_direct_path)
                    if second_path:
                        paths.append(second_path)
                            
            entity.pop("relations",None)
            rel_paths.extend(paths)
            entity["paths"] = direct_paths.copy()
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
            binarizedImg[rows,cols]=255
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
    num = min(len(contours),10)
    contours = sorted(contours, key=cv.contourArea, reverse=True)[:num]
    for idx,contour in enumerate(contours):
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


