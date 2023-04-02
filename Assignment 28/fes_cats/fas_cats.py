import cv2
cat_cascade =cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalcatface.xml")
img = cv2.imread('input/cats.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cats = cat_cascade.detectMultiScale(gray,1.1,5)
for x, y, w, h in cats:
    # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print(x,y,w,h)
# cv2.imshow('Cat Detection', img)
# cv2.waitKey(0)
cv2.destroyAllWindows()
