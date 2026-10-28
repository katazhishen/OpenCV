import cv2
import numpy as np

img = cv2.imread("phi.jpg")
logo = cv2.imread("tb.png")

# 1. 先确定 ROI 位置和尺寸
x1, y1, x2, y2 = 1000, 1000, 1400, 1400
roi = img[y1:y2, x1:x2]
h, w = roi.shape[:2]

# 2. 把 logo 缩放到和 ROI 一样大（关键修复）
logo = cv2.resize(logo, (w, h))

# 3. 生成单通道 8 位二值掩码
mask = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
# 黑底照片：大于250变白→255，人物深色→0，得到前景掩码
_, mask_fg = cv2.threshold(mask, 250, 255, cv2.THRESH_BINARY_INV)
mask_bg = cv2.bitwise_not(mask_fg)   # 背景掩码，和前景正好相反


# 4. 分别抠出背景和前景，再相加
tmp = cv2.bitwise_and(roi, roi, mask=mask_bg)
logo = cv2.bitwise_and(logo, logo, mask=mask_fg)
dst = cv2.add(tmp, logo)

# 5. 把结果写回原图对应位置
img[y1:y2, x1:x2] = dst

while True:
    cv2.imshow("img", img)
    cv2.imshow("mask_fg", mask_fg)
    cv2.imshow("mask_bg", mask_bg)
    

    
    cv2.imshow("tmp", tmp)
    cv2.imshow("dst", dst)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
