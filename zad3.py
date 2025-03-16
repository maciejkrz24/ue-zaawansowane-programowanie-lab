import cv2, imutils

image = cv2.imread("img.png")

cv2.imshow("Oryginal", image)

(h, w) = image.shape[:2]

M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Obrot o 30 stopni wokol naroznika", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
