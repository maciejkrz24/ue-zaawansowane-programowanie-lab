import cv2

fname = "profilowe.jpg"
image = cv2.imread(fname)

if image is None:
    print(f"ERROR: Image `{fname}` was not found!")
    exit(1)

eye_l = (100, 100)
eye_r = (152, 100)

lips_top_l = (100, 155)
lips_bot_r = (150, 160)

face_center = (128, 100)

cv2.circle(image, eye_l, 5, (0, 0, 255), -1)
cv2.circle(image, eye_r, 5, (0, 0, 255), -1)

cv2.rectangle(image, lips_top_l, lips_bot_r, (0, 255, 0), -1)

cv2.circle(image, face_center, 90, (255, 0, 0), 5)

cv2.imshow(f"Image {fname}", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
