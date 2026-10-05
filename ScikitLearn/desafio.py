from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



dados = pd.read_excel(r"C:\Users\davif\Documents\Obsidian Vault\FUCAPE\2026-2\Linguagens de Programação\Biblioteca\94557f36-bfa8-42dd-b367-c6620ca47b56.xlsx")
x1 = dados['Pclass'].values
x2 = dados['Sex'].values
x3 = dados['Age'].values
x4 = dados['Relatives'].values
x5 = dados['Fare'].values
y = dados['Survived'].values

X = np.column_stack((x1, x2,x3,x4,x5))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("R2 score: %.2f" % r2_score(y_test, y_pred))

plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--')
plt.title("Avaliação do Modelo")
plt.show()

predicao = modelo.predict([[1,1,22,1,7.25]])
print(predicao)