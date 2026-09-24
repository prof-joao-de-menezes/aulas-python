# TRATAMENTO COM TRY E EXCPETS
try: # Executa esse bloco de código
    numero = int(input("Insira o numero do produto: "))
    divisao = 100 / numero
    print(divisao)
except ZeroDivisionError: # Pega um erro específico de divisão por 0
    print("Erro: impossível dividir por 0")
except ValueError:
    print("Erro: impossível divir com esse valor")
except Exception as erro: # qualquer erro não listado
    print(f"Erro inesperado: {erro}")
finally: # se der erro ou não, é executado
    print("Fim do seu código.")
