import matplotlib.pyplot as plt
import pandas as pd 

clientes = pd.read_excel(r"C:\Users\davif\Downloads\aula_pandas_joins.xlsx", sheet_name="clientes")
pedidos = pd.read_excel(r"C:\Users\davif\Downloads\aula_pandas_joins.xlsx", sheet_name="pedidos")
populacao = pd.read_excel(r"C:\Users\davif\Downloads\aula_pandas_joins.xlsx", sheet_name="populacao")
area = pd.read_excel(r"C:\Users\davif\Downloads\aula_pandas_joins.xlsx", sheet_name="area")
vendas_jan = pd.read_excel(r"C:\Users\davif\Downloads\aula_pandas_joins.xlsx", sheet_name="vendas_jan")
vendas_fev = pd.read_excel(r"C:\Users\davif\Downloads\aula_pandas_joins.xlsx", sheet_name="vendas_fev")
vendas_mar = pd.read_excel(r"C:\Users\davif\Downloads\aula_pandas_joins.xlsx", sheet_name="vendas_mar")

vendas_por_cidade = pd.merge(pedidos, clientes, on="id_cliente").groupby("cidade")["valor"].sum().reset_index()

valor_total_jan = 0
for i in range(vendas_jan['vendas'].shape[0]):
    valor_total_jan += vendas_jan['vendas'][i]
valor_total_fev = 0
for i in range(vendas_fev['vendas'].shape[0]):
    valor_total_fev += vendas_fev['vendas'][i]
valor_total_mar = 0
for i in range(vendas_mar['vendas'].shape[0]):
    valor_total_mar += vendas_mar['vendas'][i]
    
dados = [valor_total_jan, valor_total_fev, valor_total_mar]
mes = ["Janeiro", "Fevereiro", "Março"]

fig,axs = plt.subplots(nrows=2, ncols=2, figsize=(12,8))

axs[0,0].scatter(populacao["cidade"], populacao["pop_mil"], marker='o', color='red')
axs[0,0].set_title("População por Cidade", fontsize=14, fontweight='bold')
axs[0,0].set_xlabel("Cidade", fontsize=12)
axs[0,0].set_ylabel("População (milhares)", fontsize=12)
axs[0,0].grid(True, linestyle='--', alpha=0.5)

axs[0,1].pie(vendas_por_cidade["valor"], labels=vendas_por_cidade["cidade"], autopct='%1.1f%%')
axs[0,1].set_title("Vendas por Cidade", fontsize=14, fontweight='bold')

axs[1,0].plot(pedidos["data"], pedidos["valor"], color='green', linestyle='-', marker='o')
axs[1,0].set_title("Valor do Pedido por Data", fontsize=14, fontweight='bold')
axs[1,0].set_xlabel("Data", fontsize=12)
axs[1,0].set_ylabel("Valor (R$)", fontsize=12)
axs[1,0].grid(True, linestyle='--', alpha=0.5)

axs[1,1].bar(mes, dados, color='green')
axs[1,1].set_title("Vendas vs Mes", fontsize=14, fontweight='bold')
axs[1,1].set_xlabel("Mes", fontsize=12)
axs[1,1].set_ylabel("Total de Vendas", fontsize=12)
axs[1,1].grid(True, linestyle='--', alpha=0.5)

plt.show()


plt.stem (area["cidade"], area["area_km2"],)
plt.title("Cidade por km²")
plt.xlabel("Cidade")
plt.ylabel("Área (km²)")
plt.show()  


