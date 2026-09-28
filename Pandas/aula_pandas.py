import pandas as pd

serie = pd.Series([1, 2, 3, 4, 5, 6], index=["a", "b", "c", "d", "e", "f"])
print(serie)

data = {
    "Produto": [
        "Cafe",
        "Arroz",
        "Feijao",
    ],
    "Quantidade": [10, 20, 30],
    "Valor": [45, 15, 10],
}


df = pd.DataFrame(data)
# print(df)
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df.tail())
# print(df['Quantidade'])
# print(df[['Quantidade', 'Valor']])
# print(df.loc[0:1])
# print(df.iloc[0:1])



arquivo = pd.read_excel(r"C:\Users\davif\Downloads\dados_unificados.xlsx")

print(arquivo)
print(arquivo[arquivo['População 2022'] <10000] [['Municipio', 'População 2022']])

arquivo['superavit'] = arquivo['Total de receitas brutas 2024'] - arquivo['Total de despesas brutas 2024']

print(arquivo[['Municipio', 'superavit']])
print(arquivo[['População 2022', 'Escolarização 2022', 'PIB per capita 2021', 'superavit']].describe().round(2))
# arquivo.to_excel("arquivo_salvo.xlsx")
