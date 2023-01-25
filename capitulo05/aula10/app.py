list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(0, len(list_a)):
    if list_a[i] == 4:
        del list_a[i]
        break


print(list_a)
