import numpy as np
import cv2

img = cv2.imread('messi.jpg',cv2.IMREAD_COLOR)
print(img.shape)

ball = img[240:280,280:320]
img[50:90,50:90] = ball
print(ball)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('messi_extra_ball.jpg', img)

print('Hello World')
print(np.__version__)
print(cv2.__version__)