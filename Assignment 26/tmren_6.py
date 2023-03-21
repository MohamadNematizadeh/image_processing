import cv2

img = cv2.imread("6.jpg", 0)

cv2.imwrite("result.jpg", img)
print(img.shape)
treshold = 120
height, width = img.shape

for i in range(250):
    if i <= 100:
        for j in range(100-i, 250-i):
            if j >= 0:
                img[i, j] = 0
    else:
        for j in range(0, 250-i):
            if j >= 0:
                img[i, j] = 0

img[560:60, 0:5] = 0
img[0:60, 501:5] = 0
img[0:4, 0:5] = 0

cv2.imshow("death symbol", img)
cv2.waitKey()
cv2.imwrite("death_symbol.jpg",img)