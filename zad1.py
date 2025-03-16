import cv2

image = cv2.imread("img.png")
flipped = cv2.flip(image, 1)

cv2.imshow("Oryginal", image)
cv2.imshow("Odbicie poziome", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
