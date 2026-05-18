# Write a program that reads a number and reports whether it is odd or even.

num = int(input("Enter number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")