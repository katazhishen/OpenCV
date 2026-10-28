import cv2
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a.shape)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(b.shape)

c = np.zeros((2, 3, 3), np.uint8)
print(c)
print(c.shape)  

d = np.ones((2, 3, 3), np.uint8)
print(d)
print(d.shape)  

# 定义full矩阵
e = np.full((2, 3, 3), 255, np.uint8)
print(e)
print(e.shape)  

f = np.identity(3, np.uint8)
print(f)
print(f.shape)

g = np.eye(3, 4, k = 1, dtype = np.uint8)
print(g)
print(g.shape)
