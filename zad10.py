import cv2

image = cv2.imread("img.png")
h = image.shape[0]
image = cv2.resize(image, (800, h))

cv2.imwrite("resized_output.jpg", image)
