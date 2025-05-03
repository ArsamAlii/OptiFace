import cv2
import os
import numpy as np

def recognize_face():
    print("Recognizing face... Please look into the camera.")
    cam = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    ret, frame = cam.read()
    cam.release()

    if not ret:
        print("Failed to capture image.")
        return None

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    if len(faces) == 0:
        print("No face detected.")
        return None

    (x, y, w, h) = faces[0]
    input_face = gray[y:y+h, x:x+w]
    input_face = cv2.resize(input_face, (100, 100))

    best_match = None
    best_score = float("inf")

    for file in os.listdir("data"):
        user_face = cv2.imread(os.path.join("data", file), cv2.IMREAD_GRAYSCALE)
        user_face = cv2.resize(user_face,(100, 100))
        score = np.sum((input_face - user_face) ** 2)

        if score < best_score:
            best_score = score
            best_match = file.split(".")[0]

    if best_match:
        print(f"Recognized as {best_match}")
        return best_match
    else:
        print("No match found.")
        return None
