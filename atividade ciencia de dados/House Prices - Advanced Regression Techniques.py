import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Etapa 1: Importação dos dados (usar arquivo real)
df = pd.read_csv("train (1).csv")

# Etapa 2: Seleção de colunas relevantes
selected_columns = ['LotArea', 'OverallQual', 'YearBuilt', 'SalePrice']
df_selected = df[selected_columns].copy()

# Etapa 3: Pré-processamento
print("Valores ausentes por coluna:")
print(df_selected.isnull().sum())

# (Opcional - normalmente não necessário)
df_selected['LotArea'] = df_selected['LotArea'].fillna(df_selected['LotArea'].mean())

# Etapa 4: Definição de X e y
X = df_selected[['LotArea', 'OverallQual', 'YearBuilt']]
y = df_selected['SalePrice']

# Etapa 5: Divisão treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Etapa 6: Treinamento do modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Etapa 7: Previsões
y_pred = model.predict(X_test)

# Etapa 8: Avaliação
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMSE (Erro Quadrático Médio): {mse:.2f}")
print(f"R² (Coeficiente de Determinação): {r2:.4f}")

# Etapa 9: Visualização
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='purple')
plt.xlabel("Valores Reais")
plt.ylabel("Valores Previstos")
plt.title("Previsão de preços")
plt.grid(True)
plt.show()