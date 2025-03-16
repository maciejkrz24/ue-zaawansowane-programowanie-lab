import cv2

image = cv2.imread("img.png")
cv2.imshow("Oryginal", image)

resized = cv2.resize(image, (200, 300))

cv2.imshow("Powiekszone", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
