import json # só pra escrever o arquivo json
import requests # Módulo EXTERNO -> Faz requisições HTTP

cep_digitado = 73040130
link = f'https://viacep.com.br/ws/{cep_digitado}/json/'
resposta = requests.get(link) # 200, 300, 400...
if resposta.status_code == 200: # retorna o código de retorno
    print('Requisição feita com sucesso!')
else:
    print("Erro na requisição")
print(resposta.json()) # printa em dicionário

with open('dados_cep.json', 'w', encoding='utf-8') as arquivo:
    json.dump(resposta.json(), arquivo, ensure_ascii=False, indent=4)