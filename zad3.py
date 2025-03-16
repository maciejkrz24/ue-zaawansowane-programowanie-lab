import cv2

fname = "img.jpg"
image = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

if image is None:
    print(f"ERROR: Image `{fname}` was not found!")
    exit(1)

h, w, c = image.shape[:3]

print(f"Loaded image `{fname}` in grayscale")
print(f" > Image width:    {w}")
print(f" > Image height:   {h}")
print(f" > Color channels: {c}")

# cv2.imshow(f"Image {fname}", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
