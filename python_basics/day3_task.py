def check_username_list(username):
    valid_usernames =["naman123", "nayan456", "karan789", "sammy101"]
    if username in valid_usernames:
        return "Valid User"
    else:
        return "Invalid User"
    

def check_username_dictionary(username):
    valid_users ={
        "naman123": "password1",
        "nayan456": "password2",
        "karan789": "password3",
        "sammy101": "password4"
    }
    
    extracted_usernames = valid_users.keys()
    
    if username in extracted_usernames :
        return "Valid User"
    else:
        return "Invalid User"

def validate_user_credentials(username,password):
    valid_users ={
        "naman123": "password1",
        "nayan456": "password2",
        "karan789": "password3",
        "sammy101": "password4"
    }
    
    if username in valid_users and valid_users[username]== password:
        return "Credentials are Valid"
    else:
        return "Credentials are Invalid"


if __name__ == "__main__":
    
    input_username = input("Enter your username:\n")
    input_password=input("Enter your password:\n")
    print("Select an option to validate username:\n")
    print("1. Check using List\n")
    print("2. Check using Dictionary\n")
    print("3. Validate using both Username and Password\n")
    while True:
        match int(input("Choose the option: \n")):
            case 1:
                result =check_username_list(input_username)
                print(result)
            case 2:
                result=check_username_dictionary(input_username)
                print(result)
            case 3:
                result=validate_user_credentials(input_username, input_password)
                print(result)
            case _:
                print("Invalid Option")
                
                
    