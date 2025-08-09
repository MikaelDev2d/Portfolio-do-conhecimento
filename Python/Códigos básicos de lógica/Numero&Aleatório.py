import random
desafio = random.randint(1,99)

print(desafio)

txt = 0
txt = int(input("Qual número estou pensando?:  "))

while txt != desafio:
    txt = int(input("Errado! tente novamente:  "))
else:
    print("Você acertou!! ")
    exit()
