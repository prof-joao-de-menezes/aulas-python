nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
# a média de notas do SENAI é 7
# a média de frequência 75% -> 200 (QUANTIDADE MÁXIMA DE PRESENÇA)
frequencia_digitada = int(input("Digite a quantide de frequencia: "))

media = (nota1 + nota2) / 2
porcentagem_frequen_min =(200 * 75) / 100 # 150

frequencia_do_aluno = (frequencia_digitada * 100) / 200

if frequencia_do_aluno >= 75 and media >= 7.0:
    print(f"A média do aluno foi: {media:.2f}."
          f"\nA frequencia do aluno foi: %{frequencia_do_aluno}."
          f"\nEle foi APROVADO com sucesso.")
else:
    print(f"A média do aluno foi: {media:.2f}."
          f"\nA frequencia do aluno foi: %{frequencia_do_aluno}."
          f"\nEle foi REPROVADO.")