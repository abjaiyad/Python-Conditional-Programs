# Login System

# Create a program:

# Ask username
# Ask password

# Rules:

# username = "admin"
# password = "1234"

# Output:

# Correct → Login Successful
# Wrong password → Incorrect Password
# Wrong username → User Not Found

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("User Not Found")