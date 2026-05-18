# 🔵 Problem 3 — ATM Withdrawal System

# Take:

# account balance
# withdrawal amount

# Rules:

# If amount ≤ balance:
# If amount ≤ 10000 → Transaction Approved
# Else → Daily Limit Exceeded
# Else → Insufficient Balance

balance = float(input("Enter balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= balance:
    if withdrawal <= 10000:
        balance -= withdrawal
        print("Transaction Approved")
        print("Remaining Balance:", balance)
    else:
        print("Daily Limit Exceeded")
else:
    print("Insufficient Balance")