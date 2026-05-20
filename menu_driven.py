# Write a menu-driven program -
# 1. cm to ft
# 2. km to miles
# 3. USD to INR
# 4. exit

# Show menu to user
print("---- Conversion Menu ----")
print("1. cm to ft")
print("2. km to miles")
print("3. USD to INR")
print("4. Exit")

# Prompt the user for enter their choice
choice = int(input("Enter your choice: "))

# Use if-elif-else to decide work
if choice == 1:
    cm = float(input("Enter cm value: "))
    ft = cm / 30.48
    print("Feet:", ft)
elif choice == 2:
    km = float(input("Enter km value: "))
    miles = km * 0.621371
    print("Miles:", miles)
elif choice == 3:
    usd = float(input("Enter USD value: "))
    inr = usd * 96.9177
    print("INR:", inr)
elif choice == 4:
    print("Program exited")
else:
    print("Invalid input")