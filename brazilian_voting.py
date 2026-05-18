# Make a program that reads a person's age and informs if he is not able to vote 
# (age less than 16 years old), if he is able to vote but is not obligated (16, 17 years old, or age equal to or greater than 70 years),
# or if it is obligatory (18 to 69 years old).

# Note: These conditions are in accordance with Brazilian legislation.

# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check the age range and inform the voting eligibility
if age < 16:
    print("You are not able to vote.")
elif age >= 18 and age <= 69:
    print("Voting is obligatory for you.")
else:
    print("You are able to vote, but it is not obligatory.")