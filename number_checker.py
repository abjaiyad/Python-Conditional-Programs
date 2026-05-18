# Write a program that reads a number and reports whether it is positive, negative or zero.

# Prompt the user for a number
number = float(input("Enter a number: "))

# Check if a number is positive, negative or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")