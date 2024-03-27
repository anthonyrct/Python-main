import pandas as pd
import matplotlib.pyplot as plt

# Definindo os dados dos clientes
clientes = [
    {"id": 101, "nome": "João da Silva", "idade": 45, "sexo": "Masculino", "cidade": "São Paulo", "valor_gasto_total": 29000.00},
    {"id": 102, "nome": "Maria Oliveira", "idade": 38, "sexo": "Feminino", "cidade": "Rio de Janeiro", "valor_gasto_total": 30800.00},
    {"id": 103, "nome": "Carlos Souza", "idade": 50, "sexo": "Masculino", "cidade": "Belo Horizonte", "valor_gasto_total": 30000.00},
    {"id": 104, "nome": "Ana Santos", "idade": 55, "sexo": "Feminino", "cidade": "Porto Alegre", "valor_gasto_total": 7500.00},
    {"id": 105, "nome": "Pedro Costa", "idade": 42, "sexo": "Masculino", "cidade": "Brasília", "valor_gasto_total": 19300.00},
    {"id": 106, "nome": "Sofia Pereira", "idade": 48, "sexo": "Feminino", "cidade": "Recife", "valor_gasto_total": 15000.00},
    {"id": 107, "nome": "José Santos", "idade": 60, "sexo": "Masculino", "cidade": "Salvador", "valor_gasto_total": 2500.00},
    {"id": 108, "nome": "Paula Lima", "idade": 36, "sexo": "Feminino", "cidade": "Fortaleza", "valor_gasto_total": 38950.00},
    {"id": 109, "nome": "Luiz Oliveira", "idade": 47, "sexo": "Masculino", "cidade": "Manaus", "valor_gasto_total": 25000.00},
    {"id": 110, "nome": "Cristina Santos", "idade": 52, "sexo": "Feminino", "cidade": "Curitiba", "valor_gasto_total": 5000.00},
    {"id": 111, "nome": "Antonio Costa", "idade": 40, "sexo": "Masculino", "cidade": "Natal", "valor_gasto_total": 8300.00},
    {"id": 112, "nome": "Beatriz Silva", "idade": 43, "sexo": "Feminino", "cidade": "Florianópolis", "valor_gasto_total": 30000.00},
    {"id": 113, "nome": "Loja Propria", "sexo": "", "cidade": "Limeira", "valor_gasto_total": 39500.00},
]

# Definindo os dados das vendas
vendas = [
    {"id": 1, "data": '2023-01-05', "produto": "Banheira", "quantidade": 2, "preco_unitario": 2500.00, "cliente_id": 101},
    {"id": 2, "data": '2023-02-12', "produto": "Ofurô", "quantidade": 1, "preco_unitario": 200.00, "cliente_id": 113},
    
]

# Criando DataFrames
df_clientes = pd.DataFrame(clientes)
df_vendas = pd.DataFrame(vendas)

# Calculando o valor total gasto por cliente
valor_gasto_por_cliente = df_vendas.groupby('cliente_id')['preco_unitario'].sum()

# Calculando a frequência de compras por cliente
frequencia_de_compras_por_cliente = df_vendas['cliente_id'].value_counts()

# Juntando os dados em um único DataFrame
df_fidelidade_clientes = pd.DataFrame({
    'valor_gasto_total': valor_gasto_por_cliente,
    'frequencia_de_compras': frequencia_de_compras_por_cliente
}).reset_index()

# Renomeando a coluna 'index' para 'cliente_id'
df_fidelidade_clientes.rename(columns={'index': 'cliente_id'}, inplace=True)

# Mesclando com os dados dos clientes para obter os nomes
df_fidelidade_clientes = df_fidelidade_clientes.merge(df_clientes[['id', 'nome']], left_on='cliente_id', right_on='id')

# Plotando o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df_fidelidade_clientes['frequencia_de_compras'], df_fidelidade_clientes['valor_gasto_total'], color='skyblue')
plt.title('Valor Total Gasto vs. Frequência de Compras por Cliente')
plt.xlabel('Frequência de Compras')
plt.ylabel('Valor Total Gasto (R$)')
plt.grid(True, linestyle='--', alpha=0.7)
for i in range(len(df_fidelidade_clientes)):
    plt.text(df_fidelidade_clientes['frequencia_de_compras'][i] + 0.1, df_fidelidade_clientes['valor_gasto_total'][i], df_fidelidade_clientes['nome'][i], fontsize=9)
plt.tight_layout()
plt.show()
