#login and registration using file with username and password
import json
import os

FilePath= r"python_basics\credential.txt"

def load_users():
    if not os.path.exists(FilePath):
        return FileNotFoundError
    else:
        with open(FilePath, "r") as f:
            content = f.read()
        list_credential = content.splitlines()
        users = [json.loads(item) for item in list_credential]
        return list_credential

def register():
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    users = load_users()

    # Check if username already exists
    for user in users:
        if username in user:
            print(f"User '{username}' already exists!")
            return

    # Add new user
    dict_credential = {username: password}
    with open(FilePath, "a") as f:
        f.write(json.dumps(dict_credential) + "\n")
    print(f"Username '{username}' created successfully.")



while True:
    choice = int(input("Enter 1 for register, 2 for login , 3 for exist: "))
    match choice:
        case 1:
            register()
        case 2:
            login()
        case 3:
            break
        case _:
            print("Please enter the valid option")
        
        
