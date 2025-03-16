import cv2

image = cv2.imread("img.png")

h = image.shape[1]
w = image.shape[0]

image[:, w // 2 : w] = cv2.flip(image[:, w // 2 : w], 1)

cv2.imshow("Obraz", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
