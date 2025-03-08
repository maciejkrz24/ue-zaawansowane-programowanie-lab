import cv2

image = cv2.imread("img.jpg")

pixel = image[0, 0]
b, g, r = pixel

print(f"Wartości piksela w [0,0]: R: {r}, G: {g}, B: {b}")
