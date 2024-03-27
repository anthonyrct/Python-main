import pandas as pd
import matplotlib.pyplot as plt

# Dados das vendas
vendas = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},
    
]

# Dados do comportamento do cliente
comportamento_cliente = [
    {"id": 101, "nome": "João da Silva", "idade": 45, "sexo": "Masculino", "cidade": "São Paulo", "valor_gasto_total": 29000.00},
    {"id": 102, "nome": "Maria Oliveira", "idade": 38, "sexo": "Feminino", "cidade": "Rio de Janeiro", "valor_gasto_total": 30800.00},
   
]

# Criando DataFrame para as vendas e comportamento do cliente
df_vendas = pd.DataFrame(vendas)
df_comportamento_cliente = pd.DataFrame(comportamento_cliente)

# Juntando os DataFrames com base no cliente_id
df_merged = pd.merge(df_vendas, df_comportamento_cliente, left_on='cliente_id', right_on='id', how='inner')

# Calculando o valor total gasto por cada cliente
total_gasto_por_cliente = df_merged.groupby('cliente_id')['valor_gasto_total'].sum()

# Plotando o histograma da distribuição dos gastos dos clientes
plt.figure(figsize=(10, 6))
plt.hist(total_gasto_por_cliente, bins=10, color='skyblue', edgecolor='black')
plt.title('Distribuição dos Gastos dos Clientes')
plt.xlabel('Valor Total Gasto')
plt.ylabel('Número de Clientes')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
