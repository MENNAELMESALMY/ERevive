import numpy as np  
from skimage.morphology import dilation,closing,opening
import itertools
import matplotlib.pyplot as plt
from scipy import misc
from scipy.sparse.dok import dok_matrix
from scipy.sparse.csgraph import dijkstra
import cv2 as cv



from collections import deque
ROW = 9
COL = 10
 
# To store matrix cell coordinates
class Point:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y
 
# A data structure for queue used in BFS
class queueNode:
    def __init__(self,pt: Point, dist: int):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source
 
# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)
 
# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1,1,1,-1,-1]
colNum = [0, -1, 1, 0,1,-1,1,-1]
 
# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src: Point, dest: Point):
     
    # check source and destination cell
    # of the matrix have value 1
    if mat[src.x][src.y]==0 or mat[dest.x][dest.y]==0:
        return -1
     
    visited = [[False for i in range(COL)]
                       for j in range(ROW)]
     
    # Mark the source cell as visited
    visited[src.x][src.y] = True
     
    # Create a queue for BFS
    q = deque()
     
    # Distance of source cell is 0
    s = queueNode(src,0)
    q.append(s) #  Enqueue source cell
     
    # Do a BFS starting from source cell
    while q:
 
        curr = q.popleft() # Dequeue the front cell
         
        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
         
        # Otherwise enqueue its adjacent cells
        for i in range(8):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
             
            # if adjacent cell is valid, has path 
            # and not visited yet, enqueue it.
            if (isValid(row,col) and
               mat[row][col] != 0 and
                not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row,col),
                                    curr.dist+1)
                q.append(Adjcell)
     
    # Return -1 if destination cannot be reached
    return -1
 
# Driver code
def run_bfs(mat,start,end):
    source = Point(start[1],start[0])
    dest = Point(end[1],end[0])
    global ROW
    ROW = mat.shape[0]
    global COL
    COL = mat.shape[1]
    dist = BFS(mat,source,dest)
    
    if dist!=-1:
        return True
    else:
        return False






def get_real_path(original_img,start,end):
    # Load the image from disk as a numpy ndarray
    
    # Create a flat color image for graph building:
    img = original_img.copy()


    # Defines a translation from 2 coordinates to a single number
    def to_index(y, x):
        return y * img.shape[1] + x


    # Defines a reversed translation from index to 2 coordinates
    def to_coordinates(index):
        return index // img.shape[1], index % img.shape[1]


    # A sparse adjacency matrix.
    # Two pixels are adjacent in the graph if both are painted.
    adjacency = dok_matrix((img.shape[0] * img.shape[1],
                            img.shape[0] * img.shape[1]), dtype=bool)

    # The following lines fills the adjacency matrix by
    directions = list(itertools.product([0, 1, -1], [0, 1, -1]))
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            if not img[i, j]:
                continue

            for y_diff, x_diff in directions:
                if img[i + y_diff, j + x_diff]:
                    adjacency[to_index(i, j),
                            to_index(i + y_diff, j + x_diff)] = True

    # We chose two arbitrary points, which we know are connected
    source = to_index(start[1], start[0])
    target = to_index(end[1], end[0])
    #print("adjacency",adjacency)
    # Compute the shortest path between the source and all other points in the image
    _, predecessors = dijkstra(adjacency, directed=False, indices=[source],
                            unweighted=True, return_predecessors=True)

    # Constructs the path between source and target
    pixel_index = target
    pixels_path = []
    while pixel_index != source:
        pixels_path.append(pixel_index)
        pixel_index = predecessors[0, pixel_index]


    # The following code is just for debugging and it visualizes the chosen path
    k=0
    #original_img = original_img*255
    for pixel_index in pixels_path:
        i, j = to_coordinates(pixel_index)
        #print("i j ",i, j)
        if k==len(pixels_path)//2:
            original_img[int(i), int(j)] = 0
        k+=1
    #cv.imwrite("path.png",original_img*255)
    return original_img,pixels_path
    #plt.imshow(original_img)
    #plt.show()
    
