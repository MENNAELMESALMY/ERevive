import numpy as np
import cv2 as cv
import math
from skimage.morphology import dilation
from path_points import *
from utility import fillHole
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

    
        
def get_paths(p2,binarized_img,center,contour,entity,r,e):
    pathed_img = binarized_img.copy()    
    points = contour[0]
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
    for relation in relations.values():
        x,y,w,h = relation["bounding_box"]
        rows = [p[0] for p in relation["contour_cardinality"][0]]
        cols = [p[1] for p in relation["contour_cardinality"][0]]
        img[cols,rows]=255
        all_points=[]
        for path in relation["paths"]:
            rows = [p[0] for p in path]
            cols = [p[1] for p in path]
            all_points.extend(path)
            img[rows,cols]=255 
        width = 3*w
        height = 3*h
        x = x-w
        y = y-h
        if x<0:
            x=0
        if y<0:
            y=0
        if x+width>img.shape[1]:
            width = img.shape[1]-x
        if y+height>img.shape[0]:
            height = img.shape[0]-y
        cardinality_img = img.copy()
        #cardinality_img = img[y:y+height,x:x+width].copy()
        #relation["cardinality"] = get_relation_cardinality(cardinality_img,relation)
        cv.imwrite("card_rel_path"+ str(count) + ".png",cardinality_img)
        count+=1

def distance(p1,p2):
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

def between(p1,p2,p3):
    return math.isclose(distance(p1,p3)+distance(p2,p3),distance(p1,p2),rel_tol=0.5)

def get_relation_cardinality(cardinality_img,relation):
    cv.imwrite("card_rel_path.png",cardinality_img)
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
    cardinalities_text = classify_cardinalities(cardinalities)
    for i in range(number_of_cards):
        x1,y1,w1,h1= cv.boundingRect(cardinalities[i])
        center_cardinality = (x1+w1//2,y1+h1//2)
        for entity in relation["entities"]:
            x2,y2,w2,h2= cv.boundingRect(entity)
            center_entity = (x2+w2//2,y2+h2//2)
            if between(center_relation,center_entity,center_cardinality):
                entity["cardinality"]=cardinalities_text[i]
                break
    
            
def classify_cardinalities(cardinalities):
    return ["N","1"]



#   erased_points=[]
#         black_before = False
#         black_after = False
#         white = False
#         pattern = []
#         erased_rows = [p[0] for p in erased_points]
#         erased_cols = [p[1] for p in erased_points]
#         img[erased_rows,erased_cols]=255 
# for j in range(y,y+height):
        #     for i in range(x,x+width-1):
        
        #         if img[j][i]==0 and black_after==False:
        #             black_before = True
        #             pattern.append([j,i])
        #         if img[j][i]==255 and img[j][i+1]==0 and black_before :
        #             white = True
        #         if img[j][i]==0 and white and black_before :
        #             black_after = True
        #             pattern.append([j,i])
        #         if black_before and white and black_after:
        #             erased_points.extend(pattern)
        #             pattern=[]
        #             black_before = False
        #             black_after = False
        #             white = False
        # black_before = False
        # black_after = False
        # white = False
        # pattern = []
        # for i in range(x,x+width):
        #     for j in range(y,y+height-1):
        
        #         if img[j][i]==0 and black_after==False:
        #             black_before = True
        #             pattern.append([j,i])
        #         if img[j][i]==255 and img[j+1][i]==0 and black_before :
        #             white = True
        #         if img[j][i]==0 and white and black_before :
        #             black_after = True
        #             pattern.append([j,i])
        #         if black_before and white and black_after:
        #             erased_points.extend(pattern)
        #             pattern=[]
        #             black_before = False
        #             black_after = False
        #             white = False





