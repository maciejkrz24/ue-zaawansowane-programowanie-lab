import cv2
import numpy as np

w = 300
h = 300
canvas = np.zeros((h, w, 3), dtype="uint8")

cv2.rectangle(
    canvas, (h // 2 - 50, w // 2 - 50), (h // 2 + 50, w // 2 + 50), (180, 24, 24), -1
)
cv2.circle(canvas, (h // 2, w // 2), 30, (24, 10, 220), -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
