lista_frutas = ["Maçã", "Banana", "Pera", "Melancia"]
print("----LISTA DE FRUTAS----")
print(lista_frutas)
print("-----------------------")

cesta_compras = []

while True:
    compra_frutas = input("Que frutas deseja comprar?," \
    " 'fim' para terminar:  ")
    if compra_frutas.lower() == 'fim':
         break
    
    cesta_compras.append(compra_frutas)

for fruta in cesta_compras:
     print(fruta)
