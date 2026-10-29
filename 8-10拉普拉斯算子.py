import cv2
import numpy as np

img = cv2.imread("tb.png")

# 拉普拉斯算子滤波     好方便 好简单……
# 降噪比较差
dst = cv2.Laplacian(img, cv2.CV_64F, ksize=5)


cv2.imshow("8-10原图", img)
cv2.imshow("8-10拉普拉斯算子滤波", dst)


while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()