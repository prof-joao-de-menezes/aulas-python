#IF e ELSE -> SE e SENÃO

#CASE SENSITIVE -> E != e
idade = int(input('Digite sua idade: '))

# criando uma condição na execução do código
if idade >= 18: # executa SE a resposta boleana for True
    if idade > 65:
        print("Desculpa senhor, você não pode entrar nessa balada.")
    else:
        print("Você pode entrar nessa balada.")
elif idade < 5:    # ELSE + IF -> elif
    print("Além de não entrar, você não pode andar sozinho!!!")
else:
    print("Você não pode entrar, é menor de idade.")

nome = input('Digite seu nome: ')

if nome == "":
    print("Por favor, digite um nome válido.")
elif nome == "Joao":
    print("Olha só, o dono da balada chegou.")
else:
    print("Olá "+ nome +"! Seja bem vindo a nossa balada.")










