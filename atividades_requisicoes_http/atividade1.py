import requests, json

dicinario_dados_cep = []

with open('historico_pesquisa.json', 'r', encoding='utf-8') as arquivo:
    dicinario_dados_cep.append(json.load(arquivo))


nova_pesquisa = []

while True:
    cep_digitado = input('Digite o CEP: ')
    link = f'https://viacep.com.br/ws/{cep_digitado}/json/'
    resposta = requests.get(link)
    print(resposta.json())

    nova_pesquisa.append(resposta.json())
    dicinario_dados_cep.extend(nova_pesquisa)

    for dados in dicinario_dados_cep:
        print(f'\nLogradouro: {dados["logradouro"]}\n'
              f'Bairro: {dados["bairro"]}\n'
              f'Cidade: {dados["localidade"]}\n'
              f'Estado: {dados["estado"]}\n')

    with open('historico_pesquisa.json', 'w', encoding='utf8') as arquivo:
        json.dump(dicinario_dados_cep, arquivo, ensure_ascii=False, indent=4)

    opcao = input("Gite 'sair' para finalizar...")
    if opcao == 'sair':
        break