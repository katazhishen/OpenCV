import cv2
import numpy as np

img = cv2.imread("tb.png")

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(img1, 138, 255, cv2.THRESH_BINARY)

print(ret)
cv2.imshow("9-2threshold原图", img)
cv2.imshow("9-2threshold灰度图", img1)
cv2.imshow("9-2threshold阈值化", dst)

while cv2.waitKey(1) != ord("q"):
    pass

cv2.destroyAllWindows()