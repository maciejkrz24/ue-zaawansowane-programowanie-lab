import numpy as np
import cv2

img = np.zeros((256, 256), dtype="uint8")
p1 = (20, 20)
p2 = (120, 200)
p3 = (200, 20)
triangle = np.array([p1, p2, p3])
cv2.drawContours(img, [triangle], 0, (255, 255, 255), -1)
cv2.imshow("Trojkat", img)

circle_canvas = np.zeros((256, 256), dtype="uint8")
cv2.circle(circle_canvas, (150, 150), 60, 255, -1)
cv2.imshow("Kolo", circle_canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()

bitwiseAnd = cv2.bitwise_and(img, circle_canvas)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()

bitwiseOr = cv2.bitwise_or(img, circle_canvas)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)
cv2.destroyAllWindows()

bitwiseXor = cv2.bitwise_xor(img, circle_canvas)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)
cv2.destroyAllWindows()

bitwiseNot = cv2.bitwise_not(img)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)

cv2.destroyAllWindows()
