import functions as fun
import calculator as calc
import random

operation_a, operation_b = fun.check_even_or_odd(2), fun.check_even_or_odd(3)
operation_c, operation_d, operation_e = calc.my_sum(7, 13), calc.my_sub(10, 8), calc.my_multi(5, 20)
operation_f, operation_g = calc.my_div(2, 0), calc.my_div(30, 2)
operation_h = random.randint(1, 10)

print(operation_a)
print(operation_b)
print(operation_c)
print(operation_d)
print(operation_e)
print(operation_f)
print(operation_g)
print(operation_h)
