import cv2

fname1 = "img.jpg"
fname2 = "img2.png"
image1 = cv2.imread(fname1)
image2 = cv2.imread(fname2)

if image1 is None:
    print(f"ERROR: Image `{fname1}` was not found!")
    exit(1)

if image2 is None:
    print(f"ERROR: Image `{fname2}` was not found!")
    exit(1)

print(f"Loaded image `{fname1}` and `{fname2}`")

cv2.imshow(f"Image {fname1}", image1)
cv2.imshow(f"Image {fname2}", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
