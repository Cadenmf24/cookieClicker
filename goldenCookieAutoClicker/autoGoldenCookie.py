import cv2
import numpy as np
from tensorflow import keras


incomingData = cv2.VideoCapture('rtsp://localhost/live', cv2.CAP_FFMPEG)

lowerGold = np.array([82, 137, 153], dtype = "uint8") 

upperGold = np.array([123, 205, 229], dtype = "uint8") 

while True:

    status, image = incomingData.read()

    mask = cv2.inRange(image, lowerGold, upperGold)

    detected_output = cv2.bitwise_and(image, image, mask =  mask) 

    cv2.imshow("Golden Cookie detection", detected_output) 

    cv2.imshow('Cookie Clicker', image)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


incomingData.release()

cv2.destroyAllWindows()


