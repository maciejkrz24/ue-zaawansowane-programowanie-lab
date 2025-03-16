import cv2

image = cv2.imread("img.png")
flipped_h = cv2.flip(image, 1)
flipped_v = cv2.flip(image, 0)
flipped_b = cv2.flip(image, -1)

cv2.imshow("Oryginal", image)
cv2.imshow("Odbicie poziome", flipped_h)
cv2.imshow("Odbicie pionowe", flipped_v)
cv2.imshow("Odbicie w. obu osi", flipped_b)

cv2.waitKey(0)
cv2.destroyAllWindows()
