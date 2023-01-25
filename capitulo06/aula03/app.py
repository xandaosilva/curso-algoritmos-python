def print_name(name = "Alexandre"):
    print(f"Hello {name}")


def print_stairs(number):
    for i in range(0, number + 1):
        print("#" * i)


def sum_numbers(a, b, c = 10):
    print(a + b + c)

print_name()
print_name("Rogério")
print_stairs(5)
print_stairs(15)
sum_numbers(1, 2, 3)
sum_numbers(1, 2)
