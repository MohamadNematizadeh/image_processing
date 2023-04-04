import cv2
import numpy as np

img=np.zeros((500, 700, 3), np.uint8)
# Football field image
for i in range(7):
    if i%2==1:
        cv2.rectangle(img, (100*i, 0), (100*(i+2), 500), (0,129,0), -1)
    if i%2!=1 :
        cv2.rectangle(img, (100*i, 0), (100*(i+1), 500), (0,204,0), -1)

# The rectangle of the football field
cv2.line(img, (350, 20), (350, 480), (255, 255, 255), 2)
cv2.rectangle(img, (20, 20), (680, 480), (255, 255, 255), 2)
# football gates
cv2.rectangle(img, (20, 190), (80, 325), (255, 255, 255), 2)
cv2.rectangle(img, (620, 190), (680, 325), (255, 255, 255), 2)
cv2.rectangle(img, (20, 135), (140, 380), (255, 255, 255), 2)
cv2.rectangle(img, (560, 135), (680, 380), (255, 255, 255), 2)
# Soccer ball
cv2.circle(img, (350, 250), 80, (255, 255, 255), 2)
cv2.circle(img, (350, 250), 7, (255, 255, 255), -1)
cv2.imwrite("football pitch.png", img)

cv2.imshow("soccer img", img)
cv2.waitKey()

