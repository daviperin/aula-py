import pandas as pd

caminho_excel = r"C:\Users\davif\Downloads\4ae91468-53a4-4b37-bda3-bc9c10b5c019.xlsx"

df = pd.read_excel(caminho_excel)

# ETAPA 1 - CONHECENDO A BASE

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isna().sum())

# Análise: a base tem valores ausentes em Custos e Ativos e os textos (Empresa, Setor, Estado) estao com os acentos corrompidos. Isso precisa ser observado e corrigido

# ETAPA 2 - PRIMEIRO DIAGNÓSTICO DAS EMPRESAS

print(df.describe())

receita_media = df["Receita"].mean()
print(receita_media)

lucro_medio = df["Lucro_Liquido"].mean()
print(lucro_medio)

print(df[df["Receita"] == df["Receita"].max()][["Empresa", "Receita"]])
print(df[df["Lucro_Liquido"] == df["Lucro_Liquido"].max()][["Empresa", "Lucro_Liquido"]])
print(df[df["Funcionarios"] == df["Funcionarios"].max()][["Empresa", "Funcionarios"]])

print(len(df[df["Lucro_Liquido"] > 0]))
print(len(df[df["Lucro_Liquido"] < 0]))

# Análise: Não, utilizar somente a receita como criterio de avaliação não é suficiente, pois algumas empresas com receita alta podem apresentar prejuizo ou uma taxa de Lucro baixa. Voce deve analisar juntamente da Receita o Lucro Liquido que é o resultado final da empresa, para ter uma visão mais completa do desempenho da empresa

# ETAPA 3 - INVESTIGANDO GRUPOS DE EMPRESAS

print(df[df["Receita"] > receita_media][["Empresa", "Receita"]])

print(df[df["Lucro_Liquido"] > 0][["Empresa", "Lucro_Liquido"]])

print(df[(df["Receita"] > receita_media) & (df["Lucro_Liquido"] > 0)][["Empresa", "Receita", "Lucro_Liquido"]])

print(df[df["Estado"] == "SP"][["Empresa", "Estado"]])

empresas_setor = df[df["Setor"] == "Tecnologia"]
print(empresas_setor[["Empresa", "Setor"]])

print(empresas_setor[empresas_setor["Receita"] == empresas_setor["Receita"].max()][["Empresa", "Receita"]])

# Análise: o filtro combinado, usando a receita e o luco parece o mais interessante, pois junta empresas grandes que também tem resultado positivo, e não somente um dos dois critérios isolados

# ETAPA 4 - CRIANDO NOVOS INDICADORES

df["Margem_Liquida"] = df["Lucro_Liquido"] / df["Receita"]
df["Receita_por_Funcionario"] = df["Receita"] / df["Funcionarios"]

df["Situacao"] = "Equilíbrio"
df.loc[df["Lucro_Liquido"] > 0, "Situacao"] = "Lucro"
df.loc[df["Lucro_Liquido"] < 0, "Situacao"] = "Prejuízo"

df["Receita_Acima_Media"] = 0
df.loc[df["Receita"] > receita_media, "Receita_Acima_Media"] = 1

print(df[["Empresa", "Margem_Liquida", "Receita_por_Funcionario", "Situacao", "Receita_Acima_Media"]].head())

print(df.sort_values("Margem_Liquida", ascending=False)[["Empresa", "Margem_Liquida"]].head())
print(df.sort_values("Receita_por_Funcionario", ascending=False)[["Empresa", "Receita_por_Funcionario"]].head())

# Análise: Não necessariamente, as empresas com maior Receita não são as mesmas com maior Margem Líquida. Receita mede o tamanho da venda e quanto dinheiro ele movimenta, Margem Líquida mede a eficiencia deste dinheiro 

# ETAPA 5 - O DESAFIO DA DIRETORIA

# Critérios escolhidos:
# 1) Receita_Acima_Media == 1 -> empresa tem porte relevante
# 2) Margem_Liquida acima da média da base -> empresa e rentável
# 3) Receita_por_Funcionario acima da média da base -> empresa e produtiva

margem_media = df["Margem_Liquida"].mean()
receita_funcionario = df["Receita_por_Funcionario"].mean()

empresas_criterios = df[df["Receita_Acima_Media"] == 1]
empresas_criterios = empresas_criterios[empresas_criterios["Margem_Liquida"] > margem_media]
empresas_criterios = empresas_criterios[empresas_criterios["Receita_por_Funcionario"] > receita_funcionario]

print(len(empresas_criterios))

df["Selecionada"] = 0
df.loc[empresas_criterios.index, "Selecionada"] = 1

tabela_resumo = df[df["Selecionada"] == 1][["Empresa", "Setor", "Estado", "Receita", "Lucro_Liquido", "Margem_Liquida", "Selecionada"]]
tabela_resumo = tabela_resumo.sort_values("Margem_Liquida", ascending=False)
print(tabela_resumo)

# A ordenação foi pela Margem_Liquida, pois dentro do grupo já selecionado ela mostra quem é mais rentável, sendo a mais interessante para olhar primeiro

# ETAPA 6 - ENTREGA PARA O CLIENTE

df_selecionadas = df[df["Selecionada"] == 1].sort_values("Margem_Liquida", ascending=False)
df_selecionadas.to_excel("empresas_selecionadas.xlsx", index=False)

# Conclusão:
# Das 150 empresas da base nem sempre quem fatura mais tem o melhor desempenho tem empresa grandes dando prejuízo. Filtrei por quem fica acima da média em três frentes: Receita, Margem Líquida e Receita por Funcionário. Sobraram 5 empresas que conseguem ser grandes e ainda usar bem os recursos. Dessas 5, a que tem a maior Margem Líquida é a que a consultoria deveria olhar primeiro
