number_a = 5
number_b = 3
number_c = 10
number_d = 2
number_x = int(input("Type a number: "))
number_y = int(input("Type a number: "))
number_z = int(input("Type a number: "))

if number_x == 0:
    print("Null")
elif number_x > 0:
    print("Positive")
else:
    print("Negative")


if number_y == number_z:
    print("Equals")
else:
    print("Different")


print(number_a > number_b)
print(number_c == number_a)
print(number_d != number_a)
print(number_a <= number_c)
print(number_b > number_c)
print(number_a != number_c)
print(number_d >= number_a)
print(number_d != number_b)
print(number_d < number_c)
print(number_b >= number_a)
