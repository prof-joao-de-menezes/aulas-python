dicionario_frutas = {
    "frutas": [
        {
            "nome": "maça",
            "tipo": []

        },
        {
            "nome": "banana",
            "tipo": ["prata", "nanica", "maça", "da terra"],
        }
    ]
}

# toda vez que for utilizar o for, percorremos um tipo de lista
for produto in dicionario_frutas["frutas"]:
    print(produto['nome'])
    for tipo in produto['tipo']:
        print(f'Tipo: banana {tipo}')