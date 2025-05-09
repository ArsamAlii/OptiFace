import mysql.connector
from mysql.connector import Error

db_connection=None 

try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="07619",
        database="face_recognition"    
    )

    cursor = db_connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS face_recognition")
    cursor.execute("USE face_recognition")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) UNIQUE NOT NULL,
        registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emotions (
        emotion_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        emotion VARCHAR(100),
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS genders (
        gender_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        gender VARCHAR(50),
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ages (
        age_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        age_group VARCHAR(50),
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )""")

    print("Database and all tables created successfully!")

except Error as e:
    print("Error:", e)

finally:
    if db_connection and db_connection.is_connected():
        cursor.close()
        db_connection.close()
        print("MySQL connection closed.")
