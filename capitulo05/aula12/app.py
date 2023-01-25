list_itens = ["Porta", "Pneu", "Estepe", "Maçaneta", "Janela", "Chave", "Motor", "Marcha"]
item_a = input("O que deseja procurar primeiro? ")
item_b = input("O que deseja procurar depois? ")

for i in range(0, len(list_itens)):
    if list_itens[i] == item_a:
        print(f"{item_a} foi encontrado primeiro!")
        break
    elif list_itens[i] == item_b:
        print(f"{item_b} foi encontrado primeiro!")
        break


