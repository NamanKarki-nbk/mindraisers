#function to add two numbers
def add(a,b):
    return a+b

#function to subtract two numbers
def sub(a,b):
    return a-b

#function to divide two numbers
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
#function to multiply two numbers

def multiply(a,b):
    return a*b

#function to find the modulus of two numbers
def modulus(a,b):
    return a%b


def main():
    
    print("Choose the operation \n")
    print("1.Add\n")
    print("2.Subtract\n")
    print("3.Multiply\n")
    print("4.Divide\n")
    print("5.Modulus\n")
    print("6. Perform all the operations\n")
    
    choice = float(input("Enter choice in 1,2,3,4 or 5:\n"))
    
    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The sum is: {add(num1,num2)}")
        
    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The difference is: {sub(num1,num2)}")
    
    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The product is: {multiply(num1,num2)}")
    
    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The quotient is: {divide(num1,num2)}")
    
    elif choice == 5:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The modulus is: {modulus(num1,num2)}")
    
    elif choice == 6:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The sum is: {add(num1,num2)}")
        print(f"The difference is: {sub(num1,num2)}")
        print(f"The product is: {multiply(num1,num2)}")
        print(f"The quotient is: {divide(num1,num2)}")
        print(f"The modulus is: {modulus(num1,num2)}")
    
    else:
        print("Invalid input")
        
if __name__ == "__main__":
    
    main()

