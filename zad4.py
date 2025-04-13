import cv2
import numpy as np

img = cv2.imread("img.png")

startx = int(input("start x: "))
endx = int(input("end x: "))
starty = int(input("start y: "))
endy = int(input("end y: "))

roi = img[starty:endy, startx:endx]

cv2.imshow("ROI", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
