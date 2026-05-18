# Write a program that asks for the name of a day of the week and displays whether it is a weekday
# (Monday to Friday) or a weekend day (Saturday and Sunday).

# Prompt the user to enter the name of a day
day = input("Enter the name of a day: ").lower().strip()

# Check if the is a weekday or a weekend day
if day == "saturday" or day == "sunday":
    result = "Weekend day"
elif day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    result = "Weekday"
else:
    print("Not a valid day! Please check your input.")
    # Adding additional input validation for error handling
    day = input("Enter the name of a day: ").lower().strip()
    if day == "saturday" or day == "sunday":
        result = "Weekend day"
    else:
        result = "Weekday"

# Display the result
print(f"{day.capitalize()} is a {result}.")