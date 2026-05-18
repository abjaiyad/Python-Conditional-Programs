# Create a program that asks for a person's age and displays whether they are a child (0-12 years old), 
# teenager (13-17 years old), adult (18-59 years old), or elderly (60 years old or older).

# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check the age range and assign the category corresponding
if age <= 12:
    category = "Child"
    print("You are a", category + ".")
elif age <= 17:
    category = "Teenager"
    print("You are a", category + ".")
elif age <= 59:
    category = "Adult"
    print("You are a", category + ".")
elif age <= 99:
    category = "Elderly"
    print("You are a", category + ".")
else:
    print("God is waiting for you.")