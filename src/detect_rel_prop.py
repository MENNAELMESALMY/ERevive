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
    print("center",center)
    print("rights: ",rights)
    print("lefts: ",lefts)
    print("tops: ",tops)
    print("bottoms: ",bottoms)

    max_right = rights[np.argmax(rights[:,1])]
    max_left = lefts[np.argmin(lefts[:,1])]
    max_top = tops[np.argmin(tops[:,0])]
    max_bottom = bottoms[np.argmax(bottoms[:,0])]  
    print("min_x: ",max_left,"max_x: ",max_right,"min_y: ",max_top,"max_y: ",max_bottom)
    return max_right,max_left,max_top,max_bottom
        
def get_paths(p2,binarized_img,center,contour,entity,r,e):
    pathed_img = binarized_img.copy()    
    points = contour[0]
    max_right,max_left,max_top,max_bottom = getMaxBorders(points)
    p1s = [max_right,max_left,max_right,max_left,max_top,max_bottom]
    paths=[]
    p=0
    for i in range(6):
        test_img = pathed_img.copy()
        test_img[max_right[1]][max_right[0]] = 150
        test_img[max_left[1]][max_left[0]] = 150
        test_img[max_top[1]][max_top[0]] = 150
        test_img[max_bottom[1]][max_bottom[0]] = 150
        print("r: ",r," max_right: ",max_right[::-1]," max_left: ",max_left[::-1]," max_top: ",max_top[::-1]," max_bottom: ",max_bottom[::-1])
        cv.imwrite("max_"+str(e)+"_"+str(r)+"_"+str(i)+".png",test_img)

    for i in range(6):
        bfs_input = pathed_img.copy()
        bfs_input[p1s[i][1]][p1s[i][0]]=150
        bfs_input[p2[0][1]][p2[0][0]]=150
        cv.imwrite("bfs_input_"+str(e)+"_"+str(r)+"_"+str(i)+".png",bfs_input)
        pathed_img,path,is_found = BFS(p1s[i],p2[0],pathed_img.copy(),contour[0],entity[0],r,e,i)
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
    if entity and entity["idx"]==12:
        cv.imwrite("before_dilation.png",empty)
    empty = dilation(empty,np.ones((10,10),np.uint8))
    if entity and entity["idx"]==12:
        cv.imwrite("after_dilation.png",empty)
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
        #contour = np.zeros(relation["contour_cardinality"][0].shape,np.uint8)
        contour = []
        for point in relation["contour_cardinality"][0]:
            contour.append([point[1],point[0]])
        contour = np.array(contour)
        max_right,max_left,max_top,max_bottom = getMaxBorders(contour)
     
        for entity in relation["entities"]:
            centerX = x + w//2
            centerY = y + h//2
            iterations=1
            print("entity name",entity["name"]," participation: ",entity["participation"]," length: ",len(entity["paths"]))
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
                
                cv.imwrite("card"+ str(count) + str(c2) + ".png",cardinality_img)
                window = img[y_wind:y_wind+wind_height,x_wind:x_wind+wind_width].copy()
                #x_card,y_card,w_card,h_card = cardinalitiesContours(window,count,c2)
                #card_img = img.copy()
                #card_img[y_card:y_card+h_card,x_card:x_card+w_card]=150
                cv.imwrite("card_img"+ str(count) + str(c2) + ".png",window)
                
                entity["cardinality"]=get_relation_cardinality(window,count,c2)
                c2 += 1
           
        count+=1
    return relations

def distance(p1,p2):
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

def between(p1,p2,p3):
    return math.isclose(distance(p1,p3)+distance(p2,p3),distance(p1,p2),rel_tol=0.5)

def get_relation_cardinality(cardinality_img,count,c2):
    cardinality_img = 255 - cardinality_img
    contours = cv.findContours(cardinality_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    cardinalities_text=[]
    c3 = 0
    cardinality_img = 255 - cardinality_img
    for contour in contours:
        x,y,w,h= cv.boundingRect(contour)
        textImage = cardinality_img[y:y+h,x:x+w].copy()
        textImage = cv.copyMakeBorder(textImage, 2, 2, 2, 2,  cv.BORDER_CONSTANT, None, (255,255,255))
        cv.imwrite("final_card" + str(count) + "_" + str(c2) + "_" + str(c3) + ".png",textImage)
        c3 += 1
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


def detectDirectionPath (pathPoint,relCenter,relWidth,relHeight,max_right,max_left,max_top,max_bottom,c1,c2):
    print("pathPoint",pathPoint)
    print("relCenter",relCenter)
    print("relWidth",relWidth,"  relHeight",relHeight)

    horizontal = abs(pathPoint[1] - relCenter[1])
    vertical = abs(pathPoint[0] - relCenter[0])
    
    print("c1: ",c1," c2: ",c2)
    print("horizontal",horizontal)
    print("vertical",vertical)
    print("relWidth",relWidth)
    print("relHeight",relHeight)
    print("max_right",max_right)
    print("max_left",max_left)
    print("max_top",max_top)
    print("max_bottom",max_bottom)

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


                # y_wind = border_point[1]
                # x_wind = border_point[0]
                # cardinality_img = img.copy()
                # cardinality_img[y_wind][x_wind]=150
                # wind_width = w
                # wind_height = h
                # x_wind = x_wind-int(0.5*w)
                # y_wind = y_wind-int(0.5*h)
                # if x_wind<0:
                #     x_wind=0
                # if y_wind<0:
                #     y_wind=0
                # if x_wind+wind_width>img.shape[1]:
                #     wind_width = img.shape[1]-x_wind
                # if y_wind+wind_height>img.shape[0]:
                #     wind_height = img.shape[0]-y_wind
                # card_img = img.copy()
                # card_img[y_wind:y_wind+wind_height,x_wind:x_wind+wind_width]=150
                # cv.imwrite("card_img"+ str(count) + str(c2) + ".png",card_img)