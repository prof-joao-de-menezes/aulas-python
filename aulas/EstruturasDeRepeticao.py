# REPETIÇÃO WHILE -> Enquanto
# Estruturas de repetição
# Laços de repetição
# Loop

# ano_nascimento = 2004
# ano_final = 2077
#
# print("O ano atual é: ", ano_nascimento)
#
# idade = 0
# while ano_nascimento <= ano_final:
#     idade += 1
#     print(idade)
#     ano_nascimento += 1  # incremento
#
# print("O ano atual é: ", ano_nascimento

# seu_nome = input("Digite seu nome: ")
#
# while seu_nome != "Joao":
#     print("Pessoa não encontrada....")
#     seu_nome = input("Digite seu nome novamente: ")


fichas = 2
while fichas != 0: # sistema da maquina do fliperama
    tentativas = 3

    print(f"Você tem {fichas} quantidade de fichas.")
    while True: # sistema do jogo do fliperama
        print(f"Você tem {tentativas} tentativas.")
        opcao = input("Escolha uma opção:")
        if opcao == "b":
            print("Você ganhou!")
            fichas = 0
            break
        elif tentativas == 1:
            print("Você perdeu")
            break
        else:
            tentativas -= 1

    fichas -= 1
    if fichas <= 0:
        break










