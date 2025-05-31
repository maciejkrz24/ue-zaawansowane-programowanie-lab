import cv2
import imutils


img = cv2.imread("kostka.png")
resized = imutils.resize(img, width=300)
ratio = img.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

contours_filtered = [c for c in contours if 500 < cv2.contourArea(c) < 5000]
clone = img.copy()
for c in contours_filtered:
    c = (c * ratio).astype("int")
    cv2.drawContours(clone, [c], -1, (255, 0, 0), 2)

cv2.imshow("Kontury o powierzchni 500..5000", clone)
cv2.waitKey(0)
cv2.destroyAllWindows()
