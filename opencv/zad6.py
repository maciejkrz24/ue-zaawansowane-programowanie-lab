import cv2

fname = "img.jpg"
image = cv2.imread(fname)

if image is None:
    print(f"ERROR: Image `{fname}` was not found!")
    exit(1)

cv2.namedWindow(f"Image {fname}", cv2.WINDOW_NORMAL)
cv2.imshow(f"Image {fname}", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
