with (open('alunos.txt', 'r') as arquivo):
    linhas = arquivo.readlines()
    valores_cada_linha = []

    for linha in linhas:
        linha = linha.strip()
        linha = linha.split(";")
        # linha[0] = nome
        # linha[1] = turma
        # linha[2 até 5] = notas bimestre
        # linha[6] = 'Aprovado' ou 'Reprovado'