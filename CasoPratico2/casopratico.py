from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



dados = pd.read_excel(r"C:\Users\davif\Documents\Obsidian Vault\FUCAPE\2026-2\Linguagens de Programação\Biblioteca\cc079fef-6c3f-4620-878d-c9a41e69a9f9.xlsx")

df = pd.DataFrame(dados)
print(f"Quantidade de linhas: {df.shape[0]}, Quantidade de colunas: {df.shape[1]}")
print(f"Primeiras observações:\n{df.head()}")
print(f"Tipos de dados das variaveis:\n{df.dtypes}")
print(f"Existencia de valores ausentes:\n{df.isnull().sum()}")
print(f"Estatísticas descritivas das variaveis:\n{df.describe().round(2)}")

print()

jogo_mais_vendido = df[df['Global_Sales'] == df['Global_Sales'].max()]
print(f"O jogo mais vendido é {jogo_mais_vendido['Name'].values[0]} com {jogo_mais_vendido['Global_Sales'].values[0]} milhões de unidades faturados.")

print()


jogo_mais_vendido_america = df[df['NA_Sales'] == df['NA_Sales'].max()]
print(f"O jogo mais vendido na América do Norte é {jogo_mais_vendido_america['Name'].values[0]} com {jogo_mais_vendido_america['NA_Sales'].values[0]} milhões de unidades faturados somente na América do Norte.")

print()

jogo_mais_vendido_europa = df[df['EU_Sales'] == df['EU_Sales'].max()]
print(f"O jogo mais vendido na Europa é {jogo_mais_vendido_europa['Name'].values[0]} com {jogo_mais_vendido_europa['EU_Sales'].values[0]} milhões de unidades faturados somente na Europa.")

print()

jogo_mais_vendido_japao = df[df['JP_Sales'] == df['JP_Sales'].max()]
print(f"O jogo mais vendido no Japão é {jogo_mais_vendido_japao['Name'].values[0]} com {jogo_mais_vendido_japao['JP_Sales'].values[0]} milhões de unidades faturados somente no Japão.")

print()

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 8))

#Grafico de dispersao entre nota dos criticos e vendas globais
axs[0].scatter(df['Critic_Score'], df['Global_Sales'])
axs[0].set_title("Dispersão entre nota dos críticos e vendas globais")
axs[0].set_xlabel("Nota dos críticos")
axs[0].set_ylabel("Vendas globais (milhões de unidades)")

#Grafico de dispersao entre nota dos usuarios e vendas globais
axs[1].scatter(df['User_Score'], df['Global_Sales'])
axs[1].set_title("Dispersão entre nota dos usuários e vendas globais")
axs[1].set_xlabel("Nota dos usuários")
axs[1].set_ylabel("Vendas globais (milhões de unidades)")
plt.show()

#Modelo de vendas globais
#Construa um modelo de regressão linear utilizando:
#Variável dependente (Y):
#Global_Sales
#Variáveis explicativas (X):
#Critic_Score
#User_Score

# Remove jogos sem nota (preencher com 0 distorceria o modelo)
base = df.dropna(subset=['Critic_Score', 'User_Score'])
X = base[['Critic_Score', 'User_Score']].values
y = base['Global_Sales'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_global = LinearRegression()
modelo_global.fit(X_train, y_train)

y_pred = modelo_global.predict(X_test)

print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("R2 score: %.2f" % r2_score(y_test, y_pred))


#grafico comparando vendas reais com vendas previstas
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.title("Avaliação do Modelo")
plt.xlabel("Vendas reais (milhões de unidades)")
plt.ylabel("Vendas previstas (milhões de unidades)")
plt.show()

# agora repita a mesma análise, mas utilizando como variável dependente (Y) a variável NA_Sales.
y = base['NA_Sales'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_na = LinearRegression()
modelo_na.fit(X_train, y_train)

y_pred = modelo_na.predict(X_test)

print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("R2 score: %.2f" % r2_score(y_test, y_pred))


#grafico comparando vendas reais com vendas previstas
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.title("Avaliação do Modelo")
plt.xlabel("Vendas reais (milhões de unidades)")
plt.ylabel("Vendas previstas (milhões de unidades)")
plt.show()

# agora repita a mesma análise, mas utilizando como variável dependente (Y) a variável EU_Sales.
y = base['EU_Sales'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_eu = LinearRegression()
modelo_eu.fit(X_train, y_train)

y_pred = modelo_eu.predict(X_test)

print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("R2 score: %.2f" % r2_score(y_test, y_pred))

#grafico comparando vendas reais com vendas previstas
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.title("Avaliação do Modelo")
plt.xlabel("Vendas reais (milhões de unidades)")
plt.ylabel("Vendas previstas (milhões de unidades)")
plt.show()

# agora repita a mesma análise, mas utilizando como variável dependente (Y) a variável JP_Sales.
y = base['JP_Sales'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo_jp = LinearRegression()
modelo_jp.fit(X_train, y_train)

y_pred = modelo_jp.predict(X_test)

print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("R2 score: %.2f" % r2_score(y_test, y_pred))

#grafico comparando vendas reais com vendas previstas
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.title("Avaliação do Modelo")
plt.xlabel("Vendas reais (milhões de unidades)")
plt.ylabel("Vendas previstas (milhões de unidades)")
plt.show()

# Prevendo a previsão de vendas globais para jogos
# Critico - 90 | User Score - 8.5
predicao = modelo_global.predict([[90, 8.5]])
print(f"A previsão de vendas globais para um jogo com nota dos críticos igual a 90 e nota dos usuários igual a 8.5 é de {predicao[0]:.2f} milhões de unidades.")

# Critico - 75 | User Score - 7.0
predicao = modelo_global.predict([[75, 7.0]])
print(f"A previsão de vendas globais para um jogo com nota dos críticos igual a 75 e nota dos usuários igual a 7.0 é de {predicao[0]:.2f} milhões de unidades.")

#Critico - 55 | User Score - 5.5
predicao = modelo_global.predict([[55, 5.5]])
print(f"A previsão de vendas globais para um jogo com nota dos críticos igual a 55 e nota dos usuários igual a 5.5 é de {predicao[0]:.2f} milhões de unidades.")
