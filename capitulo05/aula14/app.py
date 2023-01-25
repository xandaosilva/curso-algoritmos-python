list_a = [500, -20, 910, 33, -15, 10, 22, -100, 49, 720, 1000, 3000]

max_value, min_value = list_a[0], list_a[0]
max_value_aux, min_value_aux = max(list_a), min(list_a)

for i in list_a:
    if i > max_value:
        max_value = i

    if i < min_value:
        min_value = i


print(f"The max value in list A is: {max_value}")
print(f"The max value in list A is: {max_value_aux}")
print(f"The min value in list A is: {min_value}")
print(f"The min value in list A is: {min_value_aux}")
