# Write a program that asks for a person's height and weight and calculates their body mass index (BMI),
# displaying the corresponding category (underweight, normal weight, overweight, obese, severely obese).
# Underweight: Below 18.5, Normal Weight: 18.5 to 24.9, Overweight: 25.0 to 29.9, Obese: 30.0 or higher

# Prompt the user to enter their height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate the BMI using the formula BMI = weight / (height^2)
bmi = weight / (height ** 2)

# Determine the corresponding BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
elif bmi < 35:
    category = "Obese"
else:
    category = "Severely obese"

# Display the BMI and category
print("Your BMI is:", bmi)
print("Category:", category)