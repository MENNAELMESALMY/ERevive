from turtle import shape
import cv2
import numpy as np
from numpy.core.fromnumeric import partition
from .removeLines import *

def getContours(binary_img):
    #applying closing
    kernel = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)

    #get contours
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    return contours, hierarchy ,closing


def filterContours(contours, hierarchy):
    #get max area
    areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areas.append(area)
        
    max_area = max(areas)
    index = 0
    filtered_contours = []
    centers = []
    bounding_boxes = []


    #filter shapes from text
    for cnt in contours:
        if(areas[index]>(max_area/32) and hierarchy[0,index,3] == -1):
            #get centers of the shapes
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            
            filtered_contours.append(cnt)
            centers.append([cx,cy])
            bounding_boxes.append(cv2.boundingRect(cnt))    
        index+=1
    return filtered_contours,centers,bounding_boxes
    

#img_c -> copy from the original image to drow bounding boxes on shapes  for visalization
#text_img -> binarized image of the original image with the text and shapes to extract the test from
#path -> directry to output the shapes and text images
def removeOverlappedContoursAndDrawThem(filtered_contours,centers,bounding_boxes,img_c,text_img,path):
    shapes_img = 255 * np.ones((text_img.shape[0],text_img.shape[1],3), np.uint8)
    #seperate overlapped contours and draw them    
    i= 0
    j= 0
    count= 0
    overlapped = False
    for i in range(len(filtered_contours)):
        overlapped = False
        cx,cy = centers[i]
        x,y,w,h = bounding_boxes[i]
        cnt = filtered_contours[i]
        
        for j in range(len(filtered_contours)) :
            xj,yj,wj,hj = bounding_boxes[j]
            if i != j and x>xj and x+w<xj+wj and y>yj and y+h<yj+hj:
                overlapped = True
                break
            
        if overlapped == False:
            #draw contour
            cv2.drawContours(img_c, [cnt], -1, (0, 0, 255), 2)  #for visualization
            cv2.drawContours(shapes_img, [cnt], -1, (0, 0, 0), 2)
            cv2.imwrite(path+"/shape"+str(count)+'.png',shapes_img[y-10:y+h+10, x-10:x+w+10 ,:]) #write output shapes image
            cv2.drawContours(text_img, [cnt], -1, (0, 0, 0), 6)
        
            #draw center
            img_c = cv2.circle(img_c, (cx,cy), radius=0, color=(0, 0, 255), thickness=5) #for visualization
        
            #draw ponding box and label
            cv2.rectangle(img_c,(x,y),(x+w,y+h),(0,255,0),2) #for visualization
            cv2.putText(img_c,'Label: '+str(count),(x,y-5),0,0.3,(0,0,255)) #for visualization
            
            #crop text
            cv2.imwrite(path+"/text"+str(count)+'.png',text_img[y:y+h, x:x+w ,:]) #write output text image
            count+=1
    return img_c , shapes_img

def testContour(text_img,c):
    h,w = text_img.shape
    
    if h<=9 or w<=24:
        return False
    ##print(c,w,h)
    proj_img = 255* np.ones((h,w))
    text_img = text_img/255
    proj = np.sum(text_img,1)
    for row in range(h):
        cv2.line(proj_img, (0,row), (int(proj[row]),row), 0, 1)
    
    x = w//19
    counter = 0
    cv2.imwrite("proj/"+str(c)+"t.png",text_img*255)
    cv2.imwrite("proj/"+str(c)+".png",proj_img)
    for y in range(h):
        if proj_img[y][x] == 0:
            counter += 1
        else:
            if counter >= (h)//12:
                ##print('counter',counter,h)
                return True
            counter =0
    return counter >= (h)//10

