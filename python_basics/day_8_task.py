import json
import os

FilePath = r"python_basics\bank.txt"

def load_users():
    if not os.path.exists(FilePath):
        return []
    else:
        with open(FilePath, "r") as f:
            content = f.read()
        list_credential = content.splitlines()
        users = [json.loads(item) for item in list_credential]
        return users

def save_users(users):
    with open(FilePath, "w") as f:
        for u in users:
            f.write(json.dumps(u) + "\n")

def register():
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    users = load_users()

    for user in users:
        if username in user:
            print(f"User '{username}' already exists!")
            return

    dict_credential = {username: {"password": password, "balance": 0.0}}
    
    with open(FilePath, "a") as f:
        f.write(json.dumps(dict_credential) + "\n")

    print(f"Username '{username}' created successfully.")

def login():
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")

    users = load_users()

    for user in users:
        if username in user and user[username]["password"] == password:
            print("Login Successful")
            bank_menu(username, users)
            return

    print("Login Failed")

def bank_menu(username, users):
    while True:
        print("\n1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")

        choice = input("Enter your choice: ")

        for user in users:
            if username in user:
                current = user[username]

        if choice == "1":
            print("Your Balance:", current["balance"])

        elif choice == "2":
            amt = float(input("Enter amount to deposit: "))
            current["balance"] += amt
            save_users(users)
            print("Deposit Successful")

        elif choice == "3":
            amt = float(input("Enter amount to withdraw: "))
            if amt > current["balance"]:
                print("Insufficient balance")
            else:
                current["balance"] -= amt
                save_users(users)
                print("Withdrawal Successful")

        elif choice == "4":
            print("Logged out.")
            break

        else:
            print("Invalid choice")

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
