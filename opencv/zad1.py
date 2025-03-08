import cv2
import numpy as np

w = 300
h = 300
canvas = np.zeros((h, w, 3), dtype="uint8")

cv2.line(canvas, (h // 2, w // 2), (h, w), (255, 0, 0), 2)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
