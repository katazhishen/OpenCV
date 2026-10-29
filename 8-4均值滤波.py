import cv2
import numpy as np

img = cv2.imread("tb.png")

h, w, ch = img.shape

kernel = np.ones((5, 5), np.uint8) / 25



dst = cv2.blur(img, (5, 5))

cv2.imshow("8-4卷积0", img)
cv2.imshow("8-4卷积", dst)


while cv2.waitKey(1) != ord("q") and cv2.waitKey(1) != ord("Q"):
    pass


cv2.destroyAllWindows()