senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada

if acesso_liberado:
    print("Acesso liberado com sucesso.")
else:
    print("Senha incorreta.")