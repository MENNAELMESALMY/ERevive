import numpy as np
import cv2 as cv
from numpy.lib.function_base import delete
from skimage.morphology import dilation,closing,opening
from skimage.morphology import skeletonize
from skimage import io
import math
G=0
from path_points import *
# entities=[
#     {
#         "entitiy":[],
#         "relations":[{
#             "contour":[]
#         }]
#     },
#    {
#         "entitiy":[],
#         "relations":[{
#             "contour":[]
#         }]
#     },
# ]
# unique relations
# loop on each relation and get an array of its entities
# path from the relation to the entities

# def show(img):
#     cv.imshow('image',img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

# def prepare_data(contours,labels):
#     print("Preparing data")
#     k=0
#     #for contour in contours:
#     #    print("shape : ",k," label ",labels[k]," bounding box: ",cv.boundingRect(contour))
#     #    k+=1
#     entities=[
#         {   
#             "name":"Menna",
#             "contour":contours[8],
#             "bounding_box":cv.boundingRect(contours[8]),
#             "relations":[
#                 {
#                     "contour":contours[5],
#                     "bounding_box":cv.boundingRect(contours[5]),
#                 },
#                 {
#                     "contour":contours[6],
#                     "bounding_box":cv.boundingRect(contours[6]),
#                 }
#             ]
#         },
#         {   
#             "name":"Nihal",
#             "contour":contours[11],
#             "bounding_box":cv.boundingRect(contours[11]),
#             "relations":[
#                 {
#                     "contour":contours[6],
#                     "bounding_box":cv.boundingRect(contours[6]),
#                 }
#             ]
#         },
#         {   
#             "name":"Nada",
#             "contour":contours[2],
#             "bounding_box":cv.boundingRect(contours[2]),
#             "relations":[
#                 {
#                     "contour":contours[5],
#                     "bounding_box":cv.boundingRect(contours[5]),
#                 }
#             ]
#         }
#     ]
#     return entities

def check_direct_path(path,entities,orig_entity,img,relations,orig_relation):
    set_path =set(tuple(x) for x in path)
    for entity in entities:
        if entity["idx"]==orig_entity["idx"]:
            continue
        contour = entity["contour"][0]
        contour = [[point[0],point[1]] for point in contour]
        #print("len of contour: ",len(contour))
        set_contour = set(tuple(x) for x in list(contour))
        #print("len intersection: ",len(set_path.intersection(set_contour)))
        if len(set_path.intersection(set_contour))!=0:
            return False
    for relation in relations:
        if relation["idx"]==orig_relation["idx"]:
            continue
        contour = relation["contour"][0]
        print("length:",len(contour))
        contour = [[point[0],point[1]] for point in contour]
        #print("len of contour: ",len(contour))
        set_contour = set(tuple(x) for x in contour)
        if orig_relation["idx"]==7:
            print("len relation intersection: ",len(set_path.intersection(set_contour)))
        if len(set_path.intersection(set_contour))!=0:
            return False
    return True

def filter_paths(paths,entities,entity,img,relations,relation):
    
    #this loop is just for test
    k=0
    for path in paths:
        k+=1
        binarized_img_test = img.copy()
        for point in path:    
            l,j  = point
            binarized_img_test[l][j]=150
        cv.imwrite("before_path_"+str(entity["idx"])+"_"+str(relation["idx"])+"_"+str(k)+".png",binarized_img_test)
   
    ret_paths=[]
    paths = sorted(paths, key=lambda x: len(x))
    print("len1: ",len(paths))
    for i in range(0,len(paths)):
        if i>=len(paths):
            continue
        ret_paths.append(paths[i])
        
        for j in range(i+1,len(paths)):
            if j>=len(paths):
                continue
            path1 = set(tuple(x) for x in paths[i])
            path2 = set(tuple(x) for x in paths[j])
            intersection = path1.intersection(path2)
            shortest = list(path1)
        
            if len(intersection)/len(shortest)>=0.2:
                paths.remove(paths[j])
    print("len2: ",len(ret_paths))
    k=0
    for path in ret_paths:
        k+=1
        binarized_img_test = img.copy()
        for point in path:    
            l,j  = point
            binarized_img_test[l][j]=150
        cv.imwrite("between_path_"+str(entity["idx"])+"_"+str(relation["idx"])+"_"+str(k)+".png",binarized_img_test)
   
    for path in ret_paths:
        if(not check_direct_path(path,entities,entity,img,relations,relation)):
            ret_paths.remove(path)
    print("len3: ",len(ret_paths))
    binarized_img_test = img.copy()
    #this loop is just for test
    k=0
    for path in ret_paths:
        k+=1
        binarized_img_test = img.copy()
        for point in path:    
            l,j  = point
            binarized_img_test[l][j]=150
        cv.imwrite("final_path_"+str(entity["idx"])+"_"+str(relation["idx"])+"_"+str(k)+".png",binarized_img_test)
    return ret_paths

    
        
