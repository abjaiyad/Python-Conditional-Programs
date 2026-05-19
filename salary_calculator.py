# Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%
# Take CTC input in Lakhs
ctc = float(input("Enter your CTC (in Lakhs): "))

# Convert Lakhs to Rupees
ctc_rupees = ctc * 100000

# ---- Deductions ----
hra = 0.10 * ctc_rupees
da = 0.05 * ctc_rupees
pf = 0.03 * ctc_rupees

total_deduction = hra + da + pf

salary_after_deduction = ctc_rupees - total_deduction

# ---- Tax Calculation ----
if ctc < 5:
    tax_rate = 0
elif ctc <= 10:
    tax_rate = 0.10
elif ctc <= 20:
    tax_rate = 0.20
else:
    tax_rate = 0.30

tax = salary_after_deduction * tax_rate

# Final Salary
final_salary_yearly = salary_after_deduction - tax

# Monthly Salary
monthly_salary = final_salary_yearly / 12

# Output
print("\n----- Salary Details -----")
print(f"Salary after deductions: ₹{salary_after_deduction:.2f}")
print(f"Tax Amount: ₹{tax:.2f}")
print(f"In-hand Monthly Salary: ₹{monthly_salary:.2f}")