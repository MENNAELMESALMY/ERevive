import numpy as np
import cv2 as cv
from numpy.lib.function_base import delete
from skimage.morphology import dilation,closing,opening
from skimage.morphology import skeletonize
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

def show(img):
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def prepare_data(contours,labels):
    print("Preparing data")
    k=0
    #for contour in contours:
    #    print("shape : ",k," label ",labels[k]," bounding box: ",cv.boundingRect(contour))
    #    k+=1
    entities=[
        {   
            "name":"Menna",
            "contour":contours[7],
            "bounding_box":cv.boundingRect(contours[7]),
            "relations":[
                {
                    "contour":contours[4],
                    "bounding_box":cv.boundingRect(contours[4]),
                },
                {
                    "contour":contours[5],
                    "bounding_box":cv.boundingRect(contours[5]),
                }
            ]
        },
        {   
            "name":"Nihal",
            "contour":contours[10],
            "bounding_box":cv.boundingRect(contours[10]),
            "relations":[
                {
                    "contour":contours[5],
                    "bounding_box":cv.boundingRect(contours[5]),
                }
            ]
        },
        {   
            "name":"Nada",
            "contour":contours[2],
            "bounding_box":cv.boundingRect(contours[2]),
            "relations":[
                {
                    "contour":contours[4],
                    "bounding_box":cv.boundingRect(contours[4]),
                }
            ]
        }
    ]
    return entities
def match(path1,path2):
    len_match=0
    for point in path1:
        for point2 in path2:
            if point[0]==point2[0] and point[1]==point2[1]:
                len_match+=1
    return len_match
def filtet_paths(paths):
    ret_paths=[]
    for i in range(0,len(paths)):
        if(paths[i] is None):
            continue
        ret_paths.append(paths[i])
        for j in range(i+1,len(paths)):
            #if(len(paths)==3):
                #print("path1",path)
                #print("path2",path2)
            matches = match(paths[i],paths[j])
            print("matches",matches)
            print("match , len",matches,len(paths[i]),len(paths[j]))
            if (len(paths[i])>len(paths[j])):
                shortest = paths[j]
            else:
                shortest = paths[i]
            if(matches/len(shortest)>0.5):
                if shortest == paths[j]:
                    ret_paths.remove(paths[i])
                    ret_paths.append(shortest)
                print("len before",len(paths))
                paths[j]=None
                
                print("len after",len(paths))
    return ret_paths

    
        
def get_paths(p1,p2,binarized_img,center,contour):
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
    #binarized_img = binarized_img*255
    #binarized_img[center[1]][center[0]] = 150   
    #for point in rights:
    #    binarized_img[point[1]][point[0]] = 150
    max_right = rights[np.argmax(rights[:,0])]
    max_left = lefts[np.argmin(lefts[:,0])]
    
    p1s = [max_right,max_left,max_right,max_left]
    cv.imwrite("binarized_img_right.jpg",binarized_img)
   
    #if p1[0] < center[0]:
    #    p1s = [p1,p1,p1,p1]
    binarized_img = binarized_img*255
    paths=[]
    for i in range(4):

        Bfs_res = run_bfs(pathed_img.copy(),p1s[i],p2[0])
        print("Bfs_res",Bfs_res)
        if Bfs_res:
            pathed_img,path = get_real_path(pathed_img.copy(),p1s[i],p2[0])
            if len(path) > 0:
                path_ret=[]
                binarized_img_test = binarized_img.copy()
                for point in path:    
                    l,j  = point // binarized_img_test.shape[1], point % binarized_img_test.shape[1]
                    binarized_img_test[l][j]=150
                    path_ret.append([l,j])
                paths.append(path_ret)
                global G
                cv.imwrite("pathed"+str(i)+str(G)+".png",binarized_img_test)
                count+=1
    G+=1
    print("p1s",p1s)
    print("paths",count)
    return count==4,paths
def show(img):
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()



def fillHole(img):
    #thresholded image
    #show(img)
    im_th = img
    im_floodfill = im_th.copy()
    h, w = im_th.shape[:2]
    #print(h,w)
    #print(im_th.shape)
    mask = np.zeros((h+2, w+2), np.uint8)
    #show(mask)
    #show(im_floodfill)
    cv.floodFill(im_floodfill, mask, (0, 0), 255)
    #show(im_floodfill)
    im_floodfill_inv = cv.bitwise_not(im_floodfill)
    #show(im_floodfill_inv)
    im_out = im_th | im_floodfill_inv
    smoothed_img = cv.medianBlur(im_out,7)
    #show(smoothed_img)
    return smoothed_img
