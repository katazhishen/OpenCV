import cv2
import numpy as np

img = cv2.imread("tb.png")
h, w, ch = img.shape

# 仿射变换矩阵 原点为中心旋转 30度 缩放比例为0.6
M = cv2.getRotationMatrix2D((w/2,h/2),30,0.6)
# 仿射变换
# 如果想改变新图像的尺寸，需要修改dsize
img2 = cv2.warpAffine(img, M, (int(w*0.5), int(h*0.5)))
cv2.imshow("7-5affine", img2)

while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()