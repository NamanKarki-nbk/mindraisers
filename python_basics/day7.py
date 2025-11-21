#login and register without password

Filename = r"E:\mindraisers\python_basics\users.txt"

def load_users():
    try:
        with open(Filename, "r") as f:
            users = f.read()
            return users
    except FileNotFoundError:
        return []
    
    

def registration():
    username = input("Enter the username:")
    users = load_users()
    
    if username in users:
        print("Username already exists")
    
    else:
        with open(Filename, "a") as f:
            f.write(username + "\n")
        print(f"Username {username} created successfully")
        

def login():
    username = input("Enter the username")
    users = load_users()
    
    if username in users:
        print(f"Login successful {username}")
    
    else:
        print("Username not found")
        


def main():
    while True:
        print("\n1. Register")
        print("\n2. Login")
        print("\n1. Exit")

        choice = int(input("\nEnter the choice"))
        
        if choice == 1:
            registration()
        
        elif choice == 2:
            login()
            
        elif choice ==3:
            break
        else:
            print("\nPlease enter the valid option")
            
        

main()