def get_contour(img):
    chull = fillHole(img)
    cv.imwrite("chull.jpg",chull)
    contours = cv.findContours(chull, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)[0]
    contour = contours[0]
    for c in contours:
        if cv.contourArea(c) > cv.contourArea(contour):
            contour = c
    contour_points=[]
    edged = cv.Canny(chull, 0, 84, apertureSize=5)

    for points in contour:
        point = points[0]
        if edged[point[1]][point[0]] == 0:
            continue
        contour_points.append(list(point))
    contour_points = np.array([contour_points])
    empty = np.zeros(chull.shape,np.uint8)
    cv.drawContours(empty, [contour_points], -1, (255,255,255), 1)
    cv.imwrite("contour_ttest.jpg",empty)
    return  contour_points
def filter_points(contour,binarizedImg):
    contour_points = []
    #draw contours
    print("contour",contour)
    empty = np.zeros(binarizedImg.shape,np.uint8)
    cv.drawContours(empty, [contour], -1, (255,255,255), 1)
    empty = dilation(empty,np.ones((10,10),np.uint8))
    cv.imwrite("empty.jpg",empty)
    contour = get_contour(empty)
  
    binarizedImg = binarizedImg*255
    for points in contour:
        for point in points:
            if binarizedImg[point[1]][point[0]] == 0:
                continue
            binarizedImg[point[1]][point[0]] = 150
            contour_points.append(list(point))
    cv.imwrite("binarizedddd_img.jpg",binarizedImg)
  
    return np.array([contour_points])
def detect_participation(relations,binarizedImg):
    #loop on each relation
    #loop on each entity
    #get type of participation between the current entitiy and relation
    #define 2 points one on for the relation and the other on the entity
    #get all paths between the 2 points
    binarized_img = 255-binarizedImg
    binarized_img = binarized_img.astype(np.uint8)
    binarized_img = dilation(binarized_img,np.ones((3,3)))
    edges = skeletonize(binarized_img//255)**1
    print(edges)
    #edges = cv.Canny(binarized_img, 0, 150, apertureSize=7)
    #edges = edges//255
    #sobelxy = cv.Sobel(src=binarized_img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5) # Combined X and Y Sobel Edge Detection
    #edges = sobelxy//255
    #edges  = closing(edges,np.ones((1,1)))
    cv.imwrite("edges.jpg",edges*255)
    r=0
    e=0
    for relation in relations.values():
        is_visited={}
        for entity in relation["entities"]:
            #get type of participation between the current entitiy and relation
            #define 2 points one on for the relation and the other on the entity
            #get all paths between the 2 points
            if ( not is_visited.get(relation["bounding_box"])):
                relation["contour"] = filter_points(relation["contour"].copy(),edges.copy())
            else:
                is_visited[relation["bounding_box"]] = True
            if ( not is_visited.get(entity["bounding_box"])):
                entity["contour"] = filter_points(entity["contour"].copy(),edges.copy())
            else:
                is_visited[entity["bounding_box"]] = True
            relation_point = np.random.randint(0,len(relation["contour"]))
            relation_point = relation["contour"][relation_point]
            entity_point = np.random.randint(0,len(entity["contour"]))
            entity_point = entity["contour"][entity_point]
            #get all paths between the 2 points
            full_partial,paths = get_paths(relation_point,entity_point,edges,relation["bounding_box"],relation["contour"])
            paths = filtet_paths(paths)
            if(len(paths)==2):
                entity["participation"]="partial"
            elif(len(paths)==4):
                entity["participation"]="full"

            entity.pop("relations",None)

            p=0
            for path in paths:
                edges_test = (edges.copy())*255
                for point in path:   
                    edges_test[point[0]][point[1]]=150
                cv.imwrite("pathed_final"+str(r)+str(e)+str(p)+".png",edges_test)
                p+=1
            e+=1
        r+=1
            
def get_relations(binarizedImg,contours,labels):
    entities = prepare_data(contours,labels)
    relations = {}
    # get unique relations
    # loop on each relation and get an array of its entities
    for entity in entities:
        for relation in entity["relations"]:
            bounding_box_str = str(relation["bounding_box"])
            if relations.get(bounding_box_str) is None:
                relations[bounding_box_str] = {
                    "entities":[]
                }
            relations[bounding_box_str]["entities"].append(entity)
            relations[bounding_box_str].update({
                "contour":relation["contour"],
                "bounding_box":relation["bounding_box"]
            })
    detect_participation(relations,binarizedImg)
    #print(relations)


