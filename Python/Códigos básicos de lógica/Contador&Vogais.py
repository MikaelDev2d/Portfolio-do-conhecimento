frase = input("Digite sua frase")

contador_vogais = 0

vogais = "aeiou"

for letra in frase.lower():

    if letra in vogais:
     contador_vogais += 1
 
print(contador_vogais)
