import pandas as pd
import matplotlib.pyplot as plt

# Definindo os dados
vendas_data = [
    {'id': 1, 'data': '2023-01-05', 'produto': 'Banheira', 'quantidade': 2, 'preco_unitario': 2500.00, 'cliente_id': 101},
    {'id': 2, 'data': '2023-02-12', 'produto': 'Ofurô', 'quantidade': 1, 'preco_unitario': 200.00, 'cliente_id': 113},
    {'id': 3, 'data': '2023-03-20', 'produto': 'Spa', 'quantidade': 3, 'preco_unitario': 5000.00, 'cliente_id': 103},
    {'id': 4, 'data': '2023-04-10', 'produto': 'Banheira', 'quantidade': 1, 'preco_unitario': 2500.00, 'cliente_id': 104},
    {'id': 5, 'data': '2023-05-15', 'produto': 'Ofurô', 'quantidade': 2, 'preco_unitario': 250.00, 'cliente_id': 105},
    {'id': 6, 'data': '2023-06-25', 'produto': 'Spa', 'quantidade':2 , 'preco_unitario':5000.00 , 'cliente_id': 106},
    {'id': 7, 'data': '2023-07-05', 'produto': 'Banheira', 'quantidade': 1, 'preco_unitario': 2500.00, 'cliente_id': 113},
    {'id': 8, 'data': '2023-08-18', 'produto': 'Ofurô', 'quantidade': 3, 'preco_unitario': 500.00, 'cliente_id': 108},
    {'id': 9, 'data': '2023-09-30', 'produto': 'Spa', 'quantidade': 1, 'preco_unitario': 5000.00, 'cliente_id': 109},
    {'id': 10, 'data': '2023-10-08', 'produto': 'Banheira', 'quantidade': 2, 'preco_unitario': 2500.00, 'cliente_id': 110},
    {'id': 11, 'data': '2023-11-12', 'produto': 'Ofurô', 'quantidade': 1, 'preco_unitario': 1000.00, 'cliente_id': 111},
    {'id': 12, 'data': '2023-12-20', 'produto': 'Spa', 'quantidade': 3, 'preco_unitario': 5000.00, 'cliente_id': 112},
]

comportamento_cliente_data = [
    {'id': 101, 'nome': 'João da Silva', 'idade': 45, 'sexo': 'Masculino', 'cidade': 'São Paulo', 'valor_gasto_total': 29.000},
    {'id': 102, 'nome': 'Maria Oliveira', 'idade': 38, 'sexo': 'Feminino', 'cidade': 'Rio de Janeiro', 'valor_gasto_total': 30.800},
    {'id': 103, 'nome': 'Carlos Souza', 'idade': 50, 'sexo': 'Masculino', 'cidade': 'Belo Horizonte', 'valor_gasto_total': 30000.00},
    {'id': 104, 'nome': 'Ana Santos', 'idade': 55, 'sexo': 'Feminino', 'cidade': 'Porto alegre', 'valor_gasto_total': 7.500},
    {'id': 105, 'nome': 'Pedro Costa', 'idade': 42, 'sexo': 'Masculino', 'cidade': 'Brasilia', 'valor_gasto_total': 19.300},
    {'id': 106, 'nome': 'Sofia Pereira', 'idade': 42, 'sexo': 'Feminino', 'cidade': 'Recife', 'valor_gasto_total': 15.000},
    {'id': 107, 'nome': 'josé Santos', 'idade': 60, 'sexo': 'Masculino', 'cidade': 'Salvador', 'valor_gasto_total': 2.500},
    {'id': 108, 'nome': 'Paula Lima', 'idade': 36, 'sexo': 'Feminino', 'cidade': 'Fortaleza', 'valor_gasto_total': 38.950},
    {'id': 109, 'nome': 'Luiz Oliveira', 'idade': 47, 'sexo': 'Masculino', 'cidade': 'Manaus', 'valor_gasto_total': 25.000},
    {'id': 110, 'nome': 'Cristina Santos', 'idade': 52, 'sexo': 'Feminino', 'cidade': 'Curitiba', 'valor_gasto_total': 5.000},
    {'id': 111, 'nome': 'Antonio Costa', 'idade': 40, 'sexo': 'Masculino', 'cidade': 'Natal', 'valor_gasto_total': 8.300},
    {'id': 112, 'nome': 'Beatriz Silva', 'idade': 43, 'sexo': 'Feminino', 'cidade': 'Florianopolis', 'valor_gasto_total': 30.000},
]

desempenho_produto_data = [
    {'produto': 'Banheira', 'vendas_totais': 26, 'receita_total': 50000.00},
    {'produto': 'Ofurô', 'vendas_totais': 60, 'receita_total': 37200.00},
    {'produto': 'Spa', 'vendas_totais': 21, 'receita_total': 105000.00},
]

# Convertendo os dados em DataFrames
vendas_df = pd.DataFrame(vendas_data)
comportamento_cliente_df = pd.DataFrame(comportamento_cliente_data)
desempenho_produto_df = pd.DataFrame(desempenho_produto_data)

# Cores para as barras
cores = ['blue', 'orange', 'green']

# Plotagem do gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(desempenho_produto_df['produto'], desempenho_produto_df['vendas_totais'], color=cores)
plt.title('Vendas Totais por Produto')
plt.xlabel('Produto')
plt.ylabel('Vendas Totais')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
