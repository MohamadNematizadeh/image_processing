import cv2
import numpy as np

image = cv2.imread("input/noes3.png")

# result = np.zeros(image.shape)
# for i in range(1,image.shape[0]-1):
#     for j in range(1,image.shape[1]-1):
#         small =image[i-1:i+2,j-1:j+2]
#         sorted_array=np.sort(small,axis=None)
#         result[i,j]=sorted_array[4]

result =cv2.medianBlur(image,3)
cv2.imwrite("output/noes3.png",result)