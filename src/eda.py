import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregamento dos dados
df = pd.read_csv('amazon_tratado.csv')

# Limpeza e conversão de tipos
df['rating'] = df['rating'].astype(str).str.replace('|', '', regex=False)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['discount_percentage'] = df['discount_percentage'].astype(str).str.replace('%', '', regex=False).astype(float) / 100

# Configuração estética dos gráficos
sns.set_theme(style="whitegrid")

# 1. Gráfico de Histograma (Distribuição de Notas)
plt.figure(figsize=(10, 6))
sns.histplot(df['rating'].dropna(), bins=15, kde=True, color='royalblue')
plt.title('Distribuição das Avaliações dos Produtos (Rating)', fontsize=14)
plt.xlabel('Nota (1-5)', fontsize=12)
plt.ylabel('Frequência de Produtos', fontsize=12)
plt.savefig('histograma_ratings.png', dpi=300)
plt.show()

# 2. Gráfico de Dispersão (Percentual de Desconto vs. Rating)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='discount_percentage', y='rating', alpha=0.5, color='darkorange')
plt.title('Relação entre Percentual de Desconto e Avaliação', fontsize=14)
plt.xlabel('Percentual de Desconto (%)', fontsize=12)
plt.ylabel('Rating', fontsize=12)
plt.axhline(df['rating'].mean(), color='red', linestyle='--', label=f'Média: {df["rating"].mean():.2f}')
plt.legend()
plt.savefig('dispersao_desconto_rating.png', dpi=300)
plt.show()
