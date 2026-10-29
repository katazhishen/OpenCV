import cv2
import numpy as np

img = cv2.imread("tb.png")
h, w, ch = img.shape


M = np.float32([[1, 0, 400], [0, 1, 100]])

# 仿射变换
img2 = cv2.warpAffine(img, M, (w, h))
cv2.imshow("7-4affine", img2)

while cv2.waitKey(1) != ord("q"):
    pass


cv2.destroyAllWindows()