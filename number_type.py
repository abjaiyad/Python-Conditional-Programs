# Number Type

# Check whether number is:

# Single digit
# Double digit
# Triple digit

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Use abs() to ignore the negative sign for our digit counting math
check_number = abs(number)

# Check the digit classification based on the absolute value
if check_number <= 9:
    result = "a single digit number"
elif check_number <= 99:
    result = "a double digit number"
elif check_number <= 999:
    result = "a triple digit number"
else:
    result = "a large multi-digit number"

# Display the result
print(f"{number} is {result}.")