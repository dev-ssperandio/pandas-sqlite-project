import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


# Caminho para o banco de dados
db_path = "./data/database.db"

# Conexão com o banco de dados
conn = sqlite3.connect(db_path)

# Lendo a tabela "sales" do banco de dados
query = "SELECT * FROM sales;"
sales_data = pd.read_sql_query(query, conn)

# Fechano conexão
conn.close()

print("Dados lidos do banco de dados: ")
print(sales_data)

# Calculando o total de vendas por produto
sales_data["total_sales"] = sales_data["quantity"] * sales_data["price"]

# Filtrando produtos com vendas totais acima de R$ 1.000,00
filtered_data = sales_data[sales_data["total_sales"] > 1000]

# Exibindo dados manipulados
print("\nDados manipulados: ")
print(filtered_data)

# Caminho para salvar o arquivo CSV
output_path = "./output/processed_data.csv"

# Salvando os dados filtrados em um arquivo CSV
filtered_data.to_csv(output_path, index=False, sep=';')

print(f"\nDados manipulados salvos em: {output_path}")


# Lendo o arquivo CSV gerado
csv_data = pd.read_csv(output_path, sep=";")

# Exibindo as primeiras linhas do arquivo
print("\nDados lidos do CSV: ")
print(csv_data.head())

# Estatísticas descritivas do total de vendas
print("\nEstatística descritiva: ")
print(csv_data["total_sales"].describe())

# Gráfico de barras
csv_data.plot(kind="bar", x="product", y="total_sales", title="Vendas por Produto", legend=False)
plt.ylabel("Total de Vendas (R$)")
plt.tight_layout()
plt.savefig("./output/sales_chart.png") # Salva o gráfico como imagem
plt.show()