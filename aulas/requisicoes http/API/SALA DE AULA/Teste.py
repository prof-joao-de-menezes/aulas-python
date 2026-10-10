import requests
import json

link = 'http://192.168.205.100:8080/usuarios'
link_cep = 'https://viacep.com.br/ws/01001000/json/'

# REQUISIÇÕES GET > busca informações na base de dados
resposta = requests.get(link)
print(f'STATUS BUSCA DADOS: {resposta}')

resposta = requests.get(link+'/1')
print(f'STATUS BUSCA DE DADOS POR ID {resposta.json()}')

# REQUISIÇÕES POST > insere informações na base de dados
# chaves aceitas na API da aula: 'nome', 'email'
meus_dados = {
    "nome": "Professor",
    "email": "professor@senai.com.br"
}
envio = requests.post(link, json=meus_dados)
print(f'STATUS ENVIO DE DADOS {envio}')

# REQUISIÇÃO PUT > atualiza informações EXISTENTES na base dados
dado_atualizado = {
    "nome": "João de Menezes Ferreira Júnior",
    "email": "emailsenai@senai.com.br"
}
atualizacao = requests.put((link+'/1'), json=dado_atualizado)

# REQUISIÇÃO DELETE > apaga alguma informação na base de dados
deletar = requests.delete(link+'/10')
print(f'STATUS DELETE {deletar.text}')

# ====================================================
# Fazendo buscas e salvado na minha base de dados

busca_cep = requests.get(link_cep)
busca_pessoa = requests.get(link+'/1')

lista_de_pessoas = []

lista_de_pessoas.append(busca_pessoa.json())
lista_de_pessoas.append(busca_cep.json())

print(lista_de_pessoas)

print(f'\n\nNome da pessoa: {lista_de_pessoas[0]['nome']}\n'
      f'CEP da pessoa: {lista_de_pessoas[1]['cep']}\n')

with open('pessoas.json', 'w', encoding='utf-8') as arquivo:
    json.dump(lista_de_pessoas, arquivo, indent=4, ensure_ascii=False)