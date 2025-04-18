import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#Creación de la trackbar
def empty(a):
    pass

cv.namedWindow("Umbral de Escala")
cv.resizeWindow("Umbral de Escala",640,240)
cv.createTrackbar("Umbral","Umbral de Escala",0,255,empty)
webcam = cv.VideoCapture(0) 
while(1):
    ret, imWebcam = webcam.read()
    imGris = cv.cvtColor(imWebcam,cv.COLOR_BGR2GRAY)
    ret, imgThresh = cv.threshold(imGris,cv.getTrackbarPos("Umbral","Umbral de Escala"),255,cv.THRESH_BINARY)
    ret, imgThreshInv = cv.threshold(imGris,cv.getTrackbarPos("Umbral","Umbral de Escala"),255,cv.THRESH_BINARY_INV)
    cv.imshow('Live',imWebcam)
    cv.imshow('Gray',imGris)
    cv.imshow('Threshold', imgThresh)
    #plt.hist(imGris.ravel(),256,[0,256])
    #plt.show()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()
#F