# ATM Menu Driven Program

menu = input(""""
Hi! how can I help you.
1. Enter 1 for check balance.
2. Enter 2 for change pin.
3. Enter 3 for withdrawal.
4. Enter 4 for  exit.
""")

if menu == '1':
  print("Congrats you are fucking rich.")
  if menu == '1':
    print("Bank can't handle your balance.")
elif menu == '2':
  print("Enter your new pin.")
elif menu == '3':
  print("Your withdrawal in prosses.")
elif menu == '4':
  print("Exit! Thanks for visiting.")
else:
  print(" Sorry it is an incorrect input.")