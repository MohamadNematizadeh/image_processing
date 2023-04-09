import cv2
import numpy as np


img_1 = cv2.imread("input/Face Morphing/Trump.jpg")
img_2= cv2.imread("input/Face Morphing/Trump2.jpg")

# img_1 = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
# img_2 = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)

# img_1 = img_1.astype(np.float32)
# img_2= img_2.astype(np.float32)
# result=img_1img_2
# result = result.astype(np.uint8)

cv2.imwrite("output/result2.jpg",img_1)