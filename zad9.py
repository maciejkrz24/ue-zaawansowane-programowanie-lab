import cv2
import numpy as np

img = cv2.imread("img.png")
roi = img[100:400, 100:400]
cv2.imwrite("new_img.png", roi)
