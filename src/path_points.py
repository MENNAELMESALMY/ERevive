from collections import deque
import cv2 as cv
import numpy as np
from utility import fillHole
from skimage.morphology import opening,erosion,dilation
def enhance_contour(img,contour,r,e,i,type,kernel=10):
    test= img.copy()
    for point in contour:
        test[point[1]][point[0]]=150
    cv.imwrite(type+"_"+str(e)+"_"+str(r)+"_"+str(i)+".png",test)
    empty_img = np.zeros(img.shape,np.uint8)
    cv.drawContours(empty_img, [contour], -1, 255,  cv.FILLED)
    empty_img = dilation(empty_img,np.ones((kernel,kernel),np.uint8))
    actual_contour = np.where(empty_img==255)
    actual_contour = list(actual_contour)
    actual_contour.reverse()
    contour = list(zip(*actual_contour))
    return contour

def reconstructEntityContour(entity,img):
    #entity points are reserved 0 is column , 1 is row
    min_x = np.min(entity[:,0])
    max_x = np.max(entity[:,0])
    min_y = np.min(entity[:,1])
    max_y = np.max(entity[:,1])
    padding = 2
    top_left = (min_y-padding,min_x-2*padding)
    bottom_right = (max_y+padding,max_x+2*padding)
    #draw rectangle
    image = np.zeros(img.shape,np.uint8)
    image = cv.rectangle(image, top_left, bottom_right, (255,255,255), 1)
    actual_contour = np.where(image==255)
    actual_contour = list(actual_contour)
    contour = list(zip(*actual_contour))
    return  contour

    
directions=[[1,0],[0,1],[0,-1],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
def BFS(start,end,img,relation,entity,r_ind,e_ind,p_ind):
    src = [start[1],start[0]]
    dst=[end[1],end[0]]
    q = deque()
    q.append([src])
    path=[]
    points_inbetween = []
    visited={}
    visited[str(src)]=True
    is_found = False
    while(q):
        path = q.popleft()
        node = path[-1]
        if node[0] == dst[0] and node[1] == dst[1]:
            is_found=True
            break
        for direction in directions:
            neighbour = [node[0]+direction[0],node[1]+direction[1]]
            if (not(neighbour[0]>=0 and neighbour[0]<img.shape[0] and neighbour[1]>=0 and neighbour[1]<img.shape[1])):
                continue
            if img[neighbour[0]][neighbour[1]]==255 and (visited.get(str(neighbour)) ==False or visited.get(str(neighbour)) is None):
                npath = list(path)
                npath.append(neighbour)
                q.append(npath)
                visited[str(neighbour)]=True
    test_img = np.zeros(img.shape)
    cv.imwrite("cutted_test_"+str(e_ind)+"_"+str(r_ind)+"_"+str(p_ind)+".png",test_img)
    if not is_found:
        path=[]
        points_inbetween=[]
    else:
        #relation = enhance_contour(img,relation,e_ind,r_ind,p_ind,"relation")
        #entity = enhance_contour(img,entity,e_ind,r_ind,p_ind,"entity")
        rel_img = img.copy()
        for point in relation:
            rel_img[point[1]][point[0]]=150
        cv.imwrite("relationn"+str(e_ind)+"_"+str(r_ind)+"_"+str(p_ind)+".png",rel_img)
        ent_img = img.copy()
        for point in entity:
            ent_img[point[1]][point[0]]=150
        cv.imwrite("entityy"+str(e_ind)+"_"+str(r_ind)+"_"+str(p_ind)+".png",ent_img)
        r =set(tuple([x[1],x[0]]) for x in list(relation))
        e =set(tuple([x[1],x[0]]) for x in list(entity))
        points_in_contours = r.union(e)
        actual_path = set(tuple(x) for x in list(path))
        points_inbetween = actual_path.difference(points_in_contours)
        points_inbetween = list(points_inbetween)
        k=len(points_inbetween)//2
        i,j = points_inbetween[k]
        img[int(i)][int(j)] = 0
        test_img = img.copy()
        cv.imwrite("cutted_"+str(e_ind)+"_"+str(r_ind)+"_"+str(p_ind)+".png",test_img)
    return img,points_inbetween,is_found


