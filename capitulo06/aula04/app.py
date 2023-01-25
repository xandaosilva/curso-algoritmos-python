def sum(a, b):
    return a + b


def multiply(a, b):
    return a * b


def calc(a, b, function):
    return function(a, b)


operation_a = calc(10, 12, sum)
operation_b = calc(30, 4, multiply)

print(operation_a)
print(operation_b)
