# Make a program that asks for two numbers and displays if the first is divisible by the second

# Prompt the user to enter the first number
num1 = int(input("Enter the first number: "))

# Prompt the user to enter the second number
num2 = int(input("Enter the second number: "))

# Check if the first number is divisible by the second number
if num1 % num2 == 0:
    result = "divisible"
else:
    result = "not divisible"

# Display the result
print(f"The first number is {result} by the second number.")