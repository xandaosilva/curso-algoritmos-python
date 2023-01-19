number_a, number_b, number_c, number_d, number_e = 5, 2, 3, 4, 10
var_true, var_false, var_x, var_y, var_z = True, False, True, False, False

condition_a = not (number_a > number_b)
condition_b = not (number_a < number_b)
condition_c = not var_true
condition_d = not var_false
condition_e = number_b % 2 == 0 and number_d % 2 == 0
condition_f = number_c % 2 == 0 and number_d % 2 == 0
condition_g = number_a > number_e or number_e == 1
condition_h = number_e > number_a or number_e == 10
condition_i = number_a > number_e or number_e == 10
condition_j = number_e > number_a or number_e == 20
condition_k = var_x and var_y
condition_l = not var_x
condition_m = var_x and var_x
condition_n = var_y and var_y
condition_o = var_y or var_x
condition_p = var_y and var_z
condition_q = not var_y
condition_r = var_z and var_z

print(condition_a)
print(condition_b)
print(condition_c)
print(condition_d)
print(condition_e)
print(condition_f)
print(condition_g)
print(condition_h)
print(condition_i)
print(condition_j)
print(condition_k)
print(condition_l)
print(condition_m)
print(condition_n)
print(condition_o)
print(condition_p)
print(condition_q)
print(condition_r)
