import cv2
import numpy as np

img = cv2.imread("tb.png")

# scharr算子滤波
d1 = cv2.Scharr(img, cv2.CV_64F, 1, 0, scale=1)
d2 = cv2.Scharr(img, cv2.CV_64F, 0, 1, scale=1)  

dst = cv2.add(d1, d2)

cv2.imshow("8-9原图", img)
cv2.imshow("8-9高通滤波", dst)


while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()