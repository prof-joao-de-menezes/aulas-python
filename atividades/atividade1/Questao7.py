# Questão 7: O Desconto da Loja
# Escreva um código que receba o valor total de uma compra (ex: 250.50). O programa deve calcular
# um desconto automático de 15% sobre esse valor. No final, exiba três dados na tela: O valor
# original da compra, o valor economizado (desconto) e o valor final que o cliente deverá pagar.

print("Calculo de desconto")

porcentagem_desconto = float(input("Digite o percentual de desconto: "))
valor_compra = float(input("Digite o valor do produto: "))
valor_economizado = porcentagem_desconto * valor_compra
valor_com_desconto = valor_compra - valor_economizado

print("O valor original da compra é: R$", valor_compra)
print("O valor do disconto foi de: R$", valor_economizado)
print("Você terá que pagar um total de: R$", valor_com_desconto)