def get_paths(p1,p2,binarized_img,center,contour,entity):
    #get all paths between the 2 points
    pathed_img = binarized_img.copy()

    count=0
    
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

    #binarized_img = binarized_img*255
    #binarized_img[center[1]][center[0]] = 150   
    #for point in rights:
    #    binarized_img[point[1]][point[0]] = 150
    max_right = rights[np.argmax(rights[:,0])]
    max_left = lefts[np.argmin(lefts[:,0])]
    max_top = tops[np.argmax(tops[0,:])]
    max_bottom = bottoms[np.argmin(bottoms[0,:])]


    p1s = [max_right,max_left,max_right,max_left,max_top,max_bottom]
    cv.imwrite("binarized_img_right.jpg",binarized_img)
   
    #if p1[0] < center[0]:
    #    p1s = [p1,p1,p1,p1]
    #binarized_img = binarized_img*255
    paths=[]
    for i in range(6):
        global G
        pathed_img,path,is_found = BFS(p1s[i],p2[0],pathed_img.copy(),i,G,contour[0],entity[0])
        print("Bfs_res",is_found)
        if not is_found:
            break
        binarized_img_test = binarized_img.copy()
        #this loop is just for test
        for point in path:    
            l,j  = point
            binarized_img_test[l][j]=150
        paths.append(path)
        cv.imwrite("pathed"+str(i)+str(G)+".png",binarized_img_test)
        count+=1
    G+=1
   
    return count==4,paths
def show(img):
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()



def fillHole(img):
    im_th = img
    im_floodfill = im_th.copy()
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
    cv.floodFill(im_floodfill, mask, (0, 0), 255)
    im_floodfill_inv = cv.bitwise_not(im_floodfill)
    im_out = im_th | im_floodfill_inv
    smoothed_img = cv.medianBlur(im_out,7)
    return smoothed_img
