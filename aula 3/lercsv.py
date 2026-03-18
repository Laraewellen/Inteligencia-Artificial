import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Etapa 1: Gerar e salvar um CSV com dados simulados
np.random.seed(42)
data = {
    'idade': np.random.randint(18, 65, size=300),
    'experiencia': np.random.randint(0, 40, size=300),
    'salario': np.random.normal(5000, 1500, size=300).round(2),
    'vendas': np.random.normal(200, 50, size=300).round(2)
}
df = pd.DataFrame(data)
df.to_csv("dados_vendas.csv", index=False)

# Etapa 2: Importação dos dados
df = pd.read_csv("dados_vendas.csv")

# Etapa 3: Seleção de colunas relevantes
selected_columns = ['idade', 'experiencia', 'salario', 'vendas']
df_selected = df[selected_columns]
# Etapa 4: Pré-processamento
print("Valores ausentes por coluna:")
print(df_selected.isnull().sum())
# Etapa 5: Transformação (normalização da coluna 'salario')
df_selected['salario_norm'] = (df_selected['salario'] - df_selected['salario'].mean()) / df_selected['salario'].std()

# Etapa 6: Mineração de dados (modelo de regressão linear)
X = df_selected[['idade', 'experiencia', 'salario']]
y = df_selected['vendas']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
plt.scatter(y_test, y_pred, alpha=0.7, color='blue')
plt.xlabel("Vendas Reais")
plt.ylabel("Vendas Previstas")
plt.title("Previsão de Vendas com Regressão Linear")
plt.grid(True)
plt.show()
