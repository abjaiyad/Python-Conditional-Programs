# Make a program that reads the year of birth of a person and informs if he is able to vote (age greater than or equal to 18 years old).

# Prompt the user to enter the year of birth
year_of_birth = int(input("Enter the year of birth: "))

# Calculate the current year
import datetime
current_year = datetime.datetime.now().year

# Calculate the age of the person
age = current_year - year_of_birth

# Check if the person is eligible to vote
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")