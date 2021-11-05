import cv2
from numpy.core.defchararray import count
from skimage.morphology import skeletonize
import numpy as np
from math import sqrt
from removeLines import *
neighbors =[
    (0,1),
    (1,0),
    (1,1),
    (0,-1),
    (-1,0),
    (-1,-1),
    (1,-1),
    (-1,1)
]

def removeText():
    pass
   
def findPixel(box,img,colored_im,idx):
    x,y,w,h=box
    hImg,wImg = img.shape
    for i in range(y+2,min(y+h,hImg)):
        for j in range(x+2,min(x+w,wImg)):
            #b,g,r = colored_im[i,j]
            if(img[i,j]==0 and sum(colored_im[i,j]) == idx):
                return i,j
    print("cannot find any starting point")
    return 0,0

def getDirection(x1,y1,x2,y2):
    '''
    right = 0
    downright = 1
    down = 2
    downleft = 3
    left = 4 0
    upleft = 5 1
    up = 6 2
    upright = 7 3
    '''
## abs(dir1-dir2)%3 7-0%3 ==1  6-0 ==0 

    if(abs(y2-y1)<=4):
        return 0 if x2>x1 else 4
    if(abs(x2-x1)<=4):
        return 2 if y2>y1 else 6

    if(y2>y1):
        return 1 if x2>x1 else 3
    else:
        return 7 if x2>x1 else 5


def BFS(y,x,colored_contours,skb,idx,colored_contours_labelled,foundVis):
    q = []
    found =[]
    startX,startY = x,y
    hImg,wImg = skb.shape
    q.append((y,x))
    deadend =[]

    while len(q):
        y,x = q.pop(0)
        skb[y,x]=254
        hasFound = False
        countVis,countWhite=0,0
        for nY,nX in neighbors:
            coorX,coorY = x+nX,y+nY
            if coorX >= wImg or coorX<0 or coorY>=hImg or coorY <0:
                continue
            if(skb[coorY,coorX] == 254):
                countVis +=1
                continue
            cur = sum(colored_contours[coorY,coorX])
            if(cur != 255*3 and cur != idx):
                foundVis[int(cur)] = 1
                found.append(int(cur))
                hasFound = True
                break
            if(skb[coorY,coorX]==0):
                q.append((coorY,coorX))
            else:
                countWhite +=1

        if(not hasFound and countVis == 1 and countWhite == 7 and sum(colored_contours[y,x]) == 255*3.0 ):
            #print(sum(colored_contours[y,x]))
            deadend.append((y,x,getDirection(startX,startY,x,y),idx))
            colored_contours_labelled[y,x]=(0,255,0)
    return list(set(deadend)),list(set(found))

def connectDeadEndsToShapes(deadEnds,colored_im,skx):
    for y,x,direction,idx in deadEnds:
        hImg,wImg,_ = colored_im.shape
        m = 5
        xL = max(0,x-m)
        xR = min(wImg,x+m+1)
        yUp = max(0,y-m)
        yDown = min(hImg,y+m+1)
        window = colored_im[yUp:yDown,xL:xR]
        h,w,_ = window.shape
        dirs = list(range(0,8))

        for i in range(h):
            breaked = False
            for j in range(w):
                if(sum(window[i,j]) != 255*3):
                    shapeDir = getDirection(x,y,j+xL,i+yUp)
                    if (direction == shapeDir or
                        direction == dirs[direction-1] or
                        direction == dirs[(direction+1)%8]
                    ):
                        #print(j+x,i+y,x,y)
                        cv2.line(skx,(j+xL,i+yUp),(x,y),0,1)
                        breaked = True
                        break
            if breaked:
                break

def connectDeadEndsToDeadEnds(deadEnds,skc):
    for y1,x1,_,_ in deadEnds:
        for y2,x2,_,_ in deadEnds:
            dist = sqrt((y2-y1)**2 + (x2-x1)**2)
            #print(x1,y1,x2,y2)
            #print('dist',dist)
            if (dist <= 5):
                cv2.line(skc,(x2,y2),(x1,y1),0,1)
    
