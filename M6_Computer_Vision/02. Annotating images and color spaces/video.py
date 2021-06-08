import cv2
import numpy as np
import matplotlib.pyplot as plt

video = cv2.VideoCapture(0)
g_l_range = (40, 50, 20)
g_u_range = (80, 255, 255)
b_l_range = (95, 50, 20)
b_u_range = (145, 255, 255)
while(video.isOpened()):
    check, frame = video.read()
    if frame is not None:
        img = frame
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        #mask1 = cv2.inRange(hsv_img,b_l_range,b_u_range)
        maskg = cv2.inRange(hsv_img,g_l_range,g_u_range)
        
        img_copy = img.copy()

        #img_copy[mask1 == 0] = [0,0,0]
        img_copy[maskg == 0] = [0,0,0]

        cv2.imshow('frame',frame)        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


video.release()

cv2.destroyAllWindows()