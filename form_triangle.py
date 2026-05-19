# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

# Prompt the user to enter three angles:
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

# Add all angles
triangle = angle1 + angle2 + angle3

# Check condition
if triangle == 180:
    result = "a triangle"
else:
    result = "not a triangle"

# Display the result
print("It can form",result)