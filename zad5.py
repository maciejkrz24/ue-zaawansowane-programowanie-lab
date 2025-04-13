import cv2
import numpy as np

img = cv2.imread("osoba.jpg")
roi = img[64:120, 240:294]

cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
