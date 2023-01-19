inter, gremio = input().split(" ")
virtorias_inter, virtorias_gremio, empate, grenais = 0, 0, 0, 0
inter = int(inter)
gremio = int(gremio)

if inter > gremio:
    virtorias_inter += 1
elif gremio > inter:
    virtorias_gremio += 1
else:
    empate += 1

grenais += 1

print("Novo grenal (1-sim 2-nao)")
op = int(input())

while op == 1:
    inter, gremio = input().split(" ")
    inter = int(inter)
    gremio = int(gremio)

    if inter > gremio:
        virtorias_inter += 1
    elif gremio > inter:
        virtorias_gremio += 1
    else:
        empate += 1

    grenais += 1

    print("Novo grenal (1-sim 2-nao)")
    op = int(input())


print(f"{grenais} grenais")
print(f"Inter:{virtorias_inter}")
print(f"Gremio:{virtorias_gremio}")
print(f"Empates:{empate}")

if empate > virtorias_gremio and empate > virtorias_inter:
    print("Nao houve vencedor")
elif virtorias_inter > virtorias_gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")

