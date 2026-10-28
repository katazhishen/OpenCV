import cv2
import numpy as np

img = np.zeros((480, 640, 3), np.uint8)
# 多边形顶点
pts = np.array([[400, 100], [200, 300], [300, 100]], np.int32)

# 绘制多边形
cv2.polylines(img, [pts], True, (0, 255, 0), 3)
# 填充多边形
cv2.fillPoly(img, [pts], (0, 255, 0))

# 添加文本
cv2.putText(img, "Hello World!", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

cv2.imshow("5-4polylines", img)
while cv2.waitKey(1) != ord("q"):
    pass
cv2.destroyAllWindows()