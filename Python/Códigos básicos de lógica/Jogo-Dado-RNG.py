import random
dado_numero = random.randint(1,20)

resposta_texto = 0
resposta_texto = input("Você quer rodar o dado? (s/n):  ")

while resposta_texto == "s":
        print("Girando dado...")
        dado_numero = random.randint(1,20)
        resposta_texto = input(f"O dado caiu no {dado_numero} quer girar denovo?! (s/n):  ")
        
else:
    print("até mais!!")
    exit()
