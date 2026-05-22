# ATM Withdrawal Logic
# Check:
# balance available?
# amount multiple of 100?
# enough balance?

# Set dummy value for the account
account_balance = 50000 # The user has 50000 in their bank account

print(f"Welcome to the ATM. Your current balance is: ₹{account_balance}")
withdraw_amount = int(input("Enter the amount you want to withdraw: "))

# Check1: Is there any balance available in the account
if account_balance <= 0:
    print("Transaction Denied: Your account balance is zero.")
else:
    # Check 2: Is the requested amount a multiple of 100?
    if withdraw_amount % 100 != 0 or withdraw_amount <= 0:
        print("Transaction Denied: Please enter an amount in multiples of 100 (e.g., 100, 200, 500)")
    else:
        # Check 3: Does the user have enough balance to cover the withdrawal?
        if withdraw_amount > account_balance:
            print("Transaction Denied: Insufficient balance.")
        else:
            # If all checks pass, deduct the money and dispense cash
            account_balance = account_balance - withdraw_amount
            print("Transaction Successful! Please collect your cash.")
            print(f"Remaining balance: {account_balance}")