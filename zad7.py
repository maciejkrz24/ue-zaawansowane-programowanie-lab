import cv2
import imutils

image = cv2.imread("img.png")

rotated_imutils = imutils.rotate(image, 60)

cv2.imshow("Obrocone (imutils)", rotated_imutils)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), -60, 1.0)
rotated_cv2 = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Obrocone (opencv)", rotated_cv2)

cv2.waitKey(0)
cv2.destroyAllWindows()