def get_contour(img):
    cv.imwrite("chull_input.jpg",img)
    chull = fillHole(img)
    cv.imwrite("chull.jpg",chull)
    #cv.imwrite("empty_in"+str(A)+".jpeg",img)
    contours = cv.findContours(chull, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    contour = contours[0]
    for c in contours:
        if cv.contourArea(c) > cv.contourArea(contour):
            contour = c
    empty = np.zeros(img.shape,np.uint8)
    cv.drawContours(empty, [contour], -1, 255,  cv.FILLED)
    cv.imwrite("contour_ttest.jpg",empty)
    ii = np.where(empty==255)
    ii = list(ii)
    ii.reverse()
    contour = list(zip(*ii))
    return  np.array([contour])
A=0
def filter_points(contourOrig,binarizedImgOrig,relation=None,entity=None):
    contour_points = []
    binarizedImg = binarizedImgOrig.copy()
    contour = contourOrig.copy()

    global A
    empty = np.zeros(binarizedImg.shape,np.uint8)
    cv.drawContours(empty, [contour], -1, (255,255,255), 1)
    #cv.imwrite("empty_bef"+str(A)+".jpeg",empty)
    empty = dilation(empty,np.ones((10,10),np.uint8))
    A+=1
    #print("contour_bef",contour)
    contour = get_contour(empty)
    if relation:
        relation["contour_cardinality"] = contour
    #print("contour_aft",contour)
    empty = np.zeros(binarizedImg.shape,np.uint8)
    cv.drawContours(empty, contour, -1, (255,255,255), 1)
    #cv.imwrite("empty_Aft"+str(A)+".jpeg",empty)
    binarizedImg = binarizedImg*255
    for points in contour:
        for point in points:
            if binarizedImg[point[1]][point[0]] == 0:
                continue
            binarizedImg[point[1]][point[0]] = 150
            contour_points.append(list(point))
    if relation and relation["idx"]==7:
        cv.imwrite("binarizedddd_img.jpg",binarizedImg)
    
    return np.array([contour_points])
def detect_participation(relations,edges):
    #loop on each relation
    #loop on each entity
    #get type of participation between the current entitiy and relation
    #define 2 points one on for the relation and the other on the entity
    #get all paths between the 2 points
    #binarized_img = 255-binarizedImg
    #binarized_img = binarized_img.astype(np.uint8)
    #binarized_img = dilation(binarized_img,np.ones((3,3)))
    #edges = skeletonize(binarized_img//255)**1
    #edges = cv.Canny(binarized_img, 0, 150, apertureSize=7)
    #edges = edges//255
    #sobelxy = cv.Sobel(src=binarized_img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5) # Combined X and Y Sobel Edge Detection
    #edges = sobelxy//255
    #edges  = closing(edges,np.ones((1,1)))
    cv.imwrite("edges.jpg",edges*255)
    r=0
    e=0
    for relation in relations.values():
        for entity in relation["entities"]:
            #get type of participation between the current entitiy and relation
            #define 2 points one on for the relation and the other on the entity
            #get all paths between the 2 points
            relation["contour"] = filter_points(relation["contour"].copy(),edges.copy(),relation)
            #if ( not is_visited.get(entity["bounding_box"])):
            entity["contour"] = filter_points(entity["contour"].copy(),edges.copy(),entity=entity)
            #else:
    for relation in relations.values():
        rel_paths=[]
        for entity in relation["entities"]:
            #get type of participation between the current entitiy and relation
            #define 2 points one on for the relation and the other on the entity
            #get all paths between the 2 points
            #relation["contour"] = filter_points(relation["contour"].copy(),edges.copy(),relation)
            #if ( not is_visited.get(entity["bounding_box"])):
            #entity["contour"] = filter_points(entity["contour"].copy(),edges.copy(),entity=entity)
            #else:
        
            #    is_visited[entity["bounding_box"]] = True
            relation_point = np.random.randint(0,len(relation["contour"]))
            relation_point = relation["contour"][relation_point]
            entity_point = np.random.randint(0,len(entity["contour"]))
            entity_point = entity["contour"][entity_point]
            #get all paths between the 2 points
            #print("get paths contour: ",relation["contour"])
            full_partial,paths = get_paths(relation_point,entity_point,edges,relation["bounding_box"],relation["contour"],entity["contour"])
            print("relation contour: ",len(relation["contour"][0]))
            paths = filter_paths(paths,relation["entities"],entity,edges,relations.values(),relation)
            if(len(paths)==1):
                entity["participation"]="partial"
            elif(len(paths)==2):
                entity["participation"]="full"

            entity.pop("relations",None)
            print("Entity: ",entity.get("idx",None)," Relation: ",relation.get("idx",None)," Participation: ",entity["participation"])
            p=0
            for path in paths:
                rel_paths.append(path)
                edges_test = (edges.copy())*255
                for point in path:   
                    edges_test[point[0]][point[1]]=150
                cv.imwrite("pathed_final"+str(r)+str(e)+str(p)+".png",edges_test)
                p+=1
            e+=1
        relation["paths"] = rel_paths.copy()
        r+=1
            
def get_relations(binarizedImg,entities):
    relations = {}
    # get unique relations
    # loop on each relation and get an array of its entities
    for entity in entities:
        print("entity",entity)
        for relation in entity["relations"]:
            bounding_box_str = str(relation["bounding_box"])
            if relations.get(bounding_box_str) is None:
                relations[bounding_box_str] = {
                    "entities":[]
                }
            relations[bounding_box_str]["entities"].append(entity)
            relations[bounding_box_str].update({
                "idx":relation["idx"],
                "contour":relation["contour"],
                "bounding_box":relation["bounding_box"]
            })

    detect_participation(relations,binarizedImg)
    return relations


def cardinality(relations,img):
    #erase relation contour
    #getting the rect bounding the relation
    #erase relation
    #create window with 3*w , 3*h of relation then erase the paths
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
        erased_points=[]
        black_before = False
        black_after = False
        white = False
        pattern = []
        for i in range(y,y+height):
            for j in range(x,x+width-1):
        
                if img[j][i]==0 and black_after==False:
                    black_before = True
                    pattern.append([j,i])
                if img[j][i]==255 and img[j][i+1]==0 and black_before :
                    white = True
                if img[j][i]==0 and white and black_before :
                    black_after = True
                    pattern.append([j,i])
                if black_before and white and black_after:
                    erased_points.extend(pattern)
                    pattern=[]
                    black_before = False
                    black_after = False
                    white = False
        black_before = False
        black_after = False
        white = False
        pattern = []
        for i in range(x,x+width):
            for j in range(y,y+height-1):
        
                if img[j][i]==0 and black_after==False:
                    black_before = True
                    pattern.append([j,i])
                if img[j][i]==255 and img[j+1][i]==0 and black_before :
                    white = True
                if img[j][i]==0 and white and black_before :
                    black_after = True
                    pattern.append([j,i])
                if black_before and white and black_after:
                    erased_points.extend(pattern)
                    pattern=[]
                    black_before = False
                    black_after = False
                    white = False
        erased_rows = [p[0] for p in erased_points]
        erased_cols = [p[1] for p in erased_points]
        img[erased_rows,erased_cols]=255 
        cardinality_img = img[y:y+height,x:x+width].copy()
        relation["cardinality"] = get_relation_cardinality(cardinality_img,relation)
    cv.imwrite("card_rel_path.png",img)

def distance(p1,p2):
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

def between(p1,p2,p3):
    #p1 is entity , p2 is relation , p3 is cardinality
    #if distance between entity+cardinality , relation+cardinality is close to entity+relation then the cardinality falls between them
    return math.isclose(distance(p1,p3)+distance(p2,p3),distance(p1,p2),rel_tol=0.5)

def get_relation_cardinality(cardinality_img,relation):
    # Get contours of cardinality_img
    # If 2 then these are the 2 cardinalities else get the biggest 2 contours
    # Classify each cardinality
    # get center of each entity and center of each cardinality then compare the rows and cols ranges
    # assign the correct cardinality for each entity
    contours = cv.findContours(cardinality_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    cardinalities=[]
    cardinalities_text=[]
    number_of_cards = len(relation["entities"])
    if len(contours<number_of_cards):
        print("Error in detecting cardinalities")
        return
    elif len(contours==number_of_cards):
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










