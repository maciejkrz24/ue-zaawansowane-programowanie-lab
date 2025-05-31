import cv2

img = cv2.imread("img.png")

(B, G, R) = cv2.split(img)

cv2.imshow("Red", R)
cv2.imwrite("red.png", R)

cv2.imshow("Green", G)
cv2.imwrite("green.png", G)

cv2.imshow("Blue", B)
cv2.imwrite("blue.png", B)

cv2.waitKey(0)
cv2.destroyAllWindows()
