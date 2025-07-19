import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Carregando os dados
df = pd.read_csv('../data/vendas.csv')
df['Data'] = pd.to_datetime(df['Data'])

# Criando colunas auxiliares
df['Mes'] = df['Data'].dt.to_period('M')

# Faturamento mensal
vendas_mes = df.groupby('Mes')['Total_Venda'].sum()

plt.figure(figsize=(10,5))
vendas_mes.plot(kind='bar', color='skyblue')
plt.title('Faturamento Mensal')
plt.ylabel('Total em R$')
plt.xlabel('Mês')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_produtos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)

sns.barplot(x=top_produtos.values, y=top_produtos.index, palette='viridis')
plt.title('Top 10 Produtos Mais Vendidos')
plt.xlabel('Quantidade')
plt.ylabel('Produto')
plt.show()

# Vendas por Estado
vendas_estado = df.groupby('Estado')['Total_Venda'].sum().reset_index()
fig = px.bar(vendas_estado, x='Estado', y='Total_Venda', title='Vendas por Estado')
fig.show()
