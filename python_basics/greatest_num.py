num1 = int(input("Enter first number: \n"))
num2 = int(input("Enter second number: \n"))
num3 = int(input("Enter third number: \n"))

if num1 >= num2 and num1 >= num3:
    print(f"The greatest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The greatest number is: {num2}")
else:
    print(f"The greatest number is: {num3}")