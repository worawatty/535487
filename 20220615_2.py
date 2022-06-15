import cv2
import numpy as np

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

cap = cv2.VideoCapture("shapesvideo_exam.mp4")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    new_frame = increase_brightness(frame,value=100)
    gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)
    kernel = np.ones((3,3),np.uint8)
    erosion = cv2.erode(thresh,kernel,iterations=1)
    dilation = cv2.dilate(erosion,kernel,iterations=1)

    contours,hierachy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    countRect = 0
    for c in contours:
        #find vertices
        epsilon = 0.035*cv2.arcLength(c,True)
        vertices = cv2.approxPolyDP(c,epsilon,True)
        
        print(len(vertices))
        x,y,w,h = cv2.boundingRect(c)
        if len(vertices)==4 and w*h>5000:
            text = "Rectangle"
            rotrect = cv2.minAreaRect(c)
            angle = rotrect[-1]
            box = cv2.boxPoints(rotrect)
            box=np.int0(box)
            cv2.drawContours(frame,c,-1,(255,0,0),5)
            if angle < -45:
                angle = (90 + angle)
            else:
                angle = -angle
            cv2.putText(frame, text+" angle: "+str(angle), (x+w, y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            #cv2.drawContours(frame,c,-1,(255,0,0),5)
            #countRect+=1
            #cv2.putText(frame,text,(x+w,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),2)
        elif len(vertices)==6 and w*h>5000:
            text2 ="NG"
            cv2.drawContours(frame,c,-1,(0,0,255),5)
            cv2.putText(frame,text2,(x+w,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        elif len(vertices)>6 and w*h>5000:
            text3 = "Good"
            cv2.drawContours(frame,c,-1,(0,255,0),5)
            cv2.putText(frame,text3,(x+w,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

        
    #cv2.putText(frame,"Number of rectangle:"+str(countRect),(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()