import cv2
import numpy as np

img = cv2.imread("tb.png")

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.adaptiveThreshold(img1, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
        21, 0)


cv2.imshow("9-4adaptiveThreshold原图", img)
cv2.imshow("9-4adaptiveThreshold灰度图", img1)
cv2.imshow("9-4adaptiveThreshold阈值化", dst)

while cv2.waitKey(1) != ord("q"):
    pass

cv2.destroyAllWindows()