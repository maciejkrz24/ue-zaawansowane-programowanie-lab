import cv2
from time import sleep

image = cv2.imread("img.png")

NOWA_SZEROKOSC = 500

r = NOWA_SZEROKOSC / image.shape[1]
dim = (NOWA_SZEROKOSC, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

print(
    "UWAGA: zdjęcie już jest kwadratem, więc nie widać pożądanego efektu...\n(sleep na 3 sekundy)"
)
sleep(3)

cv2.imshow("Zmieniona wielkosc z zachowaniem proporcji", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
