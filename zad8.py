import cv2

image = cv2.imread("img.jpg")
cv2.imshow("Obraz przed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

(h, w, _) = image.shape[:3]

image[100, 0:w] = (0, 255, 0)

cv2.imshow("Obraz po", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
