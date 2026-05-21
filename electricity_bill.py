# Electricity Bill

# Input units:

# Units	Cost
# ≤100	₹5/unit
# 101–200	₹7/unit
# >200	₹10/unit

# Print total bill.

unit = int(input("Enter the number of units: "))

if unit <= 100:
    total_bill = unit * 5
elif unit <= 200:
    total_bill = 500 + (unit - 100) * 7
else:
    total_bill = 1200 + (unit - 200) * 10

print(f"Your total electricity bill is: ₹{total_bill}")