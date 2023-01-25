list_a, list_b, list_c = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], []

for i in range(0, len(list_a)):
    list_c.append(list_a[i])

for i in range(0, len(list_b)):
    list_c.append(list_b[i])

print(list_a)
print(list_b)
print(list_c)

del list_c[0]
del list_c[len(list_c) - 1]

print(list_c)


