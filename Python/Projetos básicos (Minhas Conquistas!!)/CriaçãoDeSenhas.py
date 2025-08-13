while True:
    senha = input("Crie uma senha, (mínimo 5 caracteres):  ")
    if len(senha) < 5:
            print("Inválido, senha menor que 4 caracteres:  ")      
    else:
        confirmar = input("Confirme a senha:   ")
        while confirmar != senha:
             print("Senha não confere")
             break
        else:
             print("Cofre desbloqueado!")
             exit()
