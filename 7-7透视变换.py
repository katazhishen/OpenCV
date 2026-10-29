import cv2
import numpy as np

img = cv2.imread("ts.png")

h, w, ch = img.shape


src = np.float32([[262, 443], [2666, 372],
                    [282, 3600], [2444, 2900]])
dst = np.float32([[0, 0], [480, 0], 
                    [0, 640], [480, 640]])
# 透视变换矩阵 三点对应关系
M = cv2.getPerspectiveTransform(src, dst)
# 透视变换
# 如果想改变新图像的尺寸，需要修改dsize
img2 = cv2.warpPerspective(img, M, (480, 640))
img2 = cv2.resize(img2, (480, 640))
cv2.imshow("7-7perspective", img2)

while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()