import os
import sys

from database import (register_user, delete_user, user_exists,get_db_connection, store_emotion, store_gender, store_age)
from capture import capture_face
from face_recognition import recognize_face
from gender_identification import predict_gender
from age_estimation import predict_age_group
from emotion_analysis import predict_emotion

project_data = r"D:\DESKTOP\AI proj\project\data"

def get_user_id(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None

username=""
def register_flow():

    while True:
        username = input("\n–– Registration ––\nEnter new name (or e to exit):").strip()
        if username.lower() == "e":
            print("\nRegistration cancelled.\n")
            return None

        if not username:
            print("Name can not be blank -__-!!. Try again.")
            continue

        if user_exists(username):
            print(f"'{username}' already registered :(. choose another name please.")
            continue

        register_user(username)

        if capture_face(username):
            print(f"Registered '{username}' and captured face :).")
            return username
        else:
            print("Face was not captured due to an issue :(. Try again later....")
            delete_user(username)
            return None



def login_flow():
    print("\n–– User identity verification! ––")
    user = recognize_face()

    if user:
        print(f"Welcome back {user}!")
    else:
        print("Could not verify :(). Please try again.")

    return user



def select_user_type():
    while True:
        print("\n=== Select User Type ===")
        print("1) Existing User")
        print("2) New User")
        choice = input("Choice (1/2):").strip()

        if choice == "1":
            user = login_flow()
            if user:
                return user
        elif choice == "2":
            user = register_flow()
            if user:
                return user
        else:
            print("Invalid choice *_*. Enter 1 or 2 only.")




def options_menu(user):
    #identified = None
    user_id = get_user_id(user)

    while True:
        print(f"\n=== Options for '{user}' ===")
        #print("1) Identify user")
        print("1) Analyse emotion :(,:-|,:) ")
        print("2) Predict gender (M/F)")
        print("3) Predict age group (YOUNG,MIDDLE,OLD)")
        print("4) Delete user")
        print("5) Exit")

        choice = input("Choice (1–5): ").strip()

        # if choice == "1":
        #     identified = recognize_face()
        #     if identified:
        #         print(f"Found user: {identified}")
        #     else:
        #         print("No face detected.")

        if choice == "1":
            # if not identified:
            #     print("User has not been identified yet!!!...:(")
            #     continue

            capture_face(username)

            img_path = os.path.join(project_data, f"{username}.jpg")
            if os.path.exists(img_path):
                emotion = predict_emotion(img_path)
                store_emotion(user_id, img_path)
                print(f"Emotion Prediction: {emotion}")
            else:
                print("Image not found :-| : \n", img_path)

        elif choice == "2":
            # if not identified:
            #     print("User has not been identified yet.")
            #     continue
            capture_face(username)
            img_path = os.path.join(project_data, f"{username}.jpg")
            if os.path.exists(img_path):
                gender = predict_gender(img_path)
                store_gender(user_id, img_path)
                print(f"Gender Prediction: {gender}")
            else:
                print("Image not found:\n", img_path)

        elif choice == "3":
            # if not identified:
            #     print("User has not been identified yet.")
            #     continue
            capture_face(username)
            img_path = os.path.join(project_data, f"{username}.jpg")
            if os.path.exists(img_path):
                age_group = predict_age_group(img_path)
                store_age(user_id, img_path)
                print(f"Age Group Prediction: {age_group}")
            else:
                print("Image not found:\n", img_path)

        elif choice == "4":
            if input(f"Are you sure you want to delete '{user}'? (y/n): ").lower().startswith("y"):
                delete_user(user)
                return input("Select another user? (y/n): ").lower().startswith("y")

        elif choice == "5":
            print("Goodbye! *__* \n------------------------------------\n")
            sys.exit()

        else:
            print("Invalid input. Please choose 1–6.")


def main():
    get_db_connection()
    while True:
        user = select_user_type()
        restart = options_menu(user)
        if not restart:
            break


main()
