def show_info(name, age, profession):
    return (f"Hello {name}, you are {age} years old and your profession is {profession}.")


def say_hello(name, age, profession, function):
    return function(name, age, profession)


def my_sum(*args):
    res = 0

    for i in args:
        res += i

    return res


def my_multiply(*args):
    res = 1

    for i in args:
        res *= i

    return res

operation_a = say_hello("Alexandre", 29, "web developer", show_info)
operation_b, operation_c = my_sum(1, 2, 3, 4, 5), my_sum(50, 50)
operation_d, operation_e = my_multiply(11, 2), my_multiply(2, 3, 4)

print(operation_a)
print(operation_b)
print(operation_c)
print(operation_d)
print(operation_e)
