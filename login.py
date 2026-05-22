# Login System
# Check username & password.

# Prompt the user to create their username & password
username = input("Create your username: ").lower()
password = input("Create your password: ")

print("\nWelcome to the login page")
# Prompt the user to enter their username & password
username1 = input("Enter your username for login: ").lower()
password1 = input("Enter your password for login: ")

# Check the username and password entered by the user is correct or not using if statement
if username == username1 and password == password1:
        print("login succesful")
else:
    print("wrong username or password")