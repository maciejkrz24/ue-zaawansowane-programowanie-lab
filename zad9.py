import cv2

image = cv2.imread("img.png")

for i in range(100, 300, 20):
    w = int(image.shape[1] * (i / 100))
    h = int(image.shape[0] * (i / 100))

    image = cv2.resize(image, (w, h))
    cv2.imshow(f"{i}% powiekszenie", image)

    cv2.waitKey(500)
    cv2.destroyAllWindows()
