quer_desafio = input("Você quer um desafio? (s/n): ")
if quer_desafio == "s":
    resposta = input("Qual é a montanha mais alta do planeta? ")
    if resposta == "monte everest":
        print("Você acertou!")
    else:
        print("Você errou!")
elif quer_desafio == "n":
    print("Talvez na próxima!")
