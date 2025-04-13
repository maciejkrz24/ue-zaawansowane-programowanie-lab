import cv2
import numpy as np

img = cv2.imread("img.png")
middle = img.shape[0] // 2
roi = img[middle:, :]

cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
