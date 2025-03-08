import cv2

image = cv2.imread("img.jpg")

(h, w, _) = image.shape[:3]

part_w = w // 3
part_h = h // 3

center = image[part_h : 2 * part_h, part_w : 2 * part_w]

cv2.imshow("Obraz", center)
cv2.waitKey(0)
cv2.destroyAllWindows()
