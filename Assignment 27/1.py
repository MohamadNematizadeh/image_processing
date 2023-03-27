import cv2

img = cv2.imread('input/bat.jpg' , 0)
height , width = img.shape
_, img=cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
cv2.putText(img, 'BATMAN', (300, 550), cv2.FONT_HERSHEY_SIMPLEX, 3, 255, thickness= 5)
cv2.imshow('', img)
cv2.imwrite('output/snowy_wolf.jpg' , img)
cv2.waitKey()
