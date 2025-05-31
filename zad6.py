import cv2
import numpy as np

img = cv2.imread("opencv.png")

(B, G, R) = cv2.split(img)

swapped = cv2.merge([G, R, B])
no_red = cv2.merge([B, G, np.zeros_like(R)])

cv2.imshow("Oryginal", img)
cv2.imshow("Zamienione kanaly", swapped)
cv2.imshow("Bez czerwonego", no_red)

cv2.waitKey(0)
cv2.destroyAllWindows()
