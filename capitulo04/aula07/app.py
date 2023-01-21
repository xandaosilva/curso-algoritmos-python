saque = int(input("Digite o valor do saque: "))
notas_de_100, notas_de_50, notas_de_20, notas_de_10, notas_de_1 = 0, 0, 0, 0, 0

while saque > 0:
    while saque >= 100:
        notas_de_100 += 1
        saque -= 100
    while saque >= 50:
        notas_de_50 += 1
        saque -= 50
    while saque >= 20:
        notas_de_20 += 1
        saque -= 20
    while saque >= 10:
        notas_de_10 += 1
        saque -= 10
    while saque >= 1:
        notas_de_1 += 1
        saque -= 1


print(f"Você receberá {notas_de_100} nota(s) de R$100.00")
print(f"Você receberá {notas_de_50} nota(s) de R$50.00")
print(f"Você receberá {notas_de_20} nota(s) de R$20.00")
print(f"Você receberá {notas_de_10} nota(s) de R$10.00")
print(f"Você receberá {notas_de_1} nota(s) de R$1.00")
