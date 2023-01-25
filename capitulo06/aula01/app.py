def multiply(x, y):
    return x * y


def check_is_greater_or_less_then_ten(number):
    res = ""

    if number == 10:
        res = (f"{number} is equals to 10.")
    else:
        res = (f"{number} is greater then 10.") if number > 10 else (f"{number} is less then 10.")

    return res


def check_size_text(text):
    return ("It's a long text.") if len(text) >= 20 else ("It's a short text.")


def check_even_or_odd(number):
    return True if number % 2 == 0 else False


def return_list_even_and_odd(list_number):
    list_even, list_odd = [], []

    for i in list_number:
        list_even.append(i) if check_even_or_odd(i) else list_odd.append(i)

    return list_even, list_odd


def calc_average(list_number):
    return round((sum(list_number)/len(list_number)),2)


list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_b = [10, 20, 30]
operation_a, operation_b, operation_c, operation_d, operation_e = multiply(2, 3), multiply(20, 20), multiply(2, 70), multiply(11, 2), multiply(10, 3)
operation_f, operation_g, operation_h = check_is_greater_or_less_then_ten(11), check_is_greater_or_less_then_ten(3), check_is_greater_or_less_then_ten(10)
operation_i, operation_j = check_size_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec non ullamcorper enim."), check_size_text("Lorem")
operation_k, operation_l = return_list_even_and_odd(list_a)
operation_m, operation_n = calc_average(list_a), calc_average(list_b)

print(operation_a)
print(operation_b)
print(operation_c)
print(operation_d)
print(operation_e)
print(operation_f)
print(operation_g)
print(operation_h)
print(operation_i)
print(operation_j)
print(operation_k)
print(operation_l)
print(operation_m)
print(operation_n)
