import cv2
import numpy as np




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



def seperateShapes(contours ,cnt_img ,binary_img):
   
    text_img = 255 - 255 * np.ones((cnt_img.shape[0],cnt_img.shape[1],3), np.uint8)
    cv2.imwrite('text_img_test.png',text_img)
    binary_img = 255 - binary_img
    binary_img = np.uint8(binary_img)
    img = cv2.cvtColor(binary_img,cv2.COLOR_GRAY2RGB)
    cv2.imwrite('text_img_2_test.png',img)
    #text_img = text_img &
    
    count = 0
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        xl = max(0,x-10)
        xr = min(x+w+10,cnt_img.shape[1])
        yup = max(0,y-10)
        yd = min(y+h+10,cnt_img.shape[0])
        #seperate shape
        shape_img = 255 * np.ones((cnt_img.shape[0],cnt_img.shape[1],3), np.uint8)
        cv2.drawContours(shape_img,[cnt],-1,(0,0,0),2)
        cv2.imwrite("output/shape"+str(count)+'.png',shape_img[yup:yd,xl:xr ,:]) #write output shapes image
        #seperate text
        
        cv2.drawContours(text_img,[cnt], -1, (255,255,255), -1)
        text_img[ yup:yd,xl:xr ,:] = cv2.bitwise_and(text_img[yup:yd ,xl:xr,:] , img[yup:yd, xl:xr ,:])
        cv2.imwrite("output/text"+str(count)+'.png',text_img[y:y+h, x:x+w ,:]) #write output text image
        count+=1
    cv2.imwrite("text_img.png",text_img)
    return len(contours)
    