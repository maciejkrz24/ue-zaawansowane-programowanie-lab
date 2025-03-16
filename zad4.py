import cv2
import numpy as np
import imutils

fname = "img.png"
image = cv2.imread(fname)

w = image.shape[1]
h = image.shape[0]

if image is None:
    print(f"ERROR: Image `{fname}` was not found!")
    exit(1)

cv2.imshow("Oryginal", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

M = np.float32([[1, 0, 0.75 * w], [0, 1, 0.75 * h]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Przesuniety - warpAffine()", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()

shifted_new = imutils.translate(image, 0.75 * w, 0.75 * h)

cv2.imshow("Przesuniety - translate()", shifted_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
