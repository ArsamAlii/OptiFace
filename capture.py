import cv2
import os

def capture_face(username):
    save_path = os.path.join("data",f"{username}.jpg")

    if not os.path.exists("data"):
        os.mkdir("data")

    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

    print("Capturing your face. Press 's' to save, 'e' to exit.")

    while True:
        ret,frame=cam.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.1,5)#scalefac,minneighbour

        for (x, y, w, h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("Capture Face", frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            if len(faces) > 0:
                (x,y,w,h) = faces[0]
                face = frame[y:y+h,x:x+w]
                cv2.imwrite(save_path,face)
                print(f"Face image saved as {save_path}")
            break
        elif key == ord('e'):
            break

    cam.release()
    cv2.destroyAllWindows()