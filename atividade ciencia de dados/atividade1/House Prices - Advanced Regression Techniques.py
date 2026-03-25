import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Etapa 1: Gerar e salvar um CSV com dados simulados
# Se o arquivo real não for encontrado, o código cria um conjunto de dados simulado.
try:
    df = pd.read_csv("train (1).csv")
except FileNotFoundError:
    np.random.seed(42)
    data = {
        'LotArea': np.random.randint(1300, 215245, size=300),
        'OverallQual': np.random.randint(1, 10, size=300),
        'YearBuilt': np.random.randint(1872, 2011, size=300),
        'SalePrice': np.random.randint(34900, 755000, size=300)
    }
    df = pd.DataFrame(data)
    df.to_csv("train (1).csv", index=False)

# Etapa 2: Importação dos dados
df = pd.read_csv("train (1).csv")

# Remover espaços extras nos nomes das colunas, se houver
df.columns = df.columns.str.strip()

# Etapa 3: Seleção de colunas relevantes
selected_columns = ['LotArea', 'YearBuilt', 'OverallQual', 'SalePrice']
df_selected = df[selected_columns].copy()

# Etapa 4: Pré-processamento
print("Valores ausentes por coluna:")
print(df_selected.isnull().sum())

df_selected = df_selected.replace("NA", np.nan)

for col in selected_columns:
    df_selected[col] = pd.to_numeric(df_selected[col], errors='coerce')
    df_selected[col] = df_selected[col].fillna(df_selected[col].mean())

# Etapa 5: Transformação (normalização da coluna 'SalePrice')
df_selected['SalePrice_norm'] = (
    df_selected['SalePrice'] - df_selected['SalePrice'].mean()
) / df_selected['SalePrice'].std()

# Etapa 6: Mineração de dados (modelo de regressão linear)
X = df_selected[['LotArea', 'YearBuilt', 'OverallQual']]
y = df_selected['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Etapa 7: Interpretação dos resultados
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMSE (Erro Quadrático Médio): {mse:.2f}")
print(f"R² (Coeficiente de Determinação): {r2:.2f}")

# Etapa 8: Visualização
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='purple')
plt.xlabel("Valores Reais")
plt.ylabel("Valores Previstos")
plt.title("Previsão de Valores com Regressão Linear")
plt.grid(True)
plt.show()