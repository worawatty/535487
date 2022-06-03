import numpy as np
import cv2

img = cv2.imread("shapes.png",cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY)
kernel = np.ones((3,3),np.uint8)
thresh=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

contours,hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for c in contours:
    cv2.drawContours(img,c,-1,(0,255,0),3)
    epsilon = 0.02*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    print(approx)
    if len(approx) == 3:
        shape = "triangle"
    elif len(approx) == 4:
        shape = "rectangle"
    elif len(approx) == 5:
        shape = "pentagon"
    elif len(approx) == 6:
        shape = "hexagon"
    else:
        shape = "circle"
    x,y,w,h=cv2.boundingRect(c)
    cv2.putText(img,shape,(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),1)
cv2.imshow("threshold",img)
cv2.waitKey(0)
cv2.destroyAllWindows()