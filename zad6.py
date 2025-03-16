import cv2

image = cv2.imread("img.png")

flip = int(input("Jak odbić obraz? "))

image = cv2.flip(image, flip)

cv2.imshow("Obraz", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
