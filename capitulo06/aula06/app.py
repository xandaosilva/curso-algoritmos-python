list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_even, list_odd = [], []

def return_list_even(numbers):
    return list(filter(lambda number: number % 2 == 0, numbers))


def return_list_odd(numbers):
    return list(filter(lambda number: number % 2 != 0, numbers))

list_even = return_list_even(list_a)
list_odd = return_list_odd(list_a)

print(list_even)
print(list_odd)

