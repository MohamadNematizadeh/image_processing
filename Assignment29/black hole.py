import cv2
import numpy as np
images = [[0 for i in range(5)] for j in range(4)]
for i in range(4):
    for j in range(5):
        images[i][j] = cv2.imread(f"input/{i+1}/{j+1}.jpg",0)
        images[i][j] = cv2.resize(images[i][j], (400, 400))
image_without_noise = [0 for i in range(4)]
for i in range(4):
    for j in range(5):
        image_without_noise[i] += (images[i][j] // 5)
result = np.zeros((800, 800), dtype= np.uint8)
result[0:400, 0:400] = image_without_noise[0]
result[0:400, 400:800] = image_without_noise[1]
result[400:800, 0:400] = image_without_noise[2]
result[400:800, 400:800] = image_without_noise[3]
cv2.imwrite("output/result_Black_Hole.jpg",result)
