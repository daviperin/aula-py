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


print()
print()

# Etapa 6 - relacao entre desconto e valor da venda
desconto_ate_8 = vendas[vendas["Desconto"] <= 0.08]
desconto_8_a_12 = vendas[(vendas["Desconto"] > 0.08) & (vendas["Desconto"] <= 0.12)]
desconto_12_a_16 = vendas[(vendas["Desconto"] > 0.12) & (vendas["Desconto"] <= 0.16)]
desconto_acima_16 = vendas[vendas["Desconto"] > 0.16]
print(f"Valor médio da venda com desconto até 8%: {desconto_ate_8['Valor_Venda'].mean():.2f}")
print(f"Valor médio da venda com desconto de 8% a 12%: {desconto_8_a_12['Valor_Venda'].mean():.2f}")
print(f"Valor médio da venda com desconto de 12% a 16%: {desconto_12_a_16['Valor_Venda'].mean():.2f}")
print(f"Valor médio da venda com desconto acima de 16%: {desconto_acima_16['Valor_Venda'].mean():.2f}")
print(f"Faturamento por forma de pagamento: {vendas.groupby('Forma_Pagamento')['Valor_Venda'].sum().sort_values(ascending=False).round(2)}")
print(f"Ticket médio por forma de pagamento: {vendas.groupby('Forma_Pagamento')['Valor_Venda'].mean().round(2)}")

print()
print()

# Etapa 7 - avaliacao x desconto e valor da compra
print(f"Avaliação média com desconto até 8%: {desconto_ate_8['Avaliacao'].mean():.2f}")
print(f"Avaliação média com desconto de 8% a 12%: {desconto_8_a_12['Avaliacao'].mean():.2f}")
print(f"Avaliação média com desconto de 12% a 16%: {desconto_12_a_16['Avaliacao'].mean():.2f}")
print(f"Avaliação média com desconto acima de 16%: {desconto_acima_16['Avaliacao'].mean():.2f}")
print(f"Avaliação média em compras até R$ 200: {vendas[vendas['Valor_Venda'] <= 200]['Avaliacao'].mean():.2f}")
print(f"Avaliação média em compras de R$ 200 a R$ 400: {vendas[(vendas['Valor_Venda'] > 200) & (vendas['Valor_Venda'] <= 400)]['Avaliacao'].mean():.2f}")
print(f"Avaliação média em compras acima de R$ 400: {vendas[vendas['Valor_Venda'] > 400]['Avaliacao'].mean():.2f}")

print()
print()

# Etapa 8 - categorias por mes
print(f"Faturamento por mês e categoria:\n{vendas.groupby(['Mes', 'Categoria'])['Valor_Venda'].sum().round(2)}")


# Graficos
faturamento_loja = vendas.groupby('Loja')['Valor_Venda'].sum()
vendas_loja = vendas.groupby('Loja')['Valor_Venda'].count()
ticket_loja = vendas.groupby('Loja')['Valor_Venda'].mean()
avaliacao_loja = vendas.groupby('Loja')['Avaliacao'].mean()

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

axs[0, 0].bar(faturamento_loja.index, faturamento_loja.values, color='green')
axs[0, 0].set_title("Faturamento por Loja", fontsize=14, fontweight='bold')
axs[0, 0].set_ylabel("Faturamento (R$)", fontsize=12)
axs[0, 0].grid(True, linestyle='--', alpha=0.5)

axs[0, 1].bar(vendas_loja.index, vendas_loja.values, color='blue')
axs[0, 1].set_title("Número de Vendas por Loja", fontsize=14, fontweight='bold')
axs[0, 1].set_ylabel("Vendas", fontsize=12)
axs[0, 1].grid(True, linestyle='--', alpha=0.5)

axs[1, 0].bar(ticket_loja.index, ticket_loja.values, color='orange')
axs[1, 0].set_title("Ticket Médio por Loja", fontsize=14, fontweight='bold')
axs[1, 0].set_ylabel("Ticket médio (R$)", fontsize=12)
axs[1, 0].grid(True, linestyle='--', alpha=0.5)

axs[1, 1].bar(avaliacao_loja.index, avaliacao_loja.values, color='red')
axs[1, 1].set_title("Avaliação Média por Loja", fontsize=14, fontweight='bold')
axs[1, 1].set_ylabel("Nota média", fontsize=12)
axs[1, 1].grid(True, linestyle='--', alpha=0.5)

plt.show()


faturamento_categoria = vendas.groupby('Categoria')['Valor_Venda'].sum().sort_values()
faturamento_produto = vendas.groupby('Produto')['Valor_Venda'].sum().sort_values()

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

axs[0].barh(faturamento_categoria.index, faturamento_categoria.values, color='green')
axs[0].set_title("Faturamento por Categoria", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Faturamento (R$)", fontsize=12)

axs[1].barh(faturamento_produto.index, faturamento_produto.values, color='purple')
axs[1].set_title("Faturamento por Produto", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Faturamento (R$)", fontsize=12)

plt.show()


faturamento_vendedor = vendas.groupby('Vendedor')['Valor_Venda'].sum().sort_values()
desconto_vendedor = vendas.groupby('Vendedor')['Desconto'].mean().sort_values()

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

axs[0].barh(faturamento_vendedor.index, faturamento_vendedor.values, color='green')
axs[0].set_title("Faturamento por Vendedor", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Faturamento (R$)", fontsize=12)

axs[1].barh(desconto_vendedor.index, desconto_vendedor.values * 100, color='red')
axs[1].set_title("Desconto Médio por Vendedor", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Desconto (%)", fontsize=12)

plt.show()


plt.scatter(vendas["Desconto"] * 100, vendas["Valor_Venda"], marker='o', color='red')
plt.title("Desconto x Valor da Venda", fontsize=14, fontweight='bold')
plt.xlabel("Desconto (%)", fontsize=12)
plt.ylabel("Valor da Venda (R$)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


faturamento_mes = vendas.groupby('Mes')['Valor_Venda'].sum()
numero_vendas_mes = vendas.groupby('Mes')['Valor_Venda'].count()

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))

axs[0].plot(faturamento_mes.index, faturamento_mes.values, color='green', linestyle='-', marker='o')
axs[0].set_title("Faturamento Mensal", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Mês", fontsize=12)
axs[0].set_ylabel("Faturamento (R$)", fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.5)

axs[1].plot(numero_vendas_mes.index, numero_vendas_mes.values, color='blue', linestyle='-', marker='o')
axs[1].set_title("Número de Vendas por Mês", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Mês", fontsize=12)
axs[1].set_ylabel("Vendas", fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.5)

plt.show()


categorias = vendas['Categoria'].unique()

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

for i in range(len(categorias)):
    faturamento_categoria_mes = vendas[vendas['Categoria'] == categorias[i]].groupby('Mes')['Valor_Venda'].sum()
    axs[i // 2, i % 2].plot(faturamento_categoria_mes.index, faturamento_categoria_mes.values, color='green', linestyle='-', marker='o')
    axs[i // 2, i % 2].set_title(f"Faturamento Mensal - {categorias[i]}", fontsize=14, fontweight='bold')
    axs[i // 2, i % 2].set_xlabel("Mês", fontsize=12)
    axs[i // 2, i % 2].set_ylabel("Faturamento (R$)", fontsize=12)
    axs[i // 2, i % 2].grid(True, linestyle='--', alpha=0.5)

plt.show()
