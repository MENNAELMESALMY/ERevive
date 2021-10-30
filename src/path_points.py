from collections import deque
import cv2 as cv
directions=[[1,0],[0,1],[0,-1],[-1,0],[-1,-1],[1,1],[-1,1],[1,-1]]
def BFS(start,end,img,index1,index2):
    src = [start[1],start[0]]
    dst=[end[1],end[0]]
    q = deque()
    q.append([src])
    path=[]
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
    k=0
    if not is_found:
        path=[]
    else:
        k=len(path)//2
        i,j = path[k]
        img[int(i)][int(j)] = 0
        cv.imwrite("cutted"+str(index1)+"_"+str(index2)+".png",img)
    return img,path,is_found


