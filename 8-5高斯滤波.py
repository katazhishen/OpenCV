import cv2
import numpy as np

img = cv2.imread("tb.png")

h, w, ch = img.shape


# 高斯滤波 处理高斯噪音
dst = cv2.GaussianBlur(img, (5, 5), sigmaX=1, sigmaY=1)

cv2.imshow("8-5原图", img)
cv2.imshow("8-5高斯滤波", dst)


while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()