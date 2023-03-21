import numpy as np
import cv2

first_name = np.zeros((600, 600), np.uint8)
first_name [:,:] = 0

first_name[150:400] = 255

first_name[180:360 , 110:160] = 0
first_name[180:200,160:210] = 0
first_name[180:200,160:180]= 0

first_name[200:220,180:230]= 0

first_name[200:300,200:230]= 0

first_name[280:330,220:280]= 0

first_name[200:300,280:310]= 0

first_name[200:220,300:330]= 0
first_name[180:200,300:390] = 0
first_name[180:360,350:390] = 0


cv2.imwrite('first_name.jpg', first_name)

cv2.imshow('first_name', first_name)
cv2.waitKey()

   