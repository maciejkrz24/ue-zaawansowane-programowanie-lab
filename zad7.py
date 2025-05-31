import cv2
import imutils
import numpy as np


img = cv2.imread("kostka.png")
resized = imutils.resize(img, width=300)
ratio = img.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

widths = []
heights = []

for c in contours:
    c = (c * ratio).astype("int")
    x, y, w, h = cv2.boundingRect(c)
    widths.append(w)
    heights.append(h)

print(f"Liczba wykrytych kostek: {len(contours)}")
print(f"Srednia szerokosc: {np.mean(widths):.2f}px, wysokosc: {np.mean(heights):.2f}px")
print(
    f"Min. rozmiar: {min(widths)}x{min(heights)}px,\nMax: {max(widths)}x{max(heights)}px"
)
