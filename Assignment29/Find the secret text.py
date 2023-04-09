import cv2
img1 = cv2.imread("input/Find the secret text/1.webp",0)
img2 = cv2.imread("input/Find the secret text/2.webp", 0)
result = img2 - img1
cv2.imwrite("output/Find_the_secret_text.jpg", result)

