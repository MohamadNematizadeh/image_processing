import numpy as np 
import cv2
img= cv2.imread("input/image_noisy.png",0)
rows,cols =img.shape
result=np.zeros((rows,cols),dtype=np.uint8)
filter = np.ones((5,5))/25

for i in range(2,rows-2):
    for j in range(2,cols-2):
        small = img[i-2:i+3,j-2:j+3]
        average =np.sum(filter*small)
        result[i,j] = average
cv2.imwrite("output/noes_result.png", result)