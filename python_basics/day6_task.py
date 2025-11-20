#Multiplication Table of a Number
num = int(input("Enter a number: "))
for item in range(1, 11):
    print(f"{num} x {item} = {item * num}")

#Check if a Number is Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#Check if Number is Palindrome
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome Number")
else:
    print("Not a Palindrome")

#Print all even numbers in a List
numbers = [12, 3, 5, 8, 10, 17, 24]
for num in numbers:
    if num % 2 == 0:
        print(num)

#login without registration
def login():
    username = "naman"
    password = "naman123"

    username1 = input("Enter username: ")
    password1 = input("Enter password: ")

    if username1 == username and password1 == password:
        print("Login Successful")
    else:
        print("Unsuccessful login")

login()
