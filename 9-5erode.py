import cv2
import numpy as np

img = cv2.imread("tb.png")
# h, w
kernel = np.ones((3, 3), np.uint8)
dst = cv2.erode(img, kernel, iterations=3)

cv2.imshow("9-5erode原图", img)
cv2.imshow("9-5erode", dst)

while cv2.waitKey(1) != ord("q"):
    pass

cv2.destroyAllWindows()