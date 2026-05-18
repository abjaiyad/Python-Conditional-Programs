# Write a program:

# ✅ Check largest among 4 numbers

# Example:

# Input: 10 45 23 5
# Output: Largest is 45

a,b,c,d = map(int, input("Enter four numbers (use spaces to saparate each number): ").split())

if a >= b and a >= c and a >= d:
    print(f"{a} is largest ")
elif b >= a and b >= c and b >= d:
    print(f"{b} is largest")
elif c >= a and c >= b and c >= d:
    print(f"{c} is largest")
else:
    print(f"{d} is largest")