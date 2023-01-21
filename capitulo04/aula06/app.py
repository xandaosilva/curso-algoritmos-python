x, divisoes = int(input("Digite um número para saber se é primo: ")), 0

for i in range(1, x + 1):
    if x % i == 0:
        divisoes += 1

res = (f"O número {x} é primo.") if divisoes == 2 else (f"O número {x} não é primo.")
print(res)
