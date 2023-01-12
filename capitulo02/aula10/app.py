balance = 359.56
deposit = float(input("Type the deposit value: "))
credit_card_bill = 125.98

balance += deposit
balance -= credit_card_bill

print("Your balance is R$%.2f" % balance)