def connectEntities(hulls,hulls_orig,binarizedImg,shapes):
    bin_copy = binarizedImg.astype(np.uint8).copy()
    boxes = [cv2.boundingRect(cnt) for cnt in hulls]
    h,w = binarizedImg.shape
    colored_contours = 255*np.ones((h,w,3))
    colored_contours_labelled = 255*np.ones((h,w,3))

    for i,h in enumerate(hulls):
        b,r,g = 0,0,0
        if i<=255:
            b=i
        elif(i <= 255*2):
            b=255
            r=i-255
        elif(i <= 255*3):
            b,r=255,255
            g= i-255*2
        cv2.drawContours(colored_contours,[h],-1,(b,r,g),-1)
        cv2.drawContours(colored_contours_labelled,[h],-1,(b,r,g),1)
        cv2.putText(colored_contours_labelled,f'Label: {b} {r} {g}',(boxes[i][0],boxes[i][1]-5),0,0.3,(0,0,255)) #for visualization

    
    cv2.imwrite("colored_contours.png",colored_contours)
    cv2.imwrite("inner_outer_borders.png",bin_copy)
    bin_copy = (255 - bin_copy)/255
    skeleton = skeletonize(bin_copy)
    skeleton = (255 - skeleton*255).astype(np.uint8).copy()

    c=scale_contours(hulls_orig[:],0.9)
    cv2.drawContours(skeleton,c,-1,(255),-1)

    sk_copy = skeleton.astype(np.uint8).copy()

    cv2.imwrite("sk.png",skeleton)

    allDeadEnds = []
    foundVis = np.zeros(len(shapes))
    for i,s in enumerate(shapes):
        if s == 'rectangle':
            foundVis[i]=1
            y,x  = findPixel(boxes[i],skeleton,colored_contours,i)
            colored_contours_labelled[y,x]=(0,0,255)
            deadEnds,foundShapes = BFS(y,x,colored_contours,skeleton,i,colored_contours_labelled,foundVis)
            # print(f"shape {i} found {foundShapes}")
            # print(f"shape {i} deadends {deadEnds}")
            allDeadEnds += deadEnds

    cv2.imwrite("sk2.png",skeleton)
    print("Running Not Found shapes")
    for i,f in enumerate(foundVis):
        # if f == 1 and shapes[i] != 'diamond':
        #     continue
        y,x  = findPixel(boxes[i],skeleton,colored_contours,i)
        colored_contours_labelled[y,x]=(0,0,255)
        deadEnds,foundShapes = BFS(y,x,colored_contours,skeleton,i,colored_contours_labelled,foundVis)
        # print(f"shape {i} found {foundShapes}")
        # print(f"shape {i} deadends {deadEnds}")
        if len(foundShapes):
            foundVis[i]=1
        allDeadEnds += deadEnds

    cv2.imwrite("sk3.png",skeleton)


    allDeadEnds = list(set(allDeadEnds))
    connectDeadEndsToShapes(allDeadEnds,colored_contours,sk_copy)
    connectDeadEndsToDeadEnds(allDeadEnds,sk_copy)
    cv2.imwrite("sk4.png",sk_copy)
    skeleton_ret = sk_copy.copy()

    # sk_copy = (255 - sk_copy)/255
    # cv2.imwrite("sk4.png",sk_copy*255)

    # sk_copy = skeletonize(sk_copy)
    # cv2.imwrite("sk5.png",sk_copy*255)
    # sk_copy = (255 - sk_copy*255).astype(np.uint8).copy()
    # cv2.imwrite("sk6.png",sk_copy)

    foundVis = np.zeros(len(shapes))
    foundShapesEntities = []
    for i,s in enumerate(shapes):
        if s == 'rectangle':
            foundVis[i]=1
            y,x  = findPixel(boxes[i],sk_copy,colored_contours,i)
            colored_contours_labelled[y,x]=(0,0,255)
            deadEnds,foundShapes = BFS(y,x,colored_contours,sk_copy,i,colored_contours_labelled,foundVis)
            # print(f"shape {i} {s} found {foundShapes}")
            # print(f"shape {i} {s} deadends {deadEnds}")
            foundShapesEntities.append(  
                {
                    "idx":i,
                    "name":'x',
                    "contour":hulls_orig[i],
                    "bounding_box": boxes[i],
                    "relations":[{"idx":r,"contour":hulls_orig[r],"bounding_box":boxes[r],"attributes":[]} for r in foundShapes if shapes[r]=='diamond'],
                    "attributes":[{"idx":a,"contour":hulls_orig[a],"bounding_box":boxes[a],"children":[]} for a in foundShapes if shapes[a]=='oval']
                })

    ######################format parent atrributes



    ##################### run from children atrribute
    # stack = []
    cv2.imwrite("sk5.png",sk_copy)
    for idxf,f in enumerate(foundShapesEntities):
        for idxr,r in enumerate(f['relations']):
            i = r['idx']
            y,x  = findPixel(boxes[i],sk_copy,colored_contours,i)
            colored_contours_labelled[y,x]=(0,0,255)
            deadEnds,foundShapes = BFS(y,x,colored_contours,sk_copy,i,colored_contours_labelled,foundVis)
           # print(f"relation {i} found {foundShapes}")
            foundShapesEntities[idxf]['relations'][idxr]['attributes'] += [
            {"idx":a,"contour":hulls_orig[a],"bounding_box":boxes[a],"children":[]} for a in foundShapes if shapes[a]=='oval']
        for idxa,a in enumerate(f['attributes']):
            i = a['idx']
            y,x  = findPixel(boxes[i],sk_copy,colored_contours,i)
            colored_contours_labelled[y,x]=(0,0,255)
            deadEnds,foundShapes = BFS(y,x,colored_contours,sk_copy,i,colored_contours_labelled,foundVis)
           # print(f"att {i} found {foundShapes}")
            foundShapesEntities[idxf]['attributes'][idxa]['children'] += [
                {"idx":a,"contour":hulls_orig[a],"bounding_box":boxes[a],"children":[]} for a in foundShapes if shapes[a]=='oval']

    #################### format children attribute

    print(foundShapesEntities)

    cv2.imwrite("sk6.png",sk_copy)
    for i,f in enumerate(foundVis):
        if not f:
            print(f"shape {i} not found")
    cv2.imwrite("colored_contours_labelled.png",colored_contours_labelled)
    skeleton_ret = 255-skeleton_ret
    return foundShapesEntities ,skeleton_ret
    

