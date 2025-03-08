import cv2

image = cv2.imread("img.jpg")

x = int(input("Podaj wspolrzedna X: "))
y = int(input("Podaj wspolrzedna Y: "))

(h, w, _) = image.shape[:3]

if x > w or y > h or x < 0 or y < 0:
    print("Niepoprawne współrzędne dla zdjęcia o rozmiarze {w}x{h}!")

image[y, x] = (0, 0, 0)

cv2.imshow("Obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
