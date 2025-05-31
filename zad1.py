import cv2
import imutils


img = cv2.imread("kostka.png")
img = imutils.resize(img, width=300)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Zdjecie", img)

for th in [100, 140, 180]:
    thresh = cv2.threshold(img, th, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow(f"Threshold = {th}", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
