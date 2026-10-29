import cv2
import numpy as np

img = cv2.imread("tb.png")

# 高通滤波 处理高斯噪音
# 计算x方向梯度
d1 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# 计算y方向梯度
d2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)  

dst = cv2.add(d1, d2)

cv2.imshow("8-8原图", img)
cv2.imshow("8-8高通滤波", dst)


while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()