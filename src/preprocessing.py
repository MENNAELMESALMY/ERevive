from skimage.filters import threshold_yen
import numpy as np
import cv2

def OrderPoints(pts):
    rect = np.zeros((4, 2), dtype = "float32")
    n=60
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]+n
    rect[2] = pts[np.argmax(s)]-n

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]-n
    #x,y
    rect[1][0]-=n
    rect[1][1]+=n
    rect[3] = pts[np.argmax(diff)]
    #x,y
    rect[3][0]+=n
    rect[3][1]-=n
    return rect

def TransformPrespective(image, pts):
    rect = OrderPoints(pts)
    (tl, tr, br, bl) = rect
 
 
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array([
  [0, 0],
  [maxWidth - 1, 0],
  [maxWidth - 1, maxHeight - 1],
  [0, maxHeight - 1]], dtype = "float32")
 
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
 
    return warped

def GetMaxContour(img_dir,MORPH=9,CANNY=84,debug=False):
    """
    takes image directory ,
    structural rect dim(optional),canny max thres(optional)
    debug if true outputs images after each process
    returns a boolean specifying if the prespective shoud be adjusted,
    max contour approximation and grayoriginal image
    """
    img = cv2.imread(img_dir, cv2.IMREAD_GRAYSCALE)
    img_copy = img.copy()
    hImg, wImg = img_copy.shape
    #smooth image
    cv2.GaussianBlur(img, (3,3), 0, img)
    # Remove small details and writing on paper
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(MORPH,MORPH))
    dilated = cv2.dilate(img, kernel)
    edges = cv2.Canny(dilated, 0, CANNY, apertureSize=3)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    #get edges again so we get inner line surrounding the paper
    #avoid paper outer edges being connected to noise in background
    edges = cv2.dilate(edges, kernel)
    edges = cv2.Canny(edges, 0, CANNY, apertureSize=3)
    # finding contours
    im,contours,heirarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maxArea=0
    adjustPrespective = False
    approx=[]
    # filter for max contour
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if(w*h >= maxArea):
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.05 * peri, True)
            maxArea=w*h
            if(maxArea/(hImg*wImg) >= 0.1):
                adjustPrespective= True

    if(debug):
        orig = cv2.imread(img_dir)
        cv2.drawContours(orig,[approx], -1, (0, 255, 0), 1)
        cv2.imwrite("orig.png",img)
        cv2.imwrite("dilated.png",dilated)
        cv2.imwrite("edges.png",edges)
        cv2.imwrite('outline.png',orig)
    return adjustPrespective,approx,img_copy

def warpedPrespective(imgToWarp,approxContour,ratio=1,debug=False):
    warped = TransformPrespective(imgToWarp, approxContour.reshape(len(approxContour), 2) * ratio)
    if(debug):
        cv2.imwrite('result.png',warped)
    return warped

def RemoveShadow(img_gray,debug=False):
    #remove noise and writting on paper to leave out onlu the illumination
    dilated_img = cv2.dilate(img_gray, np.ones((7,7), np.uint8)) 
    blurred_img = cv2.medianBlur(dilated_img, 21)
    #remove any dark lighning aka shadow
    diff_img = 255 - cv2.absdiff(img_gray, blurred_img)
    norm_img = diff_img.copy()
    #normalization and word sharpening
    cv2.normalize(diff_img, norm_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    _, thr_img = cv2.threshold(norm_img, 230, 0, cv2.THRESH_TRUNC)
    cv2.normalize(thr_img, thr_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    if(debug):
        cv2.imwrite("shadowOut.png",norm_img)
        cv2.imwrite("thres.png",thr_img)
    return thr_img

def Binarize(img_gray,debug=False):
    thres =threshold_yen(img_gray)
    final = (img_gray >thres)*255
    if(debug):
        cv2.imwrite("final.png",final)
        #fig, ax = try_all_threshold(thr_img, figsize=(20, 30), verbose=False)
    return final
