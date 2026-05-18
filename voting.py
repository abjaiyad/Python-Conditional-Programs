# Question 1 — Voting Eligibility

age = int(input("Enter age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18:
    if citizen == "yes":
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("You are underage")