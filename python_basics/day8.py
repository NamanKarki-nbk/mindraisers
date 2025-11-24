#login and registration using file with username and password
import json

FilePath= r"python_basics\credential.txt"


def register():
    username = input("\n Enter your username: ")
    password  = input("\nEnter your password: ")
    
    dict_credential = {username:password}
    json_credential = json.dumps(dict_credential)
    with open(FilePath, "a") as f:
        f.write(json_credential+"\n")
    print(f"Username with {username} and password: {password}  created successfully")
    
    
def login():
    username = input("\n Enter your username: ")
    password = input("\nEnter your password: ")

    with open(FilePath, "r") as f:
        content = f.read()

    list_credential = content.splitlines()   
    found = False

    for item in list_credential:
        dict_i = json.loads(item)  

        if username in dict_i and dict_i[username] == password:
            print("Login Successful")
            found = True
            break  

    if not found:
        print("Login Failed")


    
    

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
        
        
#for else