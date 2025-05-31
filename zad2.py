import cv2
import imutils


img = cv2.imread("kostka.png")
resized = imutils.resize(img, width=300)
ratio = img.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)[1]

modes = [
    cv2.RETR_EXTERNAL,
    cv2.RETR_TREE,
    cv2.RETR_LIST,
]

for m in modes:
    tmp = img
    contours = cv2.findContours(thresh.copy(), m, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    for c in contours:
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.drawContours(tmp, [c], -1, (0, 0, 255), 2)

    cv2.imshow(f"Zdjecie, tryb={str(m)}", tmp)

cv2.waitKey(0)
cv2.destroyAllWindows()
