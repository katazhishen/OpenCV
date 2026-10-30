
import cv2
import numpy as np

img = cv2.imread("hand.png")
img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
print(img.shape)

# 转变为单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

# 查找轮廓
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contours)


img1 = img.copy()
r = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(img1, [box], 0, (0, 255, 0), 2)

img2 = img.copy()
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 0, 255), 2)


cv2.imshow("10-6外接矩阵原图", img)
cv2.imshow("10-6外接矩阵-minArea", img1)
cv2.imshow("10-6外接矩阵-bounding", img2)

while cv2.waitKey(1) != ord("q"):
    pass

cv2.destroyAllWindows()