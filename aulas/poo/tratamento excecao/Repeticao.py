while True:
    valor = ""
    try:
        valor = int(input("Digite a senha: "))
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
    finally: # executa se tiver erro ou não
        if valor == 1234:
            break