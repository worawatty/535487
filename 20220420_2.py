import numpy as np
import cv2
#create black, empty canvas]
img = np.zeros((512,512,3), np.uint8)
#img2 = np.ones((512,512,3),np.uint8)
#img2 = img2*255
#Draw diagonal line
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
img = cv2.rectangle(img,(128,128),(384,384),(0,0,255),5)
img = cv2.circle(img,(255,255),128,(0,255,0),5)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,"Drawings",(128,100),font,1,(0,255,255),3)

#accessing image pixel
px = img[50,50]
print(px)

#modify pixel
px = [0,0,255]
img[50:55,50:55] = px

cv2.imshow("black canvas",img)
cv2.waitKey(0)
cv2.destroyAllWindows()