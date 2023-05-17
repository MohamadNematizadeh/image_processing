
import cv2

cap = cv2.VideoCapture(0)
background = cv2.imread('input/shakespear_rambrant.jpg')
face_detector =cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_alt.xml")
# Get video properties
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Blend background image with video frame
    faces = face_detector.detectMultiScale(frame)    
    for face in faces :
        x , y , w , h  = face
        # background [y+20:y+int((h/2))+20 , x+40:x+int(w)-40] = frame[y+20:y+int((h/2))+20   , x+40:x+int(w)-40] #eye
        background [y+130:y+int((h/2))+100 , x+50:x+int(w)-50] = frame[y+130:y+int((h/2))+100 , x+50:x+int(w)-50] #lip+nose

    # Display or save blended frames as desired
    cv2.imshow('Blended Frame', background)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

cap.release()
# 
# qcv2.destroyAllWindows()
