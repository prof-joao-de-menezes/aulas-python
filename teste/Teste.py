import pandas as pd

data = pd.read_csv("estoque_supermercado.csv")

data["setor"] = (
    data["setor"].str.lower().str.replace(" ", "")
)

print(data["setor"])
# print(data.info())

produto_limpeza = {
    'higiene': "Limpa",
    'açougue': "Carne"
}

data["ação do produto"] = data["setor"].map(produto_limpeza)

print(data.to_string())

# ultimo commit do repositório