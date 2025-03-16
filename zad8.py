import cv2
import imutils

image = cv2.imread("img.png")

rotated_imutils_seq = imutils.rotate(image, 30)
rotated_imutils_seq = imutils.rotate(rotated_imutils_seq, 30)
rotated_imutils_seq = imutils.rotate(rotated_imutils_seq, 30)

rotated_imutils_imm = imutils.rotate(image, 90)

cv2.imshow("Obrocone (imutils, sekwencyjnie)", rotated_imutils_seq)
cv2.imshow("Obrocone (imutils, pojedynczo)", rotated_imutils_imm)

cv2.waitKey(0)
cv2.destroyAllWindows()

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), -30, 1.0)
M_imm = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated_cv2_seq = cv2.warpAffine(image, M, (w, h))
rotated_cv2_seq = cv2.warpAffine(rotated_cv2_seq, M, (w, h))
rotated_cv2_seq = cv2.warpAffine(rotated_cv2_seq, M, (w, h))

rotated_cv2_imm = cv2.warpAffine(image, M_imm, (w, h))

cv2.imshow("Obrocone (opencv, sekwencyjnie)", rotated_cv2_seq)
cv2.imshow("Obrocone (opencv, pojedynczo)", rotated_cv2_imm)

cv2.waitKey(0)
cv2.destroyAllWindows()
