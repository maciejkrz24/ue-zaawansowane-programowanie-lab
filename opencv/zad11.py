import cv2

image = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)

h, w = image.shape[:3]

max = 0
max_coords = (0, 0)

for y in range(h):
    for x in range(w):
        pixel = image[y, x]
        if pixel > max:
            max = pixel
            max_coords = (x, y)

mx, my = max_coords
print(f"Najjaśniejszy pixel ({max}) na pozycji x={mx}, y={my}")
