import cv2
import numpy as np

img = cv2.imread('coins.jpg',cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(img_gray,255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,37,17)
ret,thresh = cv2.threshold(img_gray,250,255,cv2.THRESH_BINARY_INV)
#For drawing contours
kernel = np.ones((5,5),np.uint8)
thresh3=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=3)

#For counting contours
kernel = np.ones((3,3),np.uint8)
thresh2=cv2.dilate(thresh,kernel,iterations=5)
kernel = np.ones((5,5),np.uint8)
thresh2=cv2.erode(thresh2,kernel,iterations=32)

contours, h =cv2.findContours(thresh3,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
contours2, h =cv2.findContours(thresh2,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

count=0
for c in contours:
        if cv2.contourArea(c) > 500:
                cv2.drawContours(img,c,-1,(0,255,0),10)

for c in contours2:
        if cv2.contourArea(c) > 500:
                count+=1
text = "Number of Coins: "+str(count)
cv2.putText(img,text,(100,100),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),5)
cv2.imshow("gradient",thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()