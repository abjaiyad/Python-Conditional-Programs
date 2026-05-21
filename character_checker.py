# Character Checker

# Check whether input is:

# Alphabet
# Digit
# Special Character

# Character Checker System

# Prompt the user to enter a single character
user_input = input("Enter any character: ")

# Safety check: ensure the user only typed exactly ONE character
if len(user_input) != 1:
    print("Please enter only a single character!")
else:
    # Check if it is an alphabet letter
    if user_input.isalpha():
        print(f"'{user_input}' is an Alphabet.")
        
    # Check if it is a number digit
    elif user_input.isdigit():
        print(f"'{user_input}' is a Digit.")
        
    # If it's neither, it's a special character
    else:
        print(f"'{user_input}' is a Special Character.")