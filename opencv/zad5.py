import cv2
import numpy as np

w = 300
h = 300
canvas = np.zeros((h, w, 3), dtype="uint8")


for size in range(0, 175, 20):
    cv2.rectangle(
        canvas,
        (h // 2 - size // 2, w // 2 - size // 2),
        (h // 2 + size // 2, w // 2 + size // 2),
        (24, 10, 220),
        -1,
    )
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
