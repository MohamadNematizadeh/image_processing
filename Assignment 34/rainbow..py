import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.zeros((800,1500,3), dtype = "uint8")
img =cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

red = cv2.ellipse(img,(750,750),(560,560),180,0,180,[0,0,255],-2)
orang = cv2.ellipse(img,(750,750),(490,490),180,0,180,[0,127,255],-2)

yellow = cv2.ellipse(img,(750,750),(420,420),180,0,180,[0,255,255],-2)
green = cv2.ellipse(img,(750,750),(350,350),180,0,180,[0,255,0],-2)
blue = cv2.ellipse(img,(750,750),(280,280),180,0,180,[255,0,0],-2)
indigo = cv2.ellipse(img,(750,750),(210,210),180,0,180,[130,0,75],-2)
violet = cv2.ellipse(img,(750,750),(140,140),180,0,180,[211,0,148],-2)

black = cv2.ellipse(img,(750,750),(70,70),180,0,180,[0,0,0],-2)
cv2.imwrite('output/rainbow.png', img)
# cv2.imshow("img",img)
# cv2.waitKey()