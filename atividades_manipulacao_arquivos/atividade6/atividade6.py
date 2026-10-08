# ETAPA 1
import json # Módulo interno do python

with open("base1.json", 'r') as arquivo:
    dados1 = json.load(arquivo)

with open("base2.json", 'r') as arquivo:
    dados2 = json.load(arquivo)

with open("base3.json", 'r') as arquivo:
    dados3 = json.load(arquivo)

# ETAPA 2
lista_aniversariantes = []

for aniversariante in dados1:
    dicionario_aniversariante = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(dicionario_aniversariante)

for aniversariante in dados2:
    dicionario_aniversariante = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(dicionario_aniversariante)

for aniversariante in dados3:
    dicionario_aniversariante = {
        "nome": aniversariante['nome'],
        "aniversario": aniversariante['aniversario']
    }
    lista_aniversariantes.append(dicionario_aniversariante)

# ETAPA 3
with open("aniversariantes.json", 'w') as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)

# DESAFIO EXTRA
lista_aniversariantes.sort(key=lambda aniversariante: aniversariante['nome'])

# sobreescre a base de dados em orgem alfabética
with open("aniversariantes.json", 'w') as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)