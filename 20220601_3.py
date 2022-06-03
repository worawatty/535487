import numpy as np
import cv2

red = np.uint8([[[91,81,139]]])
red_hsv = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print(red_hsv)


img = cv2.imread("capture_red.PNG",cv2.IMREAD_COLOR)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
upper_orange = np.array([180,255,255])
lower_orange = np.array([170,50,50])

hsv_img =cv2.inRange(hsv_img,lower_orange,upper_orange)
#noise reduction
kernel = np.ones((3,3),np.uint8)
hsv_img = cv2.morphologyEx(hsv_img,cv2.MORPH_CLOSE,kernel,iterations=3)

contours, hierachy = cv2.findContours(hsv_img,
                    cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

obj_count = 0

for c in contours:
    if cv2.contourArea(c)>1000:
        x,y,w,h = cv2.boundingRect(c)
        #cv2.drawContours(img,c,-1,(0,255,0),3)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        obj_count+=1


if obj_count==2:
    cv2.putText(img, "QC PASSED", (10, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

#result = cv2.bitwise_and(img,img,mask=d_img)
#result =cv2.resize(result,(1024,768))
cv2.imshow("QC",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
