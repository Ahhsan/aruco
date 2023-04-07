import cv2
from cv2 import aruco

while True:
    img=cv2.imread("1.jpg")
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dic=aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
    detectorParams = cv2.aruco.DetectorParameters()

    (corners, ids, rejected) = cv2.aruco.detectMarkers(gray, dic, parameters=detectorParams)
    cv2.aruco.drawDetectedMarkers(img, corners, ids)
    print(ids)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    break 
