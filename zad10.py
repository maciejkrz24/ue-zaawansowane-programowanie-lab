import cv2

image = cv2.imread("img.jpg")

b1, g1, r1 = image[50, 50]
b2, g2, r2 = image[200, 200]

print(f"Wartości piksela w [50,50]:   R: {r1}, G: {g1}, B: {b1}")
print(f"Wartości piksela w [200,200]: R: {r2}, G: {g2}, B: {b2}")

db = abs(b2 - b1)
dg = abs(g2 - g1)
dr = abs(r2 - r1)

print(f"Różnice w: R: {dr}, G: {dg}, B: {db}")
