import cv2
import numpy as np

img = cv2.imread("tecza.png")

(B, G, R) = cv2.split(img)

swapped_channels = cv2.merge([B, R, G])
zeroed_channel = cv2.merge([B, np.zeros(G.shape, dtype=G.dtype), R])

cv2.imshow("Oryginal", img)
cv2.imshow("Zamienione kanaly", swapped_channels)
cv2.imshow("Wyzerowany kanal G", zeroed_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()
