import cv2
import imutils

image = cv2.imread("img.png")

for i in range(0, 360, 15):
    image = imutils.rotate(image, 15)
    cv2.imshow("Obrocone (imutils, pojedynczo)", image)
    cv2.waitKey(500)

cv2.waitKey(0)
cv2.destroyAllWindows()
