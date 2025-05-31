import cv2
import imutils


def contours(image_path, widths):
    img = cv2.imread(image_path)

    for w in widths:
        resized = imutils.resize(img, width=w)
        r = img.shape[0] / float(resized.shape[0])

        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

        contours = cv2.findContours(
            thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
        )
        contours = imutils.grab_contours(contours)

        out = img.copy()

        for c in contours:
            c = c.astype("float")
            c *= r
            c = c.astype("int")
            cv2.drawContours(out, [c], -1, (0, 0, 255), 2)

        cv2.imshow(f"Szerokosc obrazu = {w}px, liczba konturow = {len(contours)})", out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


fname = "kostka.png"
widths = [i for i in range(100, 800, 100)]

contours(fname, widths)
