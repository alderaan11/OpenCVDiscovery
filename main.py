import numpy as np
import cv2


img = cv2.imread("salomon-shoes.jpg",0)
img2 = cv2.imread("salomon-shoes.jpg")

#cv2.imshow('image', img)
#cv2.imshow('image2', img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite("salomon-shoesG.jpg", img)
