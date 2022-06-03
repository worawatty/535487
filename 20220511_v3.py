import numpy as np
import cv2

yellow = np.uint8([[[11,171,233]]])
yello_hsv = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
print(yello_hsv)
img = cv2.imread("ball.PNG",cv2.IMREAD_COLOR)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsv_ball = cv2.cvtColor(yello_hsv,cv2.COLOR_BGR2HSV)
upper_orange = np.array([17,255,255])
lower_orange = np.array([7,90,150])

masked_img =cv2.inRange(hsv_img,lower_orange,upper_orange)
#noise reduction
kernel = np.ones((3,3),np.uint8)
e_img =cv2.erode(masked_img,kernel,iterations=7)
d_img = cv2.dilate(e_img,kernel,iterations=7)

contours, hierachy = cv2.findContours(d_img,
                    cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for c in contours:
    cv2.drawContours(img,c,-1,(0,255,0),3)
print(contours)

#result = cv2.bitwise_and(img,img,mask=d_img)
#result =cv2.resize(result,(1024,768))
cv2.imshow("masked",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



print(hsv_ball)
