import numpy as np
import cv2

cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]
text_size = 1
writer = cv2.VideoWriter("otput/Write_a_color.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))
while True:
    ret,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    me = frame[200:300,300:400]
    if ret == False:
        break
    camera_filter = np.ones((35,35))/1225
    frame = cv2.filter2D(frame,-1,camera_filter)
    frame[200:300,300:400] = me
    color_me = frame[200:300,300:400]
    # coler black
    if  0 < np.average(color_me) <= 85:
        cv2.rectangle(frame,(300,200), (400,300), (0, 0, 255),2)
        cv2.putText(frame,'Black',(50,50),cv2.FONT_ITALIC,1,(0,0,0),int(text_size))
    # coler gray
    elif 85 < np.average(color_me) <= 170:
        cv2.rectangle(frame,(300,200), (400,300), (127, 127, 127),2)
        cv2.putText(frame,'gray',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(127,127,127),int(text_size))
    # coler white
    elif 170 < np.average(color_me) <= 255:
        cv2.rectangle(frame,(300,200), (400,300), (0, 0, 255),2)
        cv2.putText(frame,'white',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),int(text_size ))
    # saev frmame
    writer.write(frame)
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break     
              
writer.release()    