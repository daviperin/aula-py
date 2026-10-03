import matplotlib.pyplot as plt
import pandas as pd

caminho = r"C:\Users\davif\Downloads\661bc695-44b2-47f0-bc4d-2015abf56dfe.xlsx"
vendas = pd.read_excel(caminho, sheet_name="Vendas")
dicionario = pd.read_excel(caminho, sheet_name="Dicionario")
df = pd.DataFrame(vendas)
print(f"Quantidade de linhas: {df.shape[0]}, Quantidade de colunas: {df.shape[1]}")
print(f"Informações do DataFrame:\n{df.columns.tolist()}")
print(f"Tipos de dados das colunas:\n{df.dtypes}")
print(f"Existencia de valores ausentes:\n{df.isnull().sum()}")
print(f"Estatísticas descritivas das colunas numéricas:\n{df.describe().round(2)}")

print()
print()

vendas["Valor_Venda"] = vendas["Quantidade"] * vendas["Preco_Unitario"] *  (1 - vendas["Desconto"])
print(f"Faturamento total: {vendas['Valor_Venda'].sum():.2f}")
print(f"Quantidade total de produtos vendidos: {vendas['Quantidade'].sum()}")
print(f"Número de vendas realizadas: {vendas.shape[0]}")
print(f"Valor médio das vendas: {vendas['Valor_Venda'].mean():.2f}")
print(f"Desconto médio concedido: {vendas['Desconto'].mean():.2f}")
print(f"Avaliação média dos clientes: {vendas['Avaliacao'].mean():.2f}")

print()
print()

print(f"Faturamento de cada loja: {vendas.groupby('Loja')['Valor_Venda'].sum().round(2)}")
print(f"Número de vendas de cada loja: {vendas.groupby('Loja')['Valor_Venda'].count()}")
print(f"Quantidade de produtos vendidos de cada loja: {vendas.groupby('Loja')['Quantidade'].sum()}")
print(f"Ticket médio de cada loja: {vendas.groupby('Loja')['Valor_Venda'].mean().round(2)}")
print(f"Avaliação média dos clientes de cada loja: {vendas.groupby('Loja')['Avaliacao'].mean().round(2)}")

print()
print()

print(f"As categorias com maior faturamento: {vendas.groupby('Categoria')['Valor_Venda'].sum().sort_values(ascending=False).head(5)}")
print(f"As categorias com maior quantidade de produtos vendidos: {vendas.groupby('Categoria')['Quantidade'].sum().sort_values(ascending=False).head(5)}")
print(f"Os produtos com maior faturamento: {vendas.groupby('Produto')['Valor_Venda'].sum().sort_values(ascending=False).head(5)}")
print(f"Os produtos com maior quantidade vendida: {vendas.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(5)}")
print(f"Os produtos com maior número de vendas: {vendas.groupby('Produto')['Valor_Venda'].count().sort_values(ascending=False).head(5)}")

print()
print()

print(f"Faturamento de cada vendedor: {vendas.groupby('Vendedor')['Valor_Venda'].sum().round(2)}")
print(f"Número de vendas de cada vendedor: {vendas.groupby('Vendedor')['Valor_Venda'].count()}")
print(f"Quantidade de produtos vendidos de cada vendedor: {vendas.groupby('Vendedor')['Quantidade'].sum()}")
print(f"Ticket médio de cada vendedor: {vendas.groupby('Vendedor')['Valor_Venda'].mean().round(2)}")
print(f"Desconto médio concedido de cada vendedor: {vendas.groupby('Vendedor')['Desconto'].mean().round(2)}")

print()
print()

print(f"Desconto médio entre as lojas: {vendas.groupby('Loja')['Desconto'].mean().round(2)}")
print(f"Desconto médio entre as categorias: {vendas.groupby('Categoria')['Desconto'].mean().round(2)}")
print(f"Desconto médio entre os vendedores: {vendas.groupby('Vendedor')['Desconto'].mean().round(2)}")


print()
print()


print(f"Avaliacao media entre as Lojas: {vendas.groupby('Loja')['Avaliacao'].mean().round(2)}")
print(f"Avaliacao media entre as Categorias: {vendas.groupby('Categoria')['Avaliacao'].mean().round(2)}")
print(f"Avaliacao media entre os vendedores: {vendas.groupby('Vendedor')['Avaliacao'].mean().round(2)}")


print()
print()

vendas["Mes"] = vendas["Data"].dt.month
print(f"A evolução mensal do faturamento: {vendas.groupby('Mes')['Valor_Venda'].sum().round(2)}")
print(f"A evolução mensal do número de vendas: {vendas.groupby('Mes')['Valor_Venda'].count().round(2)}")
print(f"Os meses de maior faturamento: {vendas.groupby('Mes')['Valor_Venda'].sum().sort_values(ascending=False).head(5)}")
print(f"Os meses de menor faturamento: {vendas.groupby('Mes')['Valor_Venda'].sum().sort_values(ascending=True).head(5)}")
