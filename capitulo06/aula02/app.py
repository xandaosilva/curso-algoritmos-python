def sum_until_100(n):
    if n < 100:
        n += 1
        print(n)
        return sum_until_100(n)
    else:
        return n


operation_a = sum_until_100(90)

print(operation_a)
