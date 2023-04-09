import cv2
import numpy as np

img_1 = cv2.imread("input/Virtual decoration/3.png")
img_2 = cv2.imread("input/Virtual decoration/2.webp")
img_3 = cv2.imread("input/Virtual decoration/3.png")

img_1 = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
img_2 = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
img_3 = cv2.cvtColor(img_3,cv2.COLOR_BGR2GRAY)
img_2= img_2/255
result = img_2*img_1
# result = cv2.multiply(img_1,img_3)
cv2.imwrite("output/Virtual_decoration.jpg",result)
