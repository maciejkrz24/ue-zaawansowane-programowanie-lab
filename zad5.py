import cv2


img = cv2.imread("pulpit.png")
template = cv2.imread("ikonka.png")
imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

startX, startY = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

cv2.rectangle(img, (startX, startY), (endX, endY), (255, 0, 0), 2)

cv2.imshow(f"Dopasowanie, maxVal={maxVal}", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
