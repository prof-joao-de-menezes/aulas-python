import json

# lendo arquivo txt
with open('banco_livros.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    catalogo_livros = []
    for linha in linhas:
        linha = linha.strip().split(';')
        catalogo_livros.append(
            {
                'id': int(linha[0]),
                'nome': linha[1],
                'descricao': linha[2],
                'preco': float(linha[3]),
                'em_estoque': int(linha[4])
            }
        )

novos_livros = [
    {
        'id': 31,
        'nome': "Clean Code",
        'descricao': "Educacao com codigos",
        'preco': 150.00,
        'em_estoque': 10
    },
    {
        'id': 32,
        'nome': "Diario de um banana",
        'descricao': "Livro de historias",
        'preco': 15.00,
        'em_estoque': 50
    }
]

catalogo_livros.extend(novos_livros)

with open('catalogo.json', 'w') as arquivo:
    json.dump(catalogo_livros, arquivo, indent=4)

with open('catalogo.json', 'r') as arquivo:
    livros = json.load(arquivo)
    valor_total_loja = 0

    for livro in livros:
        if livro["em_estoque"] <= 15:
            print(f'O livro: {livro["nome"]} tem menos de 15 no estoque.')

        valor_total_do_estoque = livro["em_estoque"] * livro["preco"]
        print(f"Valor total do estoque do livro {livro['nome']}: R${valor_total_do_estoque:.2f}\n")
        valor_total_loja += valor_total_do_estoque

    print(f"O valor de TODOS os livros fica em R${valor_total_loja:.2f}\n")