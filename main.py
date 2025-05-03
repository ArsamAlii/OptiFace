import os
import sys

from database               import register_user, delete_user
from capture                import capture_face
from face_recognition       import recognize_face
from gender_identification  import predict_gender
from age_estimation         import predict_age_group
from emotion_analysis       import predict_emotion

project_data = r"D:\DESKTOP\AI proj\project\data" 

def register_flow():
    while True:
        username=input("\n–– Registration ––\nEnter new name or e to exit:").strip()
        if username.lower()=="e":
            print("\nRegistration cancelled.\n")
            return None

        if not username:
            print("Name should not be blank :(( try again please.")
            continue

        if user_exists(username): 
            print(f"'{username}' already registered please choose another name. :)")
            continue

        register_user(username)

        if capture_face(username): 
            print(f"registered '{username}'.")
            return username
        else:
            print("Face has not been captured :(( due to some issue try again later..")
            delete_user(username)


def login_flow():
    print("\n–– User identity verification :)––")
    user=recognize_face()

    if user:
        print(f"Welcome back , {user}! :)")
    else:
        print("Could not verify please try again.")

    return user


def select_user_type():
    while True:
        print("\n=== Select User Type ===")
        print("1) Existing User")
        print("2) New User")
        choice=input("Choice (1/2):").strip()

        if choice=="1":
            user=login_flow()
            if user:
                return user
        elif choice=="2":
            user=register_flow()
            if user: 
                return user
        else:
            print("invalid choice. Enter 1 or 2 only :((.")



def options_menu(user):
    identified=None

    while True:
        print(f"\n=== Options for '{user}' ===\n Choose any:")
        print("1) Identify user")
        print("2) Analyse emotion")
        print("3) Predict gender")
        print("4) Predict age group")
        print("5) Delete user")
        print("6) Exit")

        choice=input("Choice (1-6 only):").strip()

        if choice=="1":
            identified=recognize_face()

            if identified:
                print("Found:",identified)
            else:
                print( "No face detected.",identified)


        elif choice=="2":
            if not identified:
                print("User has not been identified yet ://")
                continue

            img_path=os.path.join(project_data,f"{identified}.jpg")

            if os.path.exists(img_path):
                print("Emotion:",predict_emotion(img_path))
            else:
                print("Image not found on the following path: \n",img_path)


        elif choice=="3":
            if not identified:
                print("User has not been identified yet... ://")
                continue
            img_path=os.path.join(project_data,f"{identified}.jpg")
            if os.path.exists(img_path):
                print("Predicted Gender:", predict_gender(img_path))
            else:
                print("Image not found on the following path :\n",img_path)

        elif choice == "4":
            if not identified:
                print("User has not been identified yet ://")
                continue
            img_path = os.path.join(project_data, f"{identified}.jpg")
            if os.path.exists(img_path):
                print("Predicted age group:",predict_age_group(img_path))
            else:
                print("Image not found on the following path: \n",img_path)

        elif choice=="5":
            if input(f"Are you sure you want to delete '{user}'?? :-/ (y/n): ").lower().startswith("y"):
                delete_user(user)
                return input("Select another user? (y/n):").lower().startswith("y")

        elif choice=="6":
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid only choose 1‑6.")


def main():
    while True:
        user=select_user_type()
        restart=options_menu(user)
        if not restart:
            break

main()
