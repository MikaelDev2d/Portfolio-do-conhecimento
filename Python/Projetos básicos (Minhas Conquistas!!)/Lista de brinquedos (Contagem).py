lista_de_brinquedos = []
contador = 0

while True:
    brinquedos = input("Diga seus brinquedos ou digite" \
    
    " 'fim' para encerrar a lista:  ")
    
    if brinquedos == "fim":
        break

    lista_de_brinquedos.append(brinquedos)

    for items in lista_de_brinquedos:
            contador += 1
            break
    
    print("------Aqui está sua lista!------")
    print(lista_de_brinquedos)
    print("--------------------------------")
    print(f"Você tem", {contador}, "brinquedos!")
