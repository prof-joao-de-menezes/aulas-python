#OPERADORES MATEMÁTICOS
numero1 = 10
numero2 = 20

#SOMA
soma = numero1 + numero2
#SUBTRAÇÃO
subtracao = numero1 - numero2
#MULTIPLICAÇÃO
multiplicacao = numero1 * numero2
#DIVISÃO
divisao = numero1 / numero2 #3 / 2 -> 1.5
#DIVISÃO SEM NUMERO QUEBRADO
divisao_sem_numero_quebrado = numero1 // numero2 #3 / 2 -> 1
#RESTO
resto = numero1 % numero2 # 11 % 2 -> 1

# print("Soma dos números: ", soma)
# print("Subtração dos números: ", subtracao)
# print("Multiplicação dos números: ", multiplicacao)
# print("Divisão dos números: ", divisao)
# print("Divisão dos números: ", divisao_sem_numero_quebrado)
# print("Resto dos números: ", resto)

"""
    # OPERADORES RELACIONAIS
    esperar uma resposta de True ou False
    != -> se for diferente retorna True, se for igual retorna False
    == -> se for diferente retorna False, se for igual retorna True
    
    > -> se for maior retorna True, se for menor retorna False
    < -> se for menor retorna False, se for igual retorna True
    
    >= -> se for maior E igual retorna True, contrario retorna False
    <= -> se for menor E igual retorna True, contrario retorna False

--------------------------------------------------------------------------

    #OPERADORES LÓGICOS
    and -> se todas as comparações forem True, retorna True
    or -> se ao menos uma das comparações for Truwe, retorna True
    not
    
--------------------------------------------------------------------------

    # OPERADORES DE ATRIBUIÇÃO
    = -> atribui um valor à variável
    += -> atribuir um valor X NUMÉRICO à variável
    -= -> subtrair um valor X NUMÉRICO da variável
    *= -> mutiplicar um valor X pelo NÚMERO da variável
    /= -> dividir um valor X pelo NÚMERO da variável
    
"""

idade = 10
print("O valor da idade é: ",idade)
idade += 8 # 18 -> incremento
print("O valor da idade é: ",idade)
idade -= 8 # 10 -> decremento
print("O valor da idade é: ",idade)
idade *= 2 # 20
print("O valor da idade é: ",idade)
idade /= 2 # 10
print("O valor da idade é: ",idade)

# print(idade != 18) # False
# print(idade == 18) # True
# print(idade > 18)  # False
# print(idade < 18)  # False
# print(idade >= 18) # True