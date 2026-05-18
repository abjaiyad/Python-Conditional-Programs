# Make a program that reads three numbers, and informs if their sum is divisible by 5 or not.

# Prompt the user to enter three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculates the sum of the three numbers
total = num1 + num2 + num3

# Check if the sum is divisible by 5
if total % 5 == 0:
    print("The sum is divisible by 5.")
else:
    print("The some is not divisible by 5.")