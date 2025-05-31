import cv2
import numpy as np

image = cv2.imread("img.jpg")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (266, 87), 40, 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginal", image)
cv2.imshow("Zdjecie z maska", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
