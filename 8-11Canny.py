import cv2
import numpy as np

img = cv2.imread("tb.png")

# Canny算子     好……nb！！！！
dst = cv2.Canny(img, 100, 200)


cv2.imshow("8-11原图", img)
cv2.imshow("8-11Canny算子", dst)


while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()