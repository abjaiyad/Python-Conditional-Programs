# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

# Prompt the user to enter cost price
cost_price = float(input("Enter the cost price of the product: "))

# Prompt the user to enter selling price
selling_price = float(input("Enter the selling price of the product: "))

# Determine the profit or loss using if statement
if selling_price > cost_price:
    result = "profit"
elif selling_price < cost_price:
    result = "loss"
else:
    result = "no profit no loss"
# Display the result
print("You are in", result)