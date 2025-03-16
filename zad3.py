import cv2
import numpy as np

w = 300
h = 300
canvas = np.zeros((h, w, 3), dtype="uint8")

r1 = 40
r2 = 60
cv2.circle(canvas, (r1, r1), r1, (255, 0, 0))
cv2.circle(canvas, (h // 2, w // 2), r2, (0, 0, 255))

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
