import cv2
import numpy as np

img = cv2.imread("autko.jpg")

mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (157, 51), (838, 671), 255, -1)

masked = cv2.bitwise_and(img, img, mask=mask)

(B, G, R) = cv2.split(img)
(B_m, _, _) = cv2.split(masked)
B_m[B_m != 0] = 40

B = cv2.add(B, B_m)
new_img = cv2.merge([B, G, R])

cv2.imshow("Oryginal", img)
cv2.imshow("Maska", masked)
cv2.imshow("Wzmocniony kanal B", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
