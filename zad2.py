import cv2
import numpy as np

fname = "img.png"
image = cv2.imread(fname)

if image is None:
    print(f"ERROR: Image `{fname}` was not found!")
    exit(1)

cv2.imshow("Oryginal", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

M = np.float32([[1, 0, -20], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Przesuniety", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
