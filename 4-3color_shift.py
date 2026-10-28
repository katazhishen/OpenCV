import cv2
import numpy as np


cv2.namedWindow("color_shift", cv2.WINDOW_NORMAL)

img = cv2.imread("tb.png")

def callback(pos):
    pass


colorspace = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA, 
              cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV_FULL, 
              cv2.COLOR_BGR2YUV, cv2.COLOR_BGR2HSV]
cv2.createTrackbar("curcolor", "color_shift", 0, int(len(colorspace)-1), callback)


while True:
    v = cv2.getTrackbarPos("curcolor", "color_shift")

    cvtimg = cv2.cvtColor(img, colorspace[v])
    cv2.imshow("color_shift", cvtimg)



    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()