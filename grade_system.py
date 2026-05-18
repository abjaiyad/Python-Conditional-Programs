# Make a program that reads three grades from a student and reports whether he passed 
# (final grade greater than or equal to 7), failed (final grade less than 4) or was in recovery (final grade between 4 and 7).

# Prompt the user to enter three grades
grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))

# Calculate the average grade
average_grade = (grade1 + grade2 + grade3) / 3

# Check the final result based on the average grade
if average_grade >= 7:
    result = "Pass"
elif average_grade < 4:
    result = "Fail"
else:
    result = "Recovery"

print("The student's final result is:", result)