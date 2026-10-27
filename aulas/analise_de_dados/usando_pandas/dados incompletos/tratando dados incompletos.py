import pandas as pd

df_dados_incompletos = pd.DataFrame([
    {
        "nome": "João de Menezes",
        "cpf": "12345678978",
        "salario": "dez mil reais",
        "telefone": "# $ *(){"
    },
    {
        "nome": "Victor Sousa",
        "cpf": 11122233344,
        "salario": "5.000,88",
        "telefone": "+55 62 12345-1234"
    },
    {
        "nome": "Marcelo Oliveira",
        "cpf": "cpf",
        "salario": 1000.9900,
        "telefone": "63 1111-1111"
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

print(dados["salario_formatado"])

dados_telefone_formatados = (
    dados["telefone"].str.replace(r"\D", "", regex=True)
)

dados.insert(7, "telefone_formatado", dados_telefone_formatados)
dados["telefone_validado"] = (dados['telefone_formatado'].str.fullmatch(r"\d{10,13}"))

print(dados.to_string())

print(f'Menor salário da base de dados: {dados["salario_formatado"].mean()}')