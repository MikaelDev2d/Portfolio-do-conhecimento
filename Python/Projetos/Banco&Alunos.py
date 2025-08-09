alunos = {}

while True:
    codigo_aluno = input("Qual é o código do aluno?  ")
    if codigo_aluno.lower() == 'pronto':
         break

    cpf_aluno = input("Digite o CPF do aluno:  ")
    nota_aluno = float(input("Digite a nota do aluno:  "))

    alunos[codigo_aluno] = {'CPF': cpf_aluno, 'Nota': nota_aluno}

print("\n--- Lista completa --- ")
for codigo, dados in alunos.items():
    print(f"Código do aluno: {codigo}")
    print(f"CPF: {dados['CPF']}")
    print(f"Nota: {dados['Nota']}")
    print("-----------------------")
