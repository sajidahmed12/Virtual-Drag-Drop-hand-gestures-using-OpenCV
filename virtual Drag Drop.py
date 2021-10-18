import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
colorRec = 255,255,0


cx, cy, w, h = 100, 10, 200, 200
 

while(True):
    success, img = cap.read()
    img =cv2.flip(img, 1) 
    img = detector.findHands(img)
    lmList, _ = detector.findPosition(img)
    
    if lmList:

        l, _, _ = detector.findDistance(8, 12, img)
        if(l<40):
            cursor =  lmList[8]    # x,y of fingertip
            if cx-w//2 < cursor[0] < cx+w//2 and  cy-h//2 < cursor[1] <  cy+h//2:
                colorRec = 0,255,0
                cx, cy = cursor

            else:
                colorRec = (255,0,255)  

    cv2.rectangle(img, (cx-w//2, cy-h//2), (cx+w//2,cy+h//2), colorRec, cv2.FILLED)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()