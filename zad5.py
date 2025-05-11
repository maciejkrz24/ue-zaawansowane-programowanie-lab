import cv2
import numpy as np

img = cv2.imread("img.png")
b, g, r = cv2.split(img)

filtered = cv2.merge([cv2.add(b, 10), cv2.subtract(g, 20), cv2.add(r, 30)])

cv2.imshow("original", img)
cv2.imshow("filtered", filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
