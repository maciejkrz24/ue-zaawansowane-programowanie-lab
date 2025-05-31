import cv2
import imutils


img = cv2.imread("kostka.png")
resized = imutils.resize(img, width=300)
ratio = img.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

for c in contours:
    c = (c * ratio).astype("int")
    x, y, w, h = cv2.boundingRect(c)

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    label = f"{w} x {h}px"
    cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

cv2.imshow("Wymiary", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
