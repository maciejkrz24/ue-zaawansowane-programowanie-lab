import cv2
import numpy as np

img = cv2.imread("img.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_bound = np.array([100, 40, 40])
upper_bound = np.array([200, 255, 255])

mask = cv2.inRange(hsv_img, lower_bound, upper_bound)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Oryginal", img)
cv2.imshow("Wynik", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
