# TIPOS DE DADOS
#nossos códigos serão escrito aqui
from time import process_time_ns

#PYTHON É CASE SENSITIVE -> A a

#VARIAVEL RECEBE UM VALOR -> VARIAVEL REPRESENTA ESSE VALOR
numero = 10 # atribuindo um valor 10
#SOMAR
numero = numero + 1 # atribuindo o resultado da soma, 11
#SUBTRAIR
numero = numero - 1 # atribuindo o resultado da subtração, 10
#COMPARAR
resultado = numero > 10 # atribuindo o resultado da COMPARAÇÃO


#CALCULADORA
primeiro_numero = 9
segundo_numero = 2

#soma
resultado_soma = primeiro_numero + segundo_numero
print(resultado_soma)
#subtração
resultado_sub = primeiro_numero - segundo_numero
print(resultado_sub)
#divisão
resultado_div = primeiro_numero / segundo_numero
print(resultado_div)
#multiplicação
resultado_multi = primeiro_numero * segundo_numero
print(resultado_multi)
#COMPARAÇÃO
resultado_comparacao = primeiro_numero > segundo_numero
print(resultado_comparacao)

#pedir um valor
#POR PADRÃO, O VALOR NO CONSOLE É UM STRING -> str
valor = input("Digite algum valor: ")
#pedir outro valor
#definir o ÚNICO TIPO DE DADO (inteiro) aceito no CONSOLE
valor_inteiro = int(input("Digite algum valor: "))

#TYPE
#FUNÇÃO RETORNA UM VALOR
#DECLARANDO UMA FUNÇÃO > nome()
#print() -> retorna um texto no console
#type() -> retorna o tipo do valor
print(type(resultado_soma))
print(type(resultado_sub))
print(type(resultado_div))
print(type(resultado_multi))
print(type(resultado_comparacao))

print(type(valor))
print(type(valor_inteiro))










