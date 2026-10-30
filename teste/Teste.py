import pandas as pd

base_de_dados = "customers-10000.csv"
df_clientes = pd.read_csv(base_de_dados, dtype={"Subscription Date": str})
# print("COLUNAS POSSÍVEIS PARA TRABALHAR")
# print(df_clientes.columns.tolist())
# print("Iinformações da DF")
# print(df_clientes.info())

lista_paises = df_clientes['Country'].unique().tolist()
lista_paises.sort()

# filtrar apenas com linhas ondes o país seja Brazil
valores_brasil = df_clientes[
    (df_clientes["Country"] == "Brazil")
]

valores_brasil['Subscription Date'] = pd.to_datetime(
    valores_brasil["Subscription Date"],
    format="%Y-%m-%d"
)

# filtragem por data
clientes_brasil_vencendo = valores_brasil[
    valores_brasil["Subscription Date"] <= "2022-01-01"
]

def mandar_email_clientes_vencimento(email):
    limitador_de_colunas = ['Customer Id','First Name','Email','Subscription Date','Website']
    cliente = clientes_brasil_vencendo[limitador_de_colunas]

    for index, linha in cliente.iterrows():
        if linha["Email"] == email:
            print(f"Olá cliente {linha["First Name"]} com o ID {linha['Customer Id']}."
                  f"\n\nSeu site com o domínio {linha["Website"]}"
                  f" está contratado desde de {linha['Subscription Date']}."
                  f"\n Contrao venceu no ano de 2026."
                  f" | faça a renovação com o nosso contato de imediato.")


map_continente ={
    "Brazil": "America do Sul",
    "Argentina": "America do Sul",
    "Bolivia": "America do Sul",
    "Albania": "Africa",
    "Angola": "Africa",
    "Australia": "Oceania",
    "Austria": "Oceania",
    "Japan": "Asia",
    "Korea": "Asia",
    "France": "Europa",
    "Armenia": "Europa"
}

# conferir se está achando os paises
# por_continente = df_clientes["Country"].isin(map_continente.keys())

df_clientes["Continente"] = df_clientes["Country"].map(map_continente)

clientes_continetes = df_clientes[
    (df_clientes["Continente"].isin(map_continente.values()))
]


clientes_asia = clientes_continetes[
    clientes_continetes["Continente"] == "Asia"
]

clientes_america_sul = clientes_continetes[
    clientes_continetes["Continente"] == "America do Sul"
]



print(f'Clientes por Continete: {len(clientes_continetes)}'
      f'\nClientes da ASIA: {len(clientes_asia)}'
      f'\nClientes da Ameria do Sul: {len(clientes_america_sul)}')
