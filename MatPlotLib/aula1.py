import matplotlib.pyplot as plt
import pandas as pd 

# plt.plot([1,2,3,4,5], [10,20,30,40,50])
# plt.plot([1,2,3,4,5], [10,20,30,40,50], color='blue', linestyle='--', marker='o')
# plt.scatter ([1,2,3,4,5], [10,20,30,40,50], marker='^', color='red')
# plt.title("Nome do Grafico")
# plt.xlabel("Eixo X")
# plt.ylabel("Eixo Y")
# plt.show()  

# dados = [12,15,13,18,22,21,22,23,25,25,27,30,33,35,40]

# plt.hist(dados, bins=5, color='blue', edgecolor='black')
# plt.title("Nome do Grafico")
# plt.xlabel("Eixo X")
# plt.ylabel("Eixo Y")
# plt.show()

# x = ["A", "B", "C", "D"]
# y = [40,25,60,30]

# # plt.bar(x,y)
# plt.pie(y, labels=x, autopct='%1.1f%%')
# plt.show()

vendas = pd.read_excel(r"C:\Users\davif\Downloads\Dados_vendas.xlsx", sheet_name="Planilha1")
produtos = pd.read_excel(r"C:\Users\davif\Downloads\Dados_vendas.xlsx", sheet_name="Planilha2")

# plt.figure(figsize=(8,4))
# plt.plot(vendas["Mes"], vendas["Vendas"], color='blue', linestyle='-', marker='o')
# plt.title("Evoluções das Vendas", fontsize=14, fontweight='bold')
# plt.xlabel("Mês", fontsize=12)
# plt.ylabel("Vendas", fontsize=12)
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.show()

# plt.plot(vendas["Vendas"], produtos["Quantidade_Vendida"], color='blue', linestyle='-', marker='o')
# plt.xlabel("Vendas", fontsize=12)
# plt.ylabel("Quantidade Vendida", fontsize=12)
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.show()

fig,axs = plt.subplots(nrows=1, ncols=2, figsize=(12,4))
axs[0].plot(vendas["Mes"], vendas["Vendas"], color='blue', linestyle='-', marker='o')
axs[0].set_title("Evolução das Vendas", fontsize=14, fontweight='bold')
axs[0].set_xlabel("Mês", fontsize=12)
axs[0].set_ylabel("Vendas", fontsize=12)
axs[0].grid(True, linestyle='--', alpha=0.5)

axs[1].plot(vendas["Vendas"], produtos["Quantidade_Vendida"], color='green', linestyle='-', marker='o')
axs[1].set_title("Vendas vs Quantidade Vendida", fontsize=14, fontweight='bold')
axs[1].set_xlabel("Vendas", fontsize=12)    
axs[1].set_ylabel("Quantidade Vendida", fontsize=12)
axs[1].grid(True, linestyle='--', alpha=0.5)

plt.show()
