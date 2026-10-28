import cv2
import numpy as np

img = np.zeros((480,640,3), np.uint8)


print(img[100,100])
img[100:200,100:200] = [255,255,0]   


cv2.imshow('4-5testnumpy', img)

while cv2.waitKey(1) & 0xFF != ord("q"):
    pass


cv2.destroyAllWindows()