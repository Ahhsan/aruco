import cv2
from cv2 import aruco

marker_size=500
dic=aruco.getPredefinedDictionary(aruco.DICT_5X5_250)

for id in range(20):  #generates 20 different arucos of id ranging from 0 to 19 
    marker_image=aruco.generateImageMarker(	dic, id, marker_size)   
    cv2.imshow("img",marker_image)    
    cv2.waitKey(0)
