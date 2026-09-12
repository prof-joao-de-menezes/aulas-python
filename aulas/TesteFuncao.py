# ARQUIVO TesteFuncao.py
#      biblioteca
from aulas.Funcoes import soma, olaUsuario # hierarquia

olaUsuario("João")

while True:
    valor = soma()
    print(valor)
    opcao = input("Quer finalizar? y/n")
    if opcao == 'y':
        break
print("Finalizando execução.") # parâmetro
