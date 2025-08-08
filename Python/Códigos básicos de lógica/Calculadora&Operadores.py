operador = input("Qual é o operador da conta?:  ")
if operador != "+" and operador != "-" and operador != "*" and operador != "/":
    print("Eu ainda não sei fazer contas com esse tipo de operador!! ")
    exit()
else:
    first = int(input("Qual é o primeiro número a ser calculado?:   "))
    second = int(input("E o segundo?  "))

if operador == "+":
    first + second
    print((first)+(second))

elif operador == "-":
    first - second
    print((first)-(second))

elif operador == "*":
    first * second
    print((first)*(second))

elif operador == "/":
    first * second
    print((first)/(second))
