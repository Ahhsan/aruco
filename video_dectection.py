#video dectection 
import cv2
import numpy as np
from cv2 import aruco

cap=cv2.VideoCapture(0)

while 1:
    ret,frame_org=cap.read()
    frame=cv2.cvtColor(frame_org,cv2.COLOR_BGR2GRAY)
    dic=aruco.getPredefinedDictionary(aruco.DICT_5X5_250)
    detectorParams = cv2.aruco.DetectorParameters()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(frame, dic, parameters=detectorParams)
    cv2.aruco.drawDetectedMarkers(frame_org, corners, ids)
    print(ids)
    cv2.imshow("aruco_detect",frame_org)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()   