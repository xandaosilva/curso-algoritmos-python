password = int(input("Type your password: "))

while password != 123456789:
    print("Invalid password!")
    password = int(input("Type your password: "))

print("Success!")
