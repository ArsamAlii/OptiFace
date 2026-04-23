# Face Recognition and Analysis System

This project is a Python-based face recognition and facial analysis system. It allows a user to register by capturing a face image, log in through face recognition, and perform facial analysis tasks such as emotion detection, gender prediction, and age group estimation. The system also stores user and prediction data in a MySQL database.

## Features

- User registration with face capture
- User login using face recognition
- Emotion prediction
- Gender prediction
- Age group prediction
- MySQL database integration for storing users and predictions
- Option to delete a user and their stored records

## Project Files

- `main.py` - main program that runs the system menu and user flows
- `capture.py` - captures a face image from webcam
- `face_recognition.py` - recognizes a registered face using image comparison
- `gender_identification.py` - predicts gender from a face image
- `age_estimation.py` - predicts age group from a face image
- `emotion_analysis.py` - predicts emotion from a face image
- `database.py` - handles database connection and data storage
- `create_tables.py` - creates the MySQL database and required tables

## Technologies Used

- Python
- OpenCV
- TensorFlow / Keras
- NumPy
- MySQL

## How It Works

1. A new user registers by entering a username and capturing their face.
2. The face image is stored in the `data` folder.
3. The username is stored in the MySQL database.
4. Existing users can log in through face recognition.
5. After login, the user can:
   - analyze emotion
   - predict gender
   - predict age group
   - delete user data

## Database Tables

The project uses the following tables:

- `users`
- `emotions`
- `genders`
- `ages`

These tables store user details and prediction history.

## Requirements

Install the required libraries before running the project:

```bash
pip install opencv-python tensorflow numpy mysql-connector-python
