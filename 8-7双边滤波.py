import cv2
import numpy as np

img = cv2.imread("tb.png")

h, w, ch = img.shape

# 双边滤波 进行美颜
dst = cv2.bilateralFilter(img, 7, 20, 50)

cv2.imshow("8-7原图", img)
cv2.imshow("8-7双边滤波", dst)


while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()