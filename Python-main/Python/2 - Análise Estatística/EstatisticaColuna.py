import pandas as pd
import matplotlib.pyplot as plt

# Definindo os dados
vendas_data = [
    {'id': 1, 'data': '2023-01-05', 'produto': 'Banheira', 'quantidade': 2, 'preco_unitario': 2500.00, 'cliente_id': 101},
    {'id': 2, 'data': '2023-02-12', 'produto': 'Ofurô', 'quantidade': 1, 'preco_unitario': 200.00, 'cliente_id': 113},
    {'id': 3, 'data': '2023-03-20', 'produto': 'Spa', 'quantidade': 3, 'preco_unitario': 5000.00, 'cliente_id': 103},
    {'id': 4, 'data': '2023-04-10', 'produto': 'Banheira', 'quantidade': 1, 'preco_unitario': 2500.00, 'cliente_id': 104},
    {'id': 5, 'data': '2023-05-15', 'produto': 'Ofurô', 'quantidade': 2, 'preco_unitario': 250.00, 'cliente_id': 105},
    {'id': 6, 'data': '2023-06-25', 'produto': 'Spa', 'quantidade': 2, 'preco_unitario': 5000.00, 'cliente_id': 106},
    {'id': 7, 'data': '2023-07-05', 'produto': 'Banheira', 'quantidade': 1, 'preco_unitario': 2500.00, 'cliente_id': 113},
    {'id': 8, 'data': '2023-08-18', 'produto': 'Ofurô', 'quantidade': 3, 'preco_unitario': 500.00, 'cliente_id': 108},
    {'id': 9, 'data': '2023-09-30', 'produto': 'Spa', 'quantidade': 1, 'preco_unitario': 5000.00, 'cliente_id': 109},
    {'id': 10, 'data': '2023-10-08', 'produto': 'Banheira', 'quantidade': 2, 'preco_unitario': 2500.00, 'cliente_id': 110},
    {'id': 11, 'data': '2023-11-12', 'produto': 'Ofurô', 'quantidade': 1, 'preco_unitario': 1000.00, 'cliente_id': 111},
    {'id': 12, 'data': '2023-12-20', 'produto': 'Spa', 'quantidade': 3, 'preco_unitario': 5000.00, 'cliente_id': 112},
]

# Convertendo os dados em DataFrames
vendas_df = pd.DataFrame(vendas_data)

# Estatísticas descritivas
estatisticas_descritivas = vendas_df.describe()

# Cores para as barras
cores = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']

# Plotagem do gráfico de barras(cores)
estatisticas_descritivas.drop('id', axis=1).plot(kind='bar', color=cores, legend=True, figsize=(10, 6))
plt.title('Estatísticas Descritivas (Quantidade, Preço Unitário)')
plt.xlabel('Estatísticas')
plt.ylabel('Valores')
plt.grid(axis='y')  # Adicionando grades apenas ao eixo y
plt.tight_layout()  # Ajustando o layout para evitar sobreposição
plt.show()  # Mostrar o gráfico
