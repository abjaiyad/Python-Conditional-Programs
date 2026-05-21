# Simple Calculator

# Prompt the user for the two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user to select operation (changed 'x' to '*' to match the code)
operation = input("Enter the operation you want to perform (+, -, *, /): ")

# Perform the operation using if statement
if operation == "+":
    result = num1 + num2
    print(f"{num1} {operation} {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} {operation} {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} {operation} {num2} = {result}")
elif operation == "/":
    # Prevent crashing when dividing by zero
    if num2 == 0:
        print("Error: division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} {operation} {num2} = {result}")
else:
    print(f"Error: '{operation}' is an invalid operation.")