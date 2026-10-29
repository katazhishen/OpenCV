import cv2
import numpy as np

img = cv2.imread("tb.png")

h, w, ch = img.shape

# 中值滤波 处理胡椒噪音
dst = cv2.medianBlur(img, 5)

cv2.imshow("8-6原图", img)
cv2.imshow("8-6中值滤波", dst)


while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()