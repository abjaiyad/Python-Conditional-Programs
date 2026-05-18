# Write a program that asks the user for three numbers and displays the largest one.

# Prompt the user for three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine the largest number using conditional statement
if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num2 >= num1 and num2 >= num3:
    largest_num = num2
else:
    largest_num = num3

# Display the largest number to the user
print("The largest number is:",largest_num)