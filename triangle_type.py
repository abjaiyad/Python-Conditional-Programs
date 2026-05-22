# Triangle Type
# If valid triangle → print:
# Equilateral
# Isosceles
# Scalene

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# 1. Check if the triangle is valid
if (a + b > c) and (a + c > b) and (b + c > a):

    # 2. Check the type
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle! The sides don't connect.")