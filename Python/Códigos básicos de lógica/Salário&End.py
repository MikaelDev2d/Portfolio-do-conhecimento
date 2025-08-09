salario = float(input("Qual seu salário?:  "))
if salario <= 3000:
    print("Você é junior!")
elif salario > 3000 and salario <=6000:
    print("Você é pleno!")
elif salario > 6000 and salario <= 15000:
    print("Você é senior!")
else:
    print("Dono de empresa :D !")
