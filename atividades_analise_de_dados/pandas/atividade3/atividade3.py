import pandas as pd

df_dados_despadronizados =  pd.read_csv("dados_despadronizados.csv")

df_dados_despadronizados.insert(2, "cpf_formatado", df_dados_despadronizados["cpf"].str.replace(r"\D", "", regex=True))
df_dados_despadronizados.insert(3, "cpf_validado", df_dados_despadronizados["cpf_formatado"].str.fullmatch(r"\d{11}"))

dados_salario_formatados = (df_dados_despadronizados["salario"]
                              .str.replace(r"[^\d,.\-]", "", regex=True)
                              .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                              .str.replace(r",",".", regex=False)) # NaN <NA>

dados_salario_formatados = pd.to_numeric(dados_salario_formatados, errors="coerce")
df_dados_despadronizados.insert(6, "salario_formatado", dados_salario_formatados)

dados_telefone_formatados = (
    df_dados_despadronizados["numero"].str.replace(r"\D", "", regex=True)
)

df_dados_despadronizados.insert(7, "numero_formatado", dados_telefone_formatados)
df_dados_despadronizados["numero_validado"] = (df_dados_despadronizados['numero_formatado'].str.fullmatch(r"\d{10,13}"))


# print(df_dados_despadronizados)
# mudando dados inválidos dentro do Data Frame
for index, linha in df_dados_despadronizados.iterrows():
    # isna procura tanto espaços com <NA> quanto NaN
    if pd.isna(linha["nome"]) or (linha["nome"].strip() == ""):
        print(f'No index {index} o NOME está sem valor.')
        novo_nome = input("Digite um nome para preencher esse espaço: ")
        df_dados_despadronizados.at[index, 'nome'] = novo_nome

    if pd.isna(linha["cpf_formatado"]):
        print(f'No index {index} o {df_dados_despadronizados.at[index,"nome"]} está sem CPF.')
        novo_cpf = input("Digite um CPF para preencher esse espaço: ")
        df_dados_despadronizados.at[index, 'cpf_formatado'] = novo_cpf
        df_dados_despadronizados.at[index, 'cpf'] = novo_cpf

    if pd.isna(linha["salario_formatado"]):
        while True:
            print(f'No index {index} o {df_dados_despadronizados.at[index, "nome"]} está sem SALÁRIO.')
            try:
                novo_salario = input("Digite o salário do funcionário: ")
                df_dados_despadronizados.at[index, 'salario_formatado'] = float(novo_salario)
                df_dados_despadronizados.at[index, 'salario'] = str(novo_salario)
                break
            except ValueError:
                print("Digite apenas números no salário!")

    if pd.isna(linha["numero_formatado"]):
        print(f'No index {index} o {df_dados_despadronizados.at[index,"nome"]} está sem NÚMERO CADASTRADO.')
        novo_numero = input("Digite o número do funcionário: ")
        df_dados_despadronizados.at[index, 'numero_formatado'] = novo_numero
        df_dados_despadronizados.at[index, 'numero'] = novo_numero

df_dados_despadronizados["salario_decimo_terceiro"] = df_dados_despadronizados["salario_formatado"]
df_dados_despadronizados["salario_anual"] = (df_dados_despadronizados["salario_formatado"] * 12) + df_dados_despadronizados["salario_decimo_terceiro"]

print("\n DADOS ATUALIZADOS")

print("SOMA DE TODOS OS SALÁRIOS: ", df_dados_despadronizados["salario_formatado"].sum())
print("MENOR SALÁRIO: ", df_dados_despadronizados["salario_formatado"].min())
print("MAIOR SALÁRIO: ", df_dados_despadronizados["salario_formatado"].max())
print("MÉDIA DOS OS SALÁRIOS: ", df_dados_despadronizados["salario_formatado"].mean())

print(df_dados_despadronizados.to_string())