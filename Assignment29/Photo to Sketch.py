import cv2
image = cv2.imread("input/Photo to Sketch/IMG_20220702_175115.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

inverted = 255-image
blered = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blured = 255-blered
sketch = image/inverted_blured
sketch = sketch*255.0
cv2.imwrite("output/result_skerch.jpg",sketch)
