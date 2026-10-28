import cv2
import numpy as np

img = cv2.imread("tb.png")

img2 = np.zeros_like(img)
img2[:, :, 0] = 50


img3 = cv2.addWeighted(img, 0.1, img2, 0.8, 0)
cv2.imshow("img3", img3)



cv2.waitKey(0)
cv2.destroyAllWindows()