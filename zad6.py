import cv2
import numpy as np

img = cv2.imread("img.png")

img[100:300, 300:500] = img[100:300, 100:300]

cv2.imshow("IMG", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
