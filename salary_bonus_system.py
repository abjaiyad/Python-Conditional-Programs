# Highest Salary Bonus System
# Give bonus based on salary range.

salary = float(input("Enter your basic salary: "))

# Determine bonus percentage based on salary range
if salary < 3000:
    bonus_percent = 0.15
elif salary <= 70000:
    bonus_percent = 0.10
else:
    bonus_percent = 0.5

# Calculate the actual bonus money
calculated_bonus = salary * bonus_percent
total_pay = salary + calculated_bonus

print(f"Your Bonus is: ₹{calculated_bonus} ({bonus_percent * 100}%)")
print(f"Total payout this month: ₹{total_pay}")