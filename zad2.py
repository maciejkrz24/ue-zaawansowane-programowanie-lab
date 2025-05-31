import cv2
import numpy as np

image = cv2.imread("img.jpg")

mask = np.ones(image.shape[:2], dtype="uint8")

cv2.circle(mask, (253, 73), 7, 0, -1)
cv2.circle(mask, (286, 74), 7, 0, -1)

masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginal", image)
cv2.imshow("Zdjecie z maska", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
