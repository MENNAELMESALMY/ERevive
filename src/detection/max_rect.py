import numpy as np
import cv2
def get_max_rect(mask):
    topleft_corner = []
    bottomright_corner = [] 
    rectangle_heights= [] 
    rectangle_areas = []
  
    for i in range(0,mask.shape[1]):
        line = mask[:,i]
        foreground_indecies = np.where(line == 255)
        if len(foreground_indecies[0]) == 0:    
            continue
        top_p1 = foreground_indecies[0][0]
        bottom_p1 = foreground_indecies[0][-1]
        line1_length = bottom_p1 - top_p1
        for j in range(mask.shape[1]-1,i+2,-1):
            line2 = mask[:,j]
            foreground_indecies = np.where(line2 == 255)
            if len(foreground_indecies[0]) == 0:    
                continue
            top_p2 = foreground_indecies[0][0]
            bottom_p2 = foreground_indecies[0][-1]
            line2_length = bottom_p2 - top_p2

            if line1_length == line2_length and i != j :
                topleft_corner.append([i,top_p1])
                bottomright_corner.append([j,bottom_p2])
                rectangle_heights.append(line1_length)
                rectangle_areas.append((j-i) *(line1_length))


    max_area_index = np.argmax(np.array(rectangle_areas))
    top_left = topleft_corner[max_area_index]
    bottom_right = bottomright_corner[max_area_index]
    cv2.rectangle(mask,(top_left[0],top_left[1]),(bottom_right[0],bottom_right[1]),(0,0,0),-1)

    return rectangle_areas[max_area_index],mask

def area(contour,A, B, C):
    A=contour[A]
    B=contour[B]
    C=contour[C]
    return abs(A[0]*(B[1]-C[1]) + B[0]*(C[1]-A[1]) + C[0]*(A[1]-B[1])) / 2.0

def max_triangle(contour):
    n = len(contour)
    A = 0; B = 1; C = 2
    bA= A; bB= B; bC= C

    while True: 

        while True:
            while area(contour,A, B, C) <= area(contour,A, B, (C+1)%n):
                C = (C+1)%n
            if area(contour,A, B, C) <= area(contour,A, (B+1)%n, C): 
                B = (B+1)%n
                continue
            else:
                break

        if area(contour,A, B, C) > area(contour,bA, bB, bC):
            bA = A; bB = B; bC = C
            

        A = (A+1)%n
        if A==B: B = (B+1)%n
        if B==C: C = (C+1)%n
        if A==0: break
    
    return area(contour,bA, bB, bC), contour[bA], contour[bB], contour[bC]
        