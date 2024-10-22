import cv2
from numpy.core.defchararray import count
from skimage.morphology import skeletonize
import numpy as np
from math import sqrt
from ..remove_lines import *
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
    for i in range(y+h//4,min(y+h,hImg)):
        for j in range(x+2,min(x+w,wImg)):
            if(img[i,j]==0 and sum(colored_im[i,j]) == idx):
                return i,j
    return 0,0

def getDirection(x1,y1,x2,y2):


    if(abs(y2-y1)<=4):
        return 0 if x2>x1 else 4
    if(abs(x2-x1)<=4):
        return 2 if y2>y1 else 6

    if(y2>y1):
        return 1 if x2>x1 else 3
    else:
        return 7 if x2>x1 else 5


def BFS(shapes,y,x,colored_contours,skb,idx,colored_contours_labelled,foundVis):
    q = []
    found =[]
    startX,startY = x,y
    hImg,wImg = skb.shape
    q.append((y,x))
    deadend =[]

    while len(q):
        y,x = q.pop(0)
  

        hasFound = False
        countVis,countWhite=0,0
        for nY,nX in neighbors:
            coorX,coorY = x+nX,y+nY
            if coorX >= wImg or coorX<0 or coorY>=hImg or coorY <0:
                continue
            if(skb[coorY,coorX] == 254):
                countVis +=1
                continue
            cur = int(sum(colored_contours[coorY,coorX]))
            if(cur != 255*3 and cur != idx):
                if (foundVis[cur] and shapes[cur]=="oval"): break
                foundVis[cur] = 1
                found.append(cur)
                hasFound = True
                break
                
            if(skb[coorY,coorX]==0):
                skb[coorY,coorX] = 254
                q.append((coorY,coorX))
            else:
                countWhite +=1


        if(not hasFound and countVis == 1 and countWhite == 7 and sum(colored_contours[y,x]) == 255*3.0 ):
            ##print(sum(colored_contours[y,x]))
            deadend.append((y,x,getDirection(startX,startY,x,y),idx))
            colored_contours_labelled[y,x]=(0,255,0)
    return list(set(deadend)),list(set(found))

def connectDeadEndsToShapes(deadEnds,colored_im,skx):
    for y,x,direction,idx in deadEnds:
        hImg,wImg,_ = colored_im.shape
        m = 10
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
                    if idx == 35:
                        print(shapeDir , direction)
                    if (direction == shapeDir or
                        direction == dirs[shapeDir-1] or
                        direction == dirs[(shapeDir+1)%8]
                    ):
                        cv2.line(skx,(j+xL,i+yUp),(x,y),0,1)
                        breaked = True
                        break
            if breaked:
                break

def connectDeadEndsToDeadEnds(deadEnds,skc):
    for y1,x1,_,_ in deadEnds:
        for y2,x2,_,_ in deadEnds:
            dist = sqrt((y2-y1)**2 + (x2-x1)**2)
            if (dist <= 5):
                cv2.line(skc,(x2,y2),(x1,y1),0,1)
    
def connectEntities(hulls,hulls_orig,binarizedImg,shapes,text,weak,isKey,dataTypesArr):
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

    path = "../connectEntitiesOutput/"
    cv2.imwrite(path+"colored_contours.png",colored_contours)
    cv2.imwrite(path+"inner_outer_borders.png",bin_copy)
    bin_copy = (255 - bin_copy)/255
    skeleton = skeletonize(bin_copy)
    skeleton = (255 - skeleton*255).astype(np.uint8).copy()

    c=scale_contours(hulls_orig[:],0.9)
    cv2.drawContours(skeleton,c,-1,(255),-1)

    sk_copy = skeleton.astype(np.uint8).copy()

    cv2.imwrite(path+"sk.png",skeleton)
    allDeadEnds = []
    foundVis = np.zeros(len(shapes))
    for i,s in enumerate(shapes):
        if s == 'rectangle':
            foundVis[i]=1
            y,x  = findPixel(boxes[i],skeleton,colored_contours,i)
            colored_contours_labelled[y,x]=(0,0,255)
            deadEnds,foundShapes = BFS(shapes,y,x,colored_contours,skeleton,i,colored_contours_labelled,foundVis)
            allDeadEnds += deadEnds

    cv2.imwrite(path+"sk2.png",skeleton)
    for i,f in enumerate(foundVis):
        y,x  = findPixel(boxes[i],skeleton,colored_contours,i)
        colored_contours_labelled[y,x]=(0,0,255)
        deadEnds,foundShapes = BFS(shapes,y,x,colored_contours,skeleton,i,colored_contours_labelled,foundVis)
        if len(foundShapes):
            foundVis[i]=1
        allDeadEnds += deadEnds

    cv2.imwrite(path+"sk3.png",skeleton)


    allDeadEnds = list(set(allDeadEnds))
    connectDeadEndsToShapes(allDeadEnds,colored_contours,sk_copy)
    connectDeadEndsToDeadEnds(allDeadEnds,sk_copy)
    cv2.imwrite(path+"sk4.png",sk_copy)
    skeleton_ret = sk_copy.copy()


    foundVis = np.zeros(len(shapes))
    foundShapesEntities = []
    for i,s in enumerate(shapes):
        if s == 'rectangle':
            foundVis[i]=1
            y,x  = findPixel(boxes[i],sk_copy,colored_contours,i)
            colored_contours_labelled[y,x]=(0,0,255)
            deadEnds,foundShapes = BFS(shapes,y,x,colored_contours,sk_copy,i,colored_contours_labelled,foundVis)
            foundShapesEntities.append(  
                {
                    "idx":i,
                    "isWeak":weak[i],
                    "name":text[i],
                    "contour":hulls_orig[i],
                    "bounding_box": boxes[i],
                    "relations":[{"idx":r,"isIdentitfying":weak[r],"name":text[r],"contour":hulls_orig[r],"bounding_box":boxes[r],"attributes":[]} for r in foundShapes if shapes[r]=='diamond'],
                    "attributes":[{"idx":a, "dataType":dataTypesArr[a],"isKey":isKey[a],"isMultivalued":weak[a],"name":text[a],"contour":hulls_orig[a],"bounding_box":boxes[a],"children":[]} for a in foundShapes if shapes[a]=='oval']
                })

    

    cv2.imwrite(path+"sk5.png",sk_copy)
    for idxf,f in enumerate(foundShapesEntities):
        for idxr,r in enumerate(f['relations']):
            i = r['idx']
            y,x  = findPixel(boxes[i],sk_copy,colored_contours,i)
            colored_contours_labelled[y,x]=(0,0,255)
            deadEnds,foundShapes = BFS(shapes,y,x,colored_contours,sk_copy,i,colored_contours_labelled,foundVis)
            foundShapesEntities[idxf]['relations'][idxr]['attributes'] += [
            {"idx":a,"dataType":dataTypesArr[a],"isKey":isKey[a],"name":text[a],"isIdentitfying":weak[a],"contour":hulls_orig[a],"bounding_box":boxes[a],"children":[]} for a in foundShapes if shapes[a]=='oval']
        
        for idxa,a in enumerate(f['attributes']):
            i = a['idx']
            y,x  = findPixel(boxes[i],sk_copy,colored_contours,i)
            colored_contours_labelled[y,x]=(0,0,255)
            deadEnds,foundShapes = BFS(shapes,y,x,colored_contours,sk_copy,i,colored_contours_labelled,foundVis)

            foundShapesEntities[idxf]['attributes'][idxa]['children'] += [
                {"idx":a,"dataType":dataTypesArr[a] ,"isKey":isKey[i],"name":text[a],"isMultivalued":weak[a],"contour":hulls_orig[a],"bounding_box":boxes[a],"children":[]} for a in foundShapes if shapes[a]=='oval']



    cv2.imwrite(path+"sk6.png",sk_copy)
    for i,f in enumerate(foundVis):
        if not f:
            print(f"shape {i} not found")
    cv2.imwrite(path+"colored_contours_labelled.png",colored_contours_labelled)
    skeleton_ret = 255-skeleton_ret
    return foundShapesEntities ,skeleton_ret
    

def removeContours(entities):
    for i,c in enumerate(entities):
        entities[i].pop('contour')
        entities[i].pop('bounding_box')
        for r in entities[i]['relations']:
            r.pop('contour')
            for c in r['attributes']:
                c.pop('bounding_box')
                c.pop('contour')
                for cn in c['children']:
                    cn.pop('bounding_box')
                    cn.pop('contour')

        for a in entities[i]['attributes']:
            a.pop('bounding_box')
            a.pop('contour')
            for c in a['children']:
                c.pop('bounding_box')
                c.pop('contour')
        
    return entities

def removeContoursRelations(relations):
    for r in relations:
        if relations[r].get('contour') is not None:
            relations[r].pop('contour')
        if relations[r].get('bounding_box') is not None:
            relations[r].pop('bounding_box')
        if relations[r].get('contour_cardinality') is not None:
            relations[r].pop('contour_cardinality')
        if relations[r].get('contour_participation') is not None:
            relations[r].pop('contour_participation')
        if relations[r].get('paths') is not None:
            relations[r].pop('paths')
        for entity in relations[r]['entities']:
            if entity.get('contour') is not None:
                entity.pop('contour')
            if entity.get('bounding_box') is not None:
                entity.pop('bounding_box')
            if entity.get('contour_cardinality') is not None:
                entity.pop('contour_cardinality')
            if entity.get('contour_participation') is not None:
                entity.pop('contour_participation')
            if entity.get('paths') is not None:
                entity.pop('paths')           
        
    return relations

def addDefaultKey(entities , idx):
    for e in entities:
        if not e["isWeak"]:
            hasKey = any([attr["isKey"] for attr in e["attributes"]])
            if not hasKey:
                e["attributes"].append({
                    "idx": idx,
                    "dataType": "int",
                    "isKey": not hasKey,
                    "isMultivalued": hasKey,
                    "name": "IncrementalKey",
                    "children": []
                })
                idx+=1
    return entities , idx