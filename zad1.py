import cv2
import numpy as np

img = cv2.imread("img.png")
roi = img[0:100, 0:100]

cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
