import cv2
import numpy as np

img = cv2.imread("tb.png")
h, w, ch = img.shape


src = np.float32([[400, 300], [800, 300], [400, 1000]])
dst = np.float32([[200, 400], [600, 500], [150, 1100]])
# 仿射变换矩阵 三点对应关系
M = cv2.getAffineTransform(src, dst)
# 仿射变换
# 如果想改变新图像的尺寸，需要修改dsize
img2 = cv2.warpAffine(img, M, (int(w*0.8), int(h*0.8)))
cv2.imshow("7-6affine", img2)

while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()