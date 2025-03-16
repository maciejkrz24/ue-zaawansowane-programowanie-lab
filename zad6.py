import cv2

image = cv2.imread("img.jpg")

(h, w, _) = image.shape[:3]

cx = w // 2
cy = h // 2

square_size = 100

image[cy - square_size : cy + square_size, cx - square_size : cx + square_size] = (
    0,
    0,
    255,
)

cv2.imshow("Obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
