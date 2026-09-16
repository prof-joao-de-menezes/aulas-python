# ARQUIVO TesteFuncao.py
#      biblioteca
from aulas.programacao_estruturada.Funcoes import soma, olaUsuario # hierarquia

olaUsuario("João", 22)

while True:
    valor = soma()
    print(valor)
    opcao = input("Quer finalizar? y/n")
    if opcao == 'y':
        break
print("Finalizando execução.") # parâmetro
