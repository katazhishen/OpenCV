import cv2
import numpy as np

img = cv2.imread("tb.png")
# h, w
#kernel = np.ones((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
"""
dst = cv2.dilate(dst, kernel, iterations=1)
dst = cv2.erode(img, kernel, iterations=1)

"""

# 顶帽 = 原图 - 开运算  = （大图形外的小图形）
dst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

print(kernel)
cv2.imshow("9-11顶帽运算原图", img)
cv2.imshow("9-11顶帽运算", dst)

while cv2.waitKey(1) != ord("q"):
    pass

cv2.destroyAllWindows()