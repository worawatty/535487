import numpy as np
import cv2

img = cv2.imread("messi.jpg",cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("HSV Image",hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale Image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
