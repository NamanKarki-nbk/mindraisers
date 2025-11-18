#Make a accounting system where a user logins and he should be able to check the balance, add balance and withdraw balance. Use dictionary, IF…ELSE and loop if needed.

users = {}

def create_user(name:str, password: str, balance:float = 0.0)-> dict:
    
    if name in users:
        print("User already exists")
        return {}
    else:
        user= {name:{ "password": password, "balance": balance}}
        users.update(user)
        return user

def login_user(name: str, password: str) -> bool:
    if name in users:
        return users[name]["password"] == password
    return False

def check_balance(name:str) -> float:
    if name in users:
        return users[name]["balance"]

def add_balance(name: str, amount:float) -> float:
    if name in users:
        users[name]['balance'] += amount
        return users[name]['balance']

def withdraw_balance(name: str, amount:float) -> float:
    if name in users:
        if users[name]['balance'] >= amount:
            users[name]['balance'] -= amount
            return users[name]['balance']
    else:
        return "Not enough balance"
    

if __name__ == "__main__":
    while True:
        
        print("1. Create User")
        print("2. Login")
        print("3. Exit")

        choice = int(input("\nChoose an option: "))

        if choice == 1:
            name = input("\nEnter the username: ")
            password = input("Enter the password: ")
            balance = input("Enter the balance or skip for default parameter: ")

            if balance == "":
                user = create_user(name, password)
            else:
                user = create_user(name, password, float(balance))

            print(f"\nUser created successfully:\n{user}")

        elif choice == 2:
            name = input("\nEnter the username: ")
            password = input("Enter the password: ")

            if login_user(name, password):
                print("\nLogin successful")

                while True:
                    print("1. Check Balance")
                    print("2. Add Balance")
                    print("3. Withdraw Balance")
                    print("4. Logout")

                    option = int(input("\nChoose an option: "))

            
                    if option == 1:
                        balance = check_balance(name)
                        print(f"\nYour current balance is: Rs. {balance}")

                    
                    elif option == 2:
                        amount = float(input("\nEnter the amount to add: "))
                        updated = add_balance(name, amount)
                        print(f"New balance: Rs. {updated}")

                    
                    elif option == 3:
                        amount = float(input("\nEnter the amount to withdraw: "))
                        updated = withdraw_balance(name, amount)
                        print(f"Updated balance: Rs. {updated}")

                    elif option == 4:
                        print("\nLogged out successfully!\n")
                        break

                    else:
                        print("Invalid option")

            else:
                print("\nInvalid username or password!")

        elif choice == 3:
            print("\nExiting the system")
            break

        else:
            print("Invalid choice.")
            

