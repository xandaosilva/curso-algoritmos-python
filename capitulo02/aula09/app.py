name = input("Type your name: ")
number_x = int(input("Type value of X: "))
number_y = int(input("Type value of Y: "))
balance = float(input("Type your balance: "))
bonus = float(input("Type your bonus: "))
salary = float(input("Type your salary: "))
increase = int(input("Type your salary increase: "))
base = int(input("Type base: "))
pot = int(input("Type pow: "))

sum_x_y = number_x + number_y
new_balance = balance + bonus
new_salary = salary + (salary * (increase / 100))
res_base_pow = pow(base, pot)

print("Hi %s, well come to our system." % name)
print("%d + %d = %d" % (number_x, number_y, sum_x_y))
print("New balance is: R$%.2f" % new_balance)
print("New salary is: R$%.2f" % new_salary)
print("Pot: %d" % res_base_pow)
