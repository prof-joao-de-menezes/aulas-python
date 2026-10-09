# FUNÇÕES
def adicionar_aluno():
    nome = input('Digite o nome do aluno: ')
    turma = input('Digite o turma do aluno: ')
    nota_1bim = float(input('Digite o nota do 1º Bimestre do aluno: '))
    nota_2bim = float(input('Digite o nota do 2º Bimestre do aluno: '))
    nota_3bim = float(input('Digite a nota do 3º Bimestre do aluno: '))
    nota_4bim = float(input('Digite a nota do 4° Bimestre do aluno: '))
    media = (nota_1bim + nota_2bim + nota_3bim + nota_4bim) / 4
    if media >= 7:
        status = 'Aprovado'
    else:
        status = 'Reprovado'
    # ABRINDO ARQUIVO alunos.txt
    # escrita -> 'w' ->  sobreescreve tudo no documento pela linha nova
    # escrita -> 'a' -> adiciona uma linha novas
    # leitura -> 'r' -> lê tudo no documento.txt como STRING
    with open('alunos.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{nome};{turma};{nota_1bim};{nota_2bim};{nota_3bim};{nota_4bim};"
                      f"{status}\n")

def lista_nomes_alunos():
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
        lista_alunos = arquivo.readlines() # lê linha por linha e adiciona numa lista
        # lista_alunos = ['João de Menezes;999;10.0;9.0;8.0;7.0;Aprovado\n']

        for aluno in lista_alunos:
            aluno = aluno.strip() # retira o \n do texto
            aluno = aluno.split(';') # separa atributos em indexes por entre os ';'
            # lista_alunos = ['João de Menezes',999,10.0,9.0,8.0,7.0,'Aprovado']

            print(f'{aluno[0]}\n')

def buscar_por_nome():
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
        nome_busca = input('Digite o nome do aluno desejado: ')
        lista_alunos = arquivo.readlines()

        for aluno in lista_alunos:
            aluno = aluno.strip().split(';')

            if nome_busca == aluno[0]:
                print(f'O aluno {aluno[0]} tem o status de: {aluno[6]}')

def maior_media():
    turma_digitada = input('Digite o turma do aluno: ')
    with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
        lista_alunos = arquivo.readlines()
        lista_media_alunos = []
        aluno_destaque = []
        maior_media = 0

        for aluno in lista_alunos:
            aluno = aluno.strip().split(';')
            if aluno[1] == turma_digitada:
                media = (float(aluno[2]) + float(aluno[3]) + float(aluno[4]) + float(aluno[5])) / 4
                nome = aluno[0]
                lista_media_alunos.append([nome, media])

                if media > maior_media:
                    maior_media = media
                    aluno_destaque.append(aluno[0])
                    aluno_destaque.append(media)

        len_nome = (len(aluno_destaque) - 2)
        len_media = (len(aluno_destaque) - 1)
        print(f"A maior maior media foi o aluno {aluno_destaque[len_nome]} com a média {aluno_destaque[len_media]}")

# SISTEMA
while True: # loop infinito
    opcao = int(input("Escolha uma opcao:\n"
                      "1) Adicionar aluno\n"
                      "2) Listar nomes\n"
                      "3) Buscar por nome\n"
                      "4) Maior media\n"
                      "5) Sair\n"
                      "\nDigite: "))

    match opcao:
        case 1:
            adicionar_aluno()
        case 2:
            lista_nomes_alunos()
        case 3:
            buscar_por_nome()
        case 4:
            maior_media()
        case 5:
            print("Finalizando sistema...")
            break











