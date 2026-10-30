import cv2
import numpy as py

img = cv2.imread("ts.png")
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
print(img.shape)

# 转变为单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contours)


cv2.imshow("10-2contours.py原图", img)
cv2.imshow("10-2contours.py", binary)

while cv2.waitKey(1) != ord("q"):
    pass

cv2.destroyAllWindows()