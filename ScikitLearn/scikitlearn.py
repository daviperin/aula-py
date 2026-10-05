from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# gastos = np.array([2.0, 2.4, 1.5, 3.5, 3.5,3.5,3.5,3.7,3.7])
# vendas = np.array([196,221,136,255,244,230,232,255,267])

# modelo = LinearRegression()
# modelo.fit(gastos.reshape(-1, 1), vendas)

# previsao = modelo.predict([[4.0]])
# print(previsao)

# dados = pd.read_excel(r"C:\Users\davif\Documents\Obsidian Vault\FUCAPE\2026-2\Linguagens de Programação\Biblioteca\data.xlsx")

# x1 = dados['Feature1'].values
# x2 = dados['Feature2'].values
# y = dados['Target'].values

# X = np.column_stack((x1, x2))

# regressor = LinearRegression()
# regressor.fit(X, y)

# previsao = regressor.predict([[2.4,0.6]])
# print(previsao)

dados = datasets.load_diabetes()
#dividir train e test
X_train, X_test, y_train, y_test = train_test_split(dados.data, dados.target, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("R2 score: %.2f" % r2_score(y_test, y_pred))

plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.xlabel("Valores Reais")
plt.ylabel("Valores Preditos")
plt.title("Avaliação do Modelo")
plt.show()