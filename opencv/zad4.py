import cv2

fname = "img.jpg"
image = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"ERROR: Image `{fname}` was not found!")
    exit(1)

print(f"Loaded image `{fname}` in grayscale")

cv2.imwrite("grayscale_" + fname, image)
