import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    img = frame
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    upper_orange = np.array([27, 255, 255])
    lower_orange = np.array([17, 50, 20])

    masked_img = cv2.inRange(hsv_img, lower_orange, upper_orange)
    #result = cv2.bitwise_and(img, img, mask=masked_img)
    kernel = np.ones((3, 3), np.uint8)

    thresh = cv2.erode(masked_img, kernel, iterations=10)
    thresh = cv2.dilate(thresh, kernel, iterations=10)
    contours,h = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    status = "Not Detected"
    for c in contours:
        if cv2.contourArea(c)>500:
            cv2.drawContours(img,c,-1,(0,255,0),5)
            status="Detected"
    cv2.putText(img,"Object: "+status,(50,50),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),3)
    cv2.imshow("Frame",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()