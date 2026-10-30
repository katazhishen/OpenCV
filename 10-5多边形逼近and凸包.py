
import cv2
import numpy as py

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

# 绘制轮廓
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# 绘制轮廓
def drawShape(src, points):
    i = 0
    while i < len(points):
        if i == len(points)-1:
            x, y = points[i][0]
            x1, y1 = points[0][0]
        else:
            x, y = points[i][0]
            x1, y1 = points[i+1][0]
        
        cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 4)
        i += 1

# 多边形逼近轮廓
ee = 20 # 近似轮廓的精度
#  True 表示闭合轮廓
approx = cv2.approxPolyDP(contours[0], ee, True)

# 凸包
hull = cv2.convexHull(contours[0])


img1 = img.copy()
img2 = img.copy()

drawShape(img1, approx)
drawShape(img2, hull)

cv2.imshow("10-5.py原图", img)
cv2.imshow("10-5.py", binary)
cv2.imshow("10-5.py-approx", img1)
cv2.imshow("10-5.py-hull", img2)

while cv2.waitKey(1) != ord("q"):
    pass

cv2.destroyAllWindows()