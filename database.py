import csv
import os

DB_FILE = "user_database.csv"

def register_user(username):
    # username = input("Enter your name: ")
    # Later: Capture face
    with open(DB_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username])
    print(f"User {username} registered successfully!")

def login_user():
    username = input("Enter your name to login: ")
    if os.path.exists(DB_FILE):
        with open(DB_FILE, mode='r') as file:
            users = [row[0] for row in csv.reader(file)]
            if username in users:
                print(f"Welcome back, {username}!")
            else:
                print("User not found.")

def delete_user():
    username = input("Enter your name to delete account: ")
    if os.path.exists(DB_FILE):
        with open(DB_FILE, mode='r') as file:
            users = [row for row in csv.reader(file)]

        users = [row for row in users if row[0] != username]

        with open(DB_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(users)
        
        print(f"User {username} deleted (if existed).")
