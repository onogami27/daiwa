from cv2 import  aruco
import cv2

aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)


img_size = 150
count = 1
for i in range(5):
    ar_img = aruco.drawMarker(aruco_dict, count, img_size)

    cv2.imwrite(f"{count}.jpg",ar_img)
    count +=1