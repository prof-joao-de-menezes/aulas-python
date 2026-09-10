# Jogo de adivinhação
while True: #sistema do jogo
    numero_secreto = 100
    numero_tentativas = 1
    numero_digitado = int(input("Tente adivinhar o número secreto: "))

    while numero_secreto != numero_digitado: #contador de tentativas
        print("Você errou, tente de novo.")
        numero_digitado = int(input("Tente adivinhar o número secreto: "))
        numero_tentativas += 1

    print(f"Parabens, você acertou o número em [{numero_tentativas}] tentativas.")
    print(f"Você ganhou, a senha era {numero_secreto}.")

    opcao = input("Quer que o programa finalize? (sim) (não)")
    if opcao == "sim":
        break