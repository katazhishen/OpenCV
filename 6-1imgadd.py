import cv2
import numpy as np

img = cv2.imread("tb.png")

# 图的加法运算就是矩阵的加法
# 注意：图的加法运算结果的像素值会超过255，会“mod”255!!!
img2 = cv2.imread("tb.png")
img3 = img + img2
cv2.imshow("img3", img3)


img3add = np.zeros_like(img)
# 图的加法运算也可以用add函数
# 超出255 取255，小于0 取0
cv2.add(img, img2, img3add)
cv2.imshow("img3add", img3add)


cv2.waitKey(0)
cv2.destroyAllWindows()