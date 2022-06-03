import numpy as np
import cv2

img = cv2.imread("gear_good.jpg",cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY)
kernel = np.ones((3,3),np.uint8)
thresh=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=1)

contours,hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
hole_count = 0
for c in contours:
    #cv2.drawContours(img, c, -1, (0, 255, 0), 3)
    if cv2.contourArea(c)<=10000:
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
        if shape=="circle":
            hole_count+=1
if hole_count==7:
    cv2.putText(img, "QC PASSED", (10,20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
else:
    cv2.putText(img, "QC Failed", (10, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
cv2.imshow("threshold",img)
cv2.waitKey(0)
cv2.destroyAllWindows()