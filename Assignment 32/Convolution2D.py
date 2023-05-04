import cv2
import numpy as np

input_image = cv2.imread("input/1.tif")
# 1. Edge detection filter
original = np.array([[0 , -1 , -1],
                   [0 ,  8 , -1],
                   [0 , -1 , -1]])
# # 2. Sharpening filter
Ayg_kemel_1_0 = np.array([[4  , 4 ,  4],
                   [4 ,  5 , 4],
                   [4  , 4 ,  4]])
# # 2. Emboss filter
Ayg_kemel_3 = np.array([[2 , 2 ,  2],
                   [2,  2 ,  2],
                   [2  ,  2 ,  2]])
# # 4. Identity filter
Ayg_kemel = np.array([[5  ,  5 ,  5],
                   [5  ,  5 ,  5],
                   [5  ,  5 ,  5]])

outpute_imag=cv2.filter2D(input_image,-1,original)

outpute_imag_2=cv2.filter2D(input_image,-1,Ayg_kemel_1_0)

outpute_imag_3=cv2.filter2D(input_image,-1,Ayg_kemel_3)

outpute_imag_4=cv2.filter2D(input_image,-1,Ayg_kemel)

res = np.hstack((input_image,outpute_imag,outpute_imag_2,outpute_imag_3,outpute_imag_4))

cv2.imwrite("output/The Magic.jpg",res)

