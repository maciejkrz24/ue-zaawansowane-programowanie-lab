import cv2
import numpy as np

img = cv2.imread("img.png")

added_cv2 = cv2.add(img, np.ones(img.shape, dtype="uint8") * 150)
added_np = img + np.ones(img.shape, dtype="uint8") * 150

cv2.imshow("original", img)
cv2.imshow("cv2 add", added_cv2)
cv2.imshow("np add", added_np)
cv2.waitKey(0)
cv2.destroyAllWindows()