def seperateShapes(contours ,cnt_img ,binary_img,count = 0):
   
    text_img = 255 - 255*np.ones((cnt_img.shape[0],cnt_img.shape[1],3), np.uint8)
    cv2.imwrite('debugOutput/text_img_test.png',text_img)
    binary_img = 255 - binary_img
    binary_img = np.uint8(binary_img)
    img = cv2.cvtColor(binary_img,cv2.COLOR_GRAY2RGB)
    cv2.imwrite('debugOutput/text_img_2_test.png',img)
    
    
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        xl = max(0,x-10)
        xr = min(x+w+10,cnt_img.shape[1])
        yup = max(0,y-10)
        yd = min(y+h+10,cnt_img.shape[0])
        #seperate shape
        shape_img = 255 * np.ones((cnt_img.shape[0],cnt_img.shape[1],3), np.uint8)

        cv2.drawContours(shape_img,[cnt],-1,(0,0,0),2)
        cv2.drawContours(text_img,[cnt], -1, (255,255,255), -1)
      
        text_img[ yup:yd,xl:xr ,:] = cv2.bitwise_and(text_img[yup:yd ,xl:xr,:] , img[yup:yd, xl:xr ,:])
        cv2.imwrite("output/text"+str(count)+'.png',text_img[y:y+h, x:x+w ,:]) #write output text image
        cv2.imwrite("output/shape"+str(count)+'.png',shape_img[yup:yd,xl:xr ,:]) #write output shapes image
        count+=1

   
    cv2.imwrite("debugOutput/text_img.png",text_img)
    return count

def checkInside(contours ,binary_img):
    binary_img = np.uint8(binary_img)
    
    count = 0
    finalContours = []
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        #seperate shape
        inside_cnt = np.zeros(binary_img.shape, np.uint8)
        cv2.drawContours(inside_cnt,[cnt], -1, 255, -1)
        inside_cnt_inv = 255 - inside_cnt

        inside_cnt = cv2.bitwise_and(inside_cnt, binary_img)
        inside_cnt = cv2.bitwise_or(inside_cnt_inv, inside_cnt)


        # cv2.imwrite("proj/demo"+str(count)+'.png',inside_cnt) #write output text image
        inside_cnt = 255 - inside_cnt

        if testContour(inside_cnt[y:y+h, x:x+w],count):
            finalContours.append(cnt)
            #seperate text
        count+=1
    return finalContours
    
def removeMultivaluedLines(shapes_no,weak,shapes,cnt):
    for i in range (shapes_no):
        if shapes[i] == "oval" and weak[i]:
            image = cv2.imread("./output/text" + str(i) + ".png",0)
            image = 255 - image
            cv2.imwrite("./multivaluesDebug/image"+str(i)+".png",image)
            invertedI = 255 - cv2.imread("./output/text" + str(i) + ".png",0)
            invertedI = cv2.cvtColor(invertedI,cv2.COLOR_GRAY2RGB)
            print(invertedI.shape)
            print(type(invertedI[0][0]))
            cv2.imwrite("./multivaluesDebug/textInverted"+str(i)+".png",invertedI)
            print(image.shape)
            filledImg = FloodFromCorners(image.copy())
            cv2.imwrite("./multivaluesDebug/filled"+str(i)+".png",filledImg)
            print("passed")
            #text_img = 255 - 255*np.ones((filledImg.shape[0],filledImg.shape[1],3), np.uint8)
            filledImg = cv2.cvtColor(filledImg,cv2.COLOR_GRAY2RGB)
            cv2.imwrite("./multivaluesDebug/textcnt"+str(i)+".png",filledImg)
            #binary_img = 255 - filledImg
            #binary_img = np.uint8(binary_img)
            #img = cv2.cvtColor(binary_img,cv2.COLOR_GRAY2RGB)
            print("filledshape" , filledImg.shape)
            print("invertedIshape" , invertedI.shape)
            text_img = cv2.bitwise_and(filledImg , invertedI)
            cv2.imwrite("./multivaluesDebug/text"+str(i)+'.png',text_img)  