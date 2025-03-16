import cv2

metody = {
    "INTER_AREA": cv2.INTER_AREA,
    "INTER_NEAREST": cv2.INTER_NEAREST,
    "INTER_LINEAR": cv2.INTER_LINEAR,
    "INTER_CUBIC": cv2.INTER_CUBIC,
    "INTER_LANCZOS4": cv2.INTER_LANCZOS4,
}

image = cv2.imread("img.png")

w = image.shape[1] // 5
h = image.shape[0] // 5

for nazwa, metoda in metody.items():
    resized = cv2.resize(image, (w, h), interpolation=metoda)
    cv2.imshow(f"5-krotne pomniejszenie, metoda: {nazwa}", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
