import cv2

metody = {
    "INTER_CUBIC": cv2.INTER_CUBIC,
    "INTER_LANCZOS4": cv2.INTER_LANCZOS4,
}

image = cv2.imread("img.png")

w = image.shape[1] * 4
h = image.shape[0] * 4

for nazwa, metoda in metody.items():
    resized = cv2.resize(image, (w, h), interpolation=metoda)
    cv2.imshow(f"4-krotne powiekszenie, metoda: {nazwa}", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
