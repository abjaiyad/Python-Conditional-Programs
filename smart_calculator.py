# 🚀 NOW — Mini Project: Smart Calculator

# Build this program:

# Requirements
# Ask first number
# Ask operator (+, -, *, /)
# Ask second number
# Print result

# Example:

# Enter number: 10
# Enter operator: *
# Enter number: 5
# Result = 50

num1 = float(input("Enter First Number: "))

operator = input("Enter an Operator(+, -, *, /): ")

num2 = float(input("Enter Second Number: "))

if operator == "+":
    print(f"Addition of {num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"Subtraction of {num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"Multiplication of {num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("Error! Division By Zero")
    else:
        print(f"Division of {num1} / {num2} = {num1 / num2}")
else:
    print("Invalid Operator")