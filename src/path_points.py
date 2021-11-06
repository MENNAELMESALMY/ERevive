from collections import deque
import cv2 as cv
import numpy as np
from utility import fillHole
from skimage.morphology import opening,erosion,dilation
def enhance_contour(img,contour,kernel=1):
    empty_img = np.zeros(img.shape,np.uint8)
    cv.drawContours(empty_img, [contour], -1, 255,  cv.FILLED)
    empty_img = opening(empty_img,np.ones((kernel,kernel),np.uint8))
    actual_contour = np.where(empty_img==255)
    actual_contour = list(actual_contour)
    actual_contour.reverse()
    contour = list(zip(*actual_contour))
    return contour
directions=[[1,0],[0,1],[0,-1],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
def BFS(start,end,img,relation,entity):
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
    if not is_found:
        path=[]
        points_inbetween=[]
    else:
        relation = enhance_contour(img,relation)
        entity = enhance_contour(img,entity)
        r =set(tuple([x[1],x[0]]) for x in list(relation))
        e =set(tuple([x[1],x[0]]) for x in list(entity))
        points_in_contours = r.union(e)
        actual_path = set(tuple(x) for x in list(path))
        points_inbetween = actual_path.difference(points_in_contours)
        points_inbetween = list(points_inbetween)
        k=len(points_inbetween)//2
        i,j = points_inbetween[k]
        img[int(i)][int(j)] = 0
    return img,points_inbetween,is_found


