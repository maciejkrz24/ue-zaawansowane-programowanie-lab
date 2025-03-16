import cv2
import imutils

fname = "img.png"
image = cv2.imread(fname)

w = image.shape[1]
h = image.shape[0]

if image is None:
    print(f"ERROR: Image `{fname}` was not found!")
    exit(1)

dx = input("Podaj przesuniecie w poziomie: ")
dy = input("Podaj przesuniecie w pionie: ")

cv2.imshow("Oryginal", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

shifted = imutils.translate(image, dx, dy)

cv2.imshow("Przesuniety", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
