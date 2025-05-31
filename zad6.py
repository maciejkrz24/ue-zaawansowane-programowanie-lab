# Przetestuj odporność algorytmu na "fałszywe trafienia".
# a Wczytaj obraz z wieloma podobnymi obiektami (np. klocki LEGO,
# opakowania).
# b Wytnij jeden jako szablon.
# c Spróbuj wykryć jego wystąpienia.
# d Czy pojawiły się błędne detekcje? Jak to wyeliminować?

import cv2

img = cv2.imread("pliki.png")
template = cv2.imread("ikonka_2.png")

imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = zip(*((result >= threshold).nonzero()[::-1]))

for pt in loc:
    cv2.rectangle(
        img,
        pt,
        (pt[0] + template.shape[1], pt[1] + template.shape[0]),
        (0, 255, 0),
        2,
    )

cv2.imshow("Dopasowania", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
