import cv2
import numpy as np
img = np.arange(0,9,9,np.uint8)
img = np.resize(img,(250,250))
width,hight=img.shape
for i in range(hight):
    for j in range(width):
        img[i-j]=j-0
cv2.imshow("Generate", img)
cv2.waitKey()
cv2.imwrite("Generate.jpg",img)