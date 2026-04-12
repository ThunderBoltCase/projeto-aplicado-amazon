import pandas as pd
import numpy as np

# 1. Carregamento do arquivo original
df = pd.read_csv('amazon.csv')

# 2. Tratamento da coluna 'rating' (Remoção da anomalia '|' e conversão)
# Substitui o caractere problemático e força a conversão para numérico (erros viram NaN)
df['rating'] = df['rating'].astype(str).str.replace('|', '', regex=False)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Preenchimento dos valores nulos resultantes com a mediana
df['rating'] = df['rating'].fillna(df['rating'].median())

# 3. Tratamento da coluna 'rating_count' (Remoção de vírgulas e valores omissos)
# Remove a pontuação de milhar antes de converter para número
df['rating_count'] = df['rating_count'].astype(str).str.replace(',', '', regex=False)
df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce')

# Substituição dos 2 valores nulos identificados na auditoria pela mediana
df['rating_count'] = df['rating_count'].fillna(df['rating_count'].median())

# 4. Tratamento das colunas financeiras (Preços)
# Remove o símbolo da moeda Indiana (₹) e as vírgulas
colunas_preco = ['actual_price', 'discounted_price']
for col in colunas_preco:
    df[col] = df[col].astype(str).str.replace('₹', '', regex=False).str.replace(',', '', regex=False)
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Tratamento da coluna de percentual de desconto
# Remove o símbolo de porcentagem e converte para formato decimal
df['discount_percentage'] = df['discount_percentage'].astype(str).str.replace('%', '', regex=False)
df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce') / 100

# 6. Exportação do arquivo limpo
# Cria uma nova planilha sem os erros
df.to_csv('amazon_tratado.csv', index=False)

print("Tratamento concluído!")
