semaforo = input("Qual a cor do semáforo?:  ")

if semaforo.lower() == "vermelho":
        print("Pare!")
elif semaforo.lower() == "amarelo":
        print("Atenção!")
elif semaforo.lower() == "verde":
        print("Prossiga!")
else:
        print("Cor inválida")
