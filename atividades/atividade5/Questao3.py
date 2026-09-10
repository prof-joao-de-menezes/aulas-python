#SOMA DE NÚMEROS DIGITADOS

total_numeros = 0


numero_digitado = int(input("Digite um número a ser somado: "))

while numero_digitado != 0:
    total_numeros += numero_digitado
    numero_digitado = int(input("Digite outro número a ser somado: "))

print(f"A soma de todos os número é igual a {total_numeros}")