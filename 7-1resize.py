import cv2
import numpy as np

img = cv2.imread("tb.png")

h, w = img.shape[:2]
scale = 0.25
img = cv2.resize(img, (int(w * scale), int(h * scale)))
cv2.imshow("7-1resize", img)

cv2.waitKey(0)
cv2.destroyAllWindows()