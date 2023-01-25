list_a = [1, 2, 3, 4, 5]
list_b = []
list_b = list_a[:]

print(f"List A - {list_a}")
print(f"List B - {list_b}")

list_b[0] = 0

print(f"List A - {list_a}")
print(f"List B - {list_b}")
