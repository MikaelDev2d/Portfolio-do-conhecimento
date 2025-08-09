notas_aluno = []
notas1 = float(input("Qual é a nota do 1 bimestre?:  "))
notas2 = float(input("Qual é a nota do 2 bimestre?:  "))
notas3 = float(input("Qual é a nota do 3 bimestre?:  "))
notas4 = float(input("Qual é a nota do 4 bimestre?:  "))

media = (notas1 + notas2 + notas3 + notas4) / 4

print(f"\nBimestre 1: {notas1}, Bimestre 2: {notas2}, Bimestre 3: {notas3}, Bimestre 4: {notas4}")
print(f"A média é {media}")
