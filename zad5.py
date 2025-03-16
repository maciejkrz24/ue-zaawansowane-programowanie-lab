import cv2

image = cv2.imread("img.jpg")

(h, w, _) = image.shape[:3]
image[0 : h // 2, 0 : w // 2] = (255, 0, 0)

cv2.imshow("Obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
