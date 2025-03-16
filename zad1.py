import cv2

image = cv2.imread("img.png")
cv2.imshow("Oryginal", image)

w = image.shape[1] // 2
h = image.shape[0] // 2

resized = cv2.resize(image, (w, h))

cv2.imshow("Zmniejszone", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
