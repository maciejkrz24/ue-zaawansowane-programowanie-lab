import cv2

img1 = cv2.imread("img1.png")
cv2.imshow("Zdjecie 1", img1)

img2 = cv2.imread("img2.png")
cv2.imshow("Zdjecie 2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

img_xor = cv2.bitwise_xor(img1, img2)
cv2.imshow("XOR", img_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
