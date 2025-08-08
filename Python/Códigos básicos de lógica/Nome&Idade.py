apresentacao = input("Olá tudo bem? Você pode se apresentar para nós? (s/n):  ")
if apresentacao == "s":
  print("Certo! vamos lá!")
  nome = input("Qual é o seu nome aventureiro?:  ")
  print(f"Uau {nome} é um nome bem chique!")
  idade = int(input("Qual é a sua idade?:  "))
  if idade >= 18:
                print(f"Vejo que você é de maior {nome}!, Muito obrigado(a) por participar do nosso experimento em python!")
  else:
                print(f"Vejo que você é de menor {nome}! Muito obrigado(a) por participar do nosso experimento em python!")
else:
  print("Tudo bem! até a próxima vez!  ")
  print("Diálogo encerrado...  ")
  exit()


