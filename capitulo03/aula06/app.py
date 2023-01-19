x = int(input("Type x :"))
y = int(input("Type y :"))
multi = x * y

res = (f"{multi} is small.") if multi <= 100 else (f"{multi} is big.")
print(res)
