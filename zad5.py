import cv2
import imutils

image = cv2.imread("img.png")

rotated = imutils.rotate(image, 180)

cv2.imshow("Obrocone", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
