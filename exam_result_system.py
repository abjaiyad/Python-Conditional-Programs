# 🟡 Problem 2 — Exam Result System

# Take:

# marks
# attendance (%)

# Rules:

# marks ≥ 40 → pass check
# attendance ≥ 75 → Eligible
# otherwise → Not Eligible
# marks < 40 → Fail

marks = float(input("Enter your marks: "))
attendance = int(input("Enter your attendance(%): "))

if marks >= 40:
    if attendance >= 75:
        print("Eligible to Pass")
    else:
        print("Not Eligible due to low attendance")
else:
    print("Fail due to low marks")