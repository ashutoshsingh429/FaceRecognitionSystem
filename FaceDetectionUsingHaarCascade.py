# Read a video stream from camera (frame by frame)
import cv2

# We use '0' for the first cam of the device (incase there are more cams in the device one can use 1 or 2 or 3 etc)
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Incase the cam did not turn ON or could not be found
    if ret == False:
        continue

    # 1.3 = scaling factor, 5 = number of neighbours
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Video Frame', frame)

    # Wait for the user input - q, then you can stop the loop
    # '1' means wait for 1 millisecond
    # cv2.waitKey(1) gives a 32 bit number and 0xFF = 1111 1111 (8 bit number). There AND would give a 8 bit number. So we basically want 
    # key_pressed to be an 8 bit number
    # ord('q') gives the ASCII value of 'q' which is again an 8 bit number
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()
