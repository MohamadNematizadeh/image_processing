import cv2
import numpy as np
images = []
for i in range(0,5):
    img = cv2.imread(f"input/img_crs/{i}.png", 0)
    img = cv2.resize(img, (640, 360))
    images.append(img)
    rows,cols= img.shape

result = np.zeros((rows, cols), dtype="uint8")
for image in images:
    result += image // 10
cv2.imwrite("output/Background_estimation.jpg",result)
