import cv2
import numpy as np

img = cv2.imread("img.png")
sub_img_h = img.shape[0] // 3
sub_img_w = img.shape[1] // 3

for y in range(0, 3):
    for x in range(0, 3):
        roi = img[
            y * sub_img_h : (y + 1) * sub_img_h, x * sub_img_w : (x + 1) * sub_img_w
        ]
        cv2.imshow(f"ROI y={y} x={x}", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
