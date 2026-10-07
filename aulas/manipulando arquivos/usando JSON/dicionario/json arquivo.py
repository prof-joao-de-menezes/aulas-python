# IMPORTANDO BIBLIOTECA, PACOTE, MÓDULO
# import -> nome da biblioteca
# como a biblioteca json é nativa do Python, nós não precisamos intalar ela no projeto
import json # JSON -> JavaScript Object Notation

dados_dicionario = [
    {
        'produto': 'Frango',
        'preco': 20.00,
        'em_estoque': True
    },
    {
        'produto': 'Carne',
        'preco': 45.00,
        'em_estoque': True
    },
    {
        'produto': 'Carne',
        'preco': 45.00,
        'em_estoque': True,
        'tipo': "Peixe"
    },
    {
        'produto': 'Arroz',
        'preco': 16.00,
        'em_estoque': True
    },
    {
        'produto': 'Carvao',
        'preco': 25.00,
        'em_estoque': True
    }
]

# escreve um documento json
# dump -> transforma um dicionário em json
with open('json_file.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_dicionario, arquivo, ensure_ascii=False, indent=4)
    print("Arquivo escrito\n")

# lê o documento json
# load -> transforma o arquivo JSON em dicionário python
with open('json_file.json', 'r', encoding='utf-8') as arquivo:
    novo_dicionario = json.load(arquivo)

# dumps -> transforma o texto python em arquivo json
for produto in novo_dicionario:
    if produto['produto'] == 'Carvao':
        produto['em_estoque'] = False
        produto['preco'] = 19.99
        produto['tipo'] = "Vegetal"
    print(produto['preco'])

with open('json_file.json', 'w', encoding='utf-8') as arquivo:
    json.dump(novo_dicionario, arquivo, ensure_ascii=False, indent=1)

dados_dicionario.append({
    'produto': 'Feijão',
    'preco': 199.99,
    'em_estoque': True
})

for produto in dados_dicionario:
    if produto['produto'] == 'Carne':
        produto['em_estoque'] = False

with open('json_file.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_dicionario, arquivo, ensure_ascii=False, indent=4)