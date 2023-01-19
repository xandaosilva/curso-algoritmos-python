n: int; quantidade: int; coelhos: int; ratos: int; sapos: int; total: int
tipo: str; p_coelhos: float; p_ratos: float; p_sapos: float

n = int(input())
coelhos, ratos, sapos = 0, 0, 0

def calc_percentual(especie, qtd):
    return (especie/qtd)*100

for i in range(1, n+1):
    quantidade, tipo = input().split(" ")
    quantidade = int(quantidade)
    tipo = str(tipo)

    if tipo == "C":
        coelhos += quantidade
    elif tipo == "R":
        ratos += quantidade
    else:
        sapos += quantidade


total = coelhos + ratos + sapos
p_coelhos, p_ratos, p_sapos = calc_percentual(coelhos, total), calc_percentual(ratos, total), calc_percentual(sapos, total)

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {p_coelhos:.2f} %")
print(f"Percentual de ratos: {p_ratos:.2f} %")
print(f"Percentual de sapos: {p_sapos:.2f} %")
