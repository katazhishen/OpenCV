import cv2
import numpy as np

img = cv2.imread("tb.png")
# h, w
#kernel = np.ones((3, 3), np.uint8)

# 自动生成矩阵
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dst = cv2.erode(img, kernel, iterations=3)
print(kernel)
cv2.imshow("9-6腐蚀2原图", img)
cv2.imshow("9-6腐蚀2", dst)

while cv2.waitKey(1) != ord("q"):
    pass

cv2.destroyAllWindows()