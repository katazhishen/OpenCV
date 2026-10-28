import cv2
import numpy as np

img = cv2.imread("tb.png")

# 图的减法运算就是矩阵的减法
img2 = np.zeros_like(img)
img2[:, :, 0] = 50
img3 = img - img2
cv2.imshow("img3", img3)


img3sub = np.zeros_like(img)
# 图的减法运算也可以用subtract函数
cv2.subtract(img, img2, img3sub)
cv2.imshow("img3sub", img3sub)


cv2.waitKey(0)
cv2.destroyAllWindows()