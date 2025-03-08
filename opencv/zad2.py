import cv2
import numpy as np

w = 400
h = 400
canvas = np.zeros((h, w, 3), dtype="uint8")

cv2.rectangle(canvas, (0, 0), (100, 50), (0, 255, 0), -1)
cv2.rectangle(canvas, (h, w), (h - 100, w - 50), (0, 0, 255), 3)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
