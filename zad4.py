import cv2

img = cv2.imread("tecza.png")

(B, G, R) = cv2.split(img)

B = cv2.add(B, 60)

new_image = cv2.merge([B, G, R])

cv2.imshow("Oryginal", img)
cv2.imshow("Wzmocnione B", new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
