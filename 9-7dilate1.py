import cv2
import numpy as np

img = cv2.imread("tb.png")
# h, w
#kernel = np.ones((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dst = cv2.dilate(img, kernel, iterations=1)

print(kernel)
cv2.imshow("9-7dilate1原图", img)
cv2.imshow("9-7dilate1", dst)

while cv2.waitKey(1) != ord("q"):
    pass

cv2.destroyAllWindows()