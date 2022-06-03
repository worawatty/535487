import numpy as np
import cv2

yellow = np.uint8([[[11,171,233]]])
yello_hsv = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
print(yello_hsv)
#bg = np.zeros((100,100,3),np.uint8)
img = cv2.imread("yellow.jpg",cv2.IMREAD_COLOR)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsv_ball = cv2.cvtColor(yello_hsv,cv2.COLOR_BGR2HSV)
upper_orange = np.array([27,255,255])
lower_orange = np.array([17,50,20])

masked_img =cv2.inRange(hsv_img,lower_orange,upper_orange)
result = cv2.bitwise_and(img,img,mask=masked_img)
result =cv2.resize(result,(1024,768))
cv2.imshow("masked",result)
cv2.waitKey(0)
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read();
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


print(hsv_ball)
