''' 🧠 Python Practice Question — Student Result System

Question:

Write a Python program that:

Takes marks of 5 subjects from the user:
English
Mathematics
Science
Computer
Hindi
Calculate:
Total Marks
Percentage
Display Grade using conditional statements:
Percentage	Grade
90 and above	A+
80 – 89	A
70 – 79	B
60 – 69	C
50 – 59	D
Below 50	Fail
Also show Result Status:
If any subject marks < 33 → Fail
Otherwise → Pass
'''

sub1 = float(input("Enter your English marks: "))
sub2 = float(input("Enter your Mathematics marks: "))
sub3 = float(input("Enter your Science marks: "))
sub4 = float(input("Enter your Computer marks: "))
sub5 = float(input("Enter your Hindi marks: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total_marks / 5

print("Your total marks is:", total_marks)
print("Your total percentage is:", percentage)

# Pass/Fail Check
if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 or sub5 < 33:
    print("Result: Fail")
    print("Grade: Fail")
else:
    print("Result: Pass")

    # Grade only if pass
    if percentage >= 90:
        print("Grade: A+")
    elif percentage >= 80:
        print("Grade: A")
    elif percentage >= 70:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    elif percentage >= 50:
        print("Grade: D")