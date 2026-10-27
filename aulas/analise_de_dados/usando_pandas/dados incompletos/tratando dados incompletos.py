import pandas as pd

df_dados_incompletos = pd.DataFrame([
    {
        "nome": "João de Menezes",
        "cpf": "12345678978",
        "salario": "dez mil reais",
        "telefone": "# $ *(){",
        "modelo_trabalho": "presencial",
        "data_admissao": "10/10/2026"
    },
    {
        "nome": "Victor Sousa",
        "cpf": 11122233344,
        "salario": "5.000,88",
        "telefone": "+55 62 12345-1234",
        "modelo_trabalho": "presencial",
        "data_admissao": "04/06/2020"
    },
    {
        "nome": "Marcelo Oliveira",
        "cpf": "cpf",
        "salario": 1000.9900,
        "telefone": "63 1111-1111",
        "modelo_trabalho": "",
        "data_admissao": "01/01/2026"
    }
])

df_dados_incompletos.to_csv("dados_incompletos.csv", index=False)

dados = pd.read_csv("dados_incompletos.csv",
                    dtype={"cpf": str,
                           "salario": "string",
                           "telefone": "string"})

# dados["cpf_formatado"] = (dados["cpf"]
#                           .str.replace(".", "")
#                           .str.replace("-", "")
#                           .str.replace(" ", ""))

dados.insert(2, "cpf_formatado", dados["cpf"].str.replace(r"\D", "", regex=True))
dados.insert(3, "cpf_validado", dados["cpf_formatado"].str.fullmatch(r"\d{11}"))

dados_salario_formatados = (dados["salario"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                              .str.replace(r",",".", regex=False)) # NaN <NA>
dados_salario_formatados = pd.to_numeric(dados_salario_formatados, errors="coerce")

dados.insert(5, "salario_formatado",dados_salario_formatados)

dados_telefone_formatados = (
    dados["telefone"].str.replace(r"\D", "", regex=True)
)

dados.insert(7, "telefone_formatado", dados_telefone_formatados)
dados["telefone_validado"] = (dados['telefone_formatado'].str.fullmatch(r"\d{10,13}"))

print(dados)

dados["salario_formatado"] = dados["salario_formatado"].fillna(0.0)
dados["modelo_trabalho"] = dados["modelo_trabalho"].fillna("home office")
print(dados[["cpf_formatado", "modelo_trabalho", "salario_formatado","data_admissao"]])

df_analise_salarial = dados[["nome", "salario_formatado", "data_admissao"]]
# df_analise_salarial = df_analise_salarial.drop(columns=["data_admissao"])
df_analise_salarial = df_analise_salarial.dropna()

# df["coluna data"] = pd.to_datetime(df["data"], format="%Y-%m-%d")
# nossa formatação atual 04/06/2026
df_analise_salarial["data_admissao"] = pd.to_datetime(
    df_analise_salarial["data_admissao"],
    format="%d/%m/%Y"
    # %d -> vai ler DIAS do mês com o formado de 01 até 31
    # %m -> vai ler os meses com o formato de 01 até 12
    # %Y -> vai ler os ANOS com o formato de 4 digitos
    # %y -> vai ler os ANOS com formato de 2 digitos
)
filtro_por_data = df_analise_salarial[
    (df_analise_salarial["data_admissao"] >= "01/01/2026") &
    (df_analise_salarial["data_admissao"] <= "01/03/2026")
]
print(dados.columns.tolist())
print(filtro_por_data.info())