# REPETIÇÃO WHILE -> Enquanto
# while (comparação ou valor boleano)
# Executava caso fosse verdadeiro (True)





# Estruturas de repetição
# Laços de repetição
# Loop
from os import remove

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


# fichas = 2
# while fichas != 0: # sistema da maquina do fliperama
#     tentativas = 3
#
#     print(f"Você tem {fichas} quantidade de fichas.")
#     while True: # sistema do jogo do fliperama
#         print(f"Você tem {tentativas} tentativas.")
#         opcao = input("Escolha uma opção:")
#         if opcao == "b":
#             print("Você ganhou!")
#             fichas = 0
#             break
#         elif tentativas == 1:
#             print("Você perdeu")
#             break
#         else:
#             tentativas -= 1
#
#     fichas -= 1
#     if fichas <= 0:
#         break



#REPETIÇÃO FOR (para)

# for (item -> variável temporária) in (lista de valores):
#         index   0        1         2
lista_alunos = []
num_aluno = 0
num_aluno_final = 0
print("ADICIONANDO ALUNOS NA LISTA DE CHAMADA")
while True: # sisitema de adição
    while True: # adicionar alunos
        aluno = input("Digite o nome do aluno: ")
        lista_alunos.append(aluno)

        opcao = input("Deseja continuar? [S/N]: ") #finalizar adição
        if opcao == "N":
            break

    print("Lista atual dos alunos.")
    for i in lista_alunos: # imprime a lista de alunos total
        print(f"Nome do aluno {num_aluno}: {i}")
        num_aluno += 1

    print("Escolha uma opção:")

    opcao_match = input("a) apagar um aluno da chamada\n"
                        "b) adicionar um aluno da chamada\n"
                        "c) finalizar o programa\n")

    match opcao_match:
        case 'a':
            aluno_apagado = input("Digite o nome do aluno que deseja apagar: ")
            lista_alunos.remove(aluno_apagado)
            break
        case 'b':
            aluno_adicionado = input("Digite o nome do aluno que deseja adicionar: ")
            lista_alunos.append(aluno_adicionado)
            break
        case _:
            break

print("A sua turma ficou com todos esses alunos:")
for i in lista_alunos: # imprime a lista de alunos total
    print(f"Nome do aluno {num_aluno_final}: {i}")
    num_aluno_final += 1


































