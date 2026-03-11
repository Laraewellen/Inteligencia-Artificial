import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar o CSV
df = pd.read_csv("evolucao_ia.csv")

# 2. Mostrar tabela
print("Linha do tempo da IA:")
print(df)

# 3. Criar gráfico de evolução
plt.figure(figsize=(10,5))
plt.plot(df["Ano"], range(len(df)), marker='o')
plt.yticks(range(len(df)), df["Marco_da_IA"])
plt.title("Evolução da Inteligência Artificial")
plt.xlabel("Ano")
plt.ylabel("Marcos Históricos")
plt.grid(True)
plt.tight_layout()
plt.show()
