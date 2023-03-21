import cv2
imgs = cv2.imread("spaces_u9ESMkINnUK9Z0nC4FPH_uploads_n1fj3dyqbjER3SLYexIW_1.webp", 0)

treshold = 180
height, width = imgs.shape
for i in range(height):
    for j in range(width):
        imgs[i, j] = 255 - imgs[i, j]

imgs =cv2.resize(imgs,(400, 400))
cv2.imshow("output", imgs)
cv2.waitKey()
cv2.imwrite("1.jpg",imgs)