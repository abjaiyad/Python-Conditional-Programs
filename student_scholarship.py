# 🔥 Problem 4

# Create a Student Scholarship Program:

# Input:

# marks
# family income

# Rules:

# marks ≥ 90
# income < 300000 → Full Scholarship
# otherwise → Half Scholarship
# marks 75–89 → Partial Scholarship
# below 75 → No Scholarship

marks = int(input("Enter marks: "))
family_income = float(input("Enter your family income: "))

if marks >= 90:
    if family_income < 300000:
        print("Full Scholarship")
    else:
        print("Half Scholarship")
elif marks >= 75:
    print("Partial Scholarship")
else:
    print("No Scholarship")