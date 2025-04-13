import cv2
import numpy as np

img = cv2.imread("img.png")
h = img.shape[0]
w = img.shape[1]

roi_width = 20

for x in range(0, w // roi_width):
    roi = img[:, x * roi_width : (x + 1) * roi_width]
    cv2.imshow(f"ROI x={x}", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
