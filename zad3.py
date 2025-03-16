import cv2

image = cv2.imread("img.jpg")

(h, w, _) = image.shape[:3]
b, g, r = image[h // 2, w // 2]

print(f"Wartości piksela w [x={w//2},y={h//2}]: R: {r}, G: {g}, B: {b}")
