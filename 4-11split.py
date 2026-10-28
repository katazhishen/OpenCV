import cv2
import numpy as np

img = cv2.imread("tb.png")

b,g,r = cv2.split(img)

"""
cv2.imshow("4-9mat", img)
cv2.imshow("4-9mat2", b)
cv2.imshow("4-9mat3", g)
cv2.imshow("4-9mat4", r)
"""


img2 = cv2.merge([b,g,r])

cv2.imshow("4-9mat5", img2)


cv2.waitKey(0)

cv2.destroyAllWindows()