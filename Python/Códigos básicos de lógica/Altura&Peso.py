peso = float(input("Qual é o seu peso companheiro?:  "))
if peso < 60.0:
             print(f"{peso}? Você é leve como uma folha!")
if peso >= 60.0:
             print(f"{peso}? Você está na média global do peso!")
if peso >= 80.0:
             print(f"{peso}? Você está acima do peso!")
             
altura = float(input("Qual é a sua altura?:  "))
if altura < 1.55:
             print(f"{altura}? Você é baixinho(a)!") 
if altura >= 1.55:
             print(f"{altura}? Você está na média de altura!")
if altura >= 1.75:
             print(f"{altura}? Você é bem alto!")

info = input("Você quer imprimir suas informações? (s/n):  ")
while info != "s" and "n":
  info = input("Incorreto, resposta com (s/n):  ")
  if info == "s":
    print(f"Seu peso é {peso} e sua altura é {altura}!")
    exit()
  if info == "n":
    print("até mais!!")
    exit()

#No código acima contém um problema proposital, se eu digo que minha altura é 1.80, então o python reconhece
#que é maior do que 1.55 e 1.75, oque retorna as duas prints de que estou na média e de que sou alto! 
#a mesma coisa acontece com o peso!
