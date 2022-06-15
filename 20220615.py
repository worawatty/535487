import cv2
import numpy

img = cv2.imread("messi.jpg",cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cap = cv2.VideoCapture("shapesvideo_exam.mp4")

while True:
    ret, frame = cap.read()
    img = frame
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img, 190, 255)
    cv2.imshow("Frame", edges)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()