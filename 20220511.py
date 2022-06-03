import cv2
import numpy as np

img = cv2.imread('numbers.png',cv2.IMREAD_COLOR)

ret,thresh = cv2.threshold(img,10,255,cv2.THRESH_BINARY)

cv2.imshow("gradient",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()