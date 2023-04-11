
import cv2
import numpy as np

image_Obama= cv2.imread("input/Face Morphing/Obama.jpg")
image_Joe_Biden =cv2.imread("input/Face Morphing/Joe_Biden.jpg")
image_Joe_Biden = image_Joe_Biden[10:,:,:]
w, h, _ = image_Joe_Biden.shape
image_Obama = cv2.resize(image_Obama, [h, w])

image_Obama = image_Obama.astype(np.float32)
image_Joe_Biden = image_Joe_Biden.astype(np.float32)

image_Joe_Biden_robert1 = image_Obama*.25 + image_Joe_Biden*.75
image_Joe_Biden_robert2 = image_Obama*.5 + image_Joe_Biden*.5
image_Joe_Biden_robert3 = image_Obama*.75 + image_Joe_Biden*.25

image_Joe_Biden_robert1 = image_Joe_Biden_robert1.astype(np.uint8)
image_Joe_Biden_robert2 = image_Joe_Biden_robert2.astype(np.uint8)
image_Joe_Biden_robert3 = image_Joe_Biden_robert3.astype(np.uint8)

image_Joe_Biden_robert = np.concatenate((image_Joe_Biden, image_Joe_Biden_robert1, image_Joe_Biden_robert2,
 image_Joe_Biden_robert3, image_Obama), axis=1)

cv2.imwrite('output/image_Obama_and_Joe_Biden.jpg',image_Joe_Biden_robert)
