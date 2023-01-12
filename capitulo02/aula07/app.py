import math

phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
velocity = input("Type your velocity: ")
var_a = 15
var_b = 7
sum_a_b = var_a + var_b
pi = math.pi
name = "Alexandre Rogério"
age = 29
money = 3150.37
savings = 10000.50
credit_card_bill = 6800
interest = 75.00

print(len(phrase))
print(phrase[0], phrase[1], phrase[2], phrase[3], phrase[4])
print("You are running at " + velocity + "Km/h")
print(f"{var_a} + {var_b} = {sum_a_b}")
print("%d + %d = %d" % (var_a, var_b, sum_a_b))
print("Value of pi is %.2f" % pi)
print("Hi, my name is %s, I'am %d years old and I have R$%.2f in my bank account." % (name, age, money))
print("You have R$%.2f, your credit card bill is R$%.2f and the interest is R$%.2f" % (savings, credit_card_bill, interest))
