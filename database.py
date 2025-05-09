import os
import mysql.connector
from capture import capture_face
from face_recognition import recognize_face
from gender_identification import predict_gender
from age_estimation import predict_age_group
from emotion_analysis import predict_emotion

project_data = r"D:\DESKTOP\AI proj\project\data"

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="07619",
        database="face_recognition"
    )

def user_exists(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None

def register_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"User {username} registered successfully!")

def delete_user(username):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]

        for table in ['emotions', 'genders', 'ages']:
            cursor.execute(f"DELETE FROM {table} WHERE user_id = %s", (user_id,))

        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        conn.commit()
        print(f"User '{username}' deleted from database.")

        image_path = os.path.join(project_data, f"{username}.jpg")
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f"Deleted image: {image_path}")
    else:
        print(f"User '{username}' not found.")

    cursor.close()
    conn.close()


def store_emotion(user_id, img_path):
    emotion = predict_emotion(img_path)
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO emotions (user_id, emotion) VALUES (%s, %s)", (user_id, emotion))
    db_connection.commit()
    db_connection.close()

# def store_gender(user_id, img_path):
#     gender = predict_gender(img_path)
#     db_connection = get_db_connection()
#     cursor = db_connection.cursor()
#     user = cursor.execute("select user_id from users where username = '%s' ", user_id)
#    cursor.execute("INSERT INTO genders (user_id, gender) VALUES (%s, %s)", (user, gender))
#     db_connection.commit()
#     db_connection.close()

def store_gender(user_id, img_path):
    gender = predict_gender(img_path)
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (user_id,))
    user = cursor.fetchone()
    if user:
        cursor.execute("INSERT INTO genders (user_id, gender) VALUES (%s, %s)", (user[0], gender))
        db_connection.commit()
    db_connection.close()

def store_age(user_id, img_path):
    age_group = predict_age_group(img_path)
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO ages (user_id, age_group) VALUES (%s, %s)", (user_id, age_group))
    db_connection.commit()
    db_connection.close()
