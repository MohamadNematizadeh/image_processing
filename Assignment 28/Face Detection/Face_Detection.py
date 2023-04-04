import cv2
import cvzone
import keyboard

f_detector =cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
e_detector =cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye_tree_eyeglasses.xml")
s_detector =cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")


f_emoj = cv2.imread("input/Happy-Face-Emoji.png", cv2.IMREAD_UNCHANGED)
e_Emoj = cv2.imread("input/eye.png", cv2.IMREAD_UNCHANGED)
s_Emoj = cv2.imread("input/smile.png", cv2.IMREAD_UNCHANGED)

video_cap = cv2.VideoCapture(0)
current_state = 0
#Resize an image to a certain width
def mirror(image):
    x_size = image.shape[1]
    flipVertical = cv2.flip(image[:,:x_size//2], 1)
    image[:,x_size//2:] = flipVertical
    return image    
while True:    
    ret, frame = video_cap.read()
    if ret == False:
        break

    k = cv2.waitKey(1)
    if keyboard.is_pressed('1'):
        FACES = f_detector.detectMultiScale(frame, 1.3)
        for (x, y, w, h) in FACES:
            finalEmojy = cv2.resize(f_emoj, (w, h))
            frame = cvzone.overlayPNG(frame, finalEmojy, [x, y])
            
    if keyboard.is_pressed('2'):
        LEYE = e_detector.detectMultiScale(frame, 1.5, maxSize=(50,50))
        for (x, y, w, h) in LEYE:
            finalEmojy = cv2.resize(e_Emoj, (w, h))
            frame = cvzone.overlayPNG(frame, finalEmojy, [x, y])  
        SMILE = s_detector.detectMultiScale(frame, 1.3, 15)
        for (x, y, w, h) in SMILE:
            finalEmojy = cv2.resize(s_Emoj, (w, h))
            frame = cvzone.overlayPNG(frame, finalEmojy, [x, y])

    if keyboard.is_pressed('3'):
        FACES = f_detector.detectMultiScale(frame, 1.3)
        for (x, y, w, h) in FACES:            
            blurred = frame[y:y+h, x:x+w]
            pixlated = cv2.resize(blurred, (15, 15), interpolation=cv2.INTER_LINEAR)
            output = cv2.resize(pixlated, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = output

    if keyboard.is_pressed('4'):
        FACES = f_detector.detectMultiScale(frame, 1.3)
        frame = mirror(frame)
         
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("Out_Put", frame)
