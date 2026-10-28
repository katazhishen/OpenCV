import cv2
import numpy as np  

img = cv2.imread("tb.png")

print(img.shape)

print(img.size)

print(img.dtype)

# 赋值宽高给w,h 
h, w = img.shape[:2]
print(w, h)
