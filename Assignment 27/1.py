import cv2

img = cv2.imread('input/bat.jpg' , 0)
height , width = img.shape
_, img=cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow('', img)
cv2.imwrite('output/snowy_wolf.jpg' , img)
cv2.waitKey()
