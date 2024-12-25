import pandas as pd
import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt

from database_operations import create_data, read_data, update_data, delete_data, fetch_data_as_dataframe


DB_PATH = Path("./data/sales.db")

# Conexão com o banco de dados
conn = sqlite3.connect(DB_PATH)

# Testando a função CREATE
create_data("Produto X", 10, 100.0, "2024-12-25")

# Testando a função READ
def show_data():
    print("\nDados atuais: ")
    datas = read_data()
    for data in datas:
        print(data)

show_data()

# Testando a função UPDATE
update_data(4, product="Produto Y", price=25.0)

show_data()

# Testando a função DELETE
delete_data(5)

show_data()


# Trabalhando com Pandas
query = "SELECT * FROM sales;"
df = pd.read_sql_query(query, conn)

conn.close()

print("\nDados lidos do banco de dados: ")
print(df)

df = fetch_data_as_dataframe()

if df is not None:
    print("\nDados garregados com sucesso! ")
    print(df)
    print(df.info())
    print(df.head())

    # Manipulando e analisando
    # Adiciona coluna de total de vendas
    df["total_sales"] = df["quantity"] * df["price"]
    print("\nDados com a colula 'total_sales' adicionada.")
    print(df.head())

    # Produto com maior total de vendas
    top_product = df.groupby("product")["total_sales"].sum().idxmax()
    print(f"\nO produto com o maior total de vendas é: {top_product}")

    # Total de vendas por ano
    df["year"] = df["date"].dt.year
    sales_by_year = df.groupby("year")["total_sales"].sum()
    print("\nTotal de vendas por ano: ")
    print(sales_by_year)

    # Produto com estoque zerado
    out_of_stock = df[df["quantity"] == 0]
    print("\nProduto com estoque zerado: ")
    print(out_of_stock)

    # Exportar resultados para CSV
    df.to_csv("./output/updated_sales_data.csv", index=False, sep=';')
    out_of_stock.to_csv("./output/out_of_stock_products.csv", index=False, sep=';')
    print("\nDados exportados para a pasta 'output'.")

    # Filtrando produtos com vendas totais acime de R$ 1.000,00
    filtered_data = df[df["total_sales"] > 1000]
    print("\nDados manipulados: ")
    print(filtered_data)

    # Lendo arquivo CSV
    df_csv_data = pd.read_csv("./output/updated_sales_data.csv", sep=';')
    print("\nDados lidos no CSV: ")
    print(df_csv_data.head())

    # Estatística descritiva do total de vendas
    print("\Estatística descritiva: ")
    print(df_csv_data["total_sales"].describe())

    # Gráfico de barras
    df_csv_data.plot(kind="bar", x="product", y="total_sales", title="Vendas por produto", legend=False)
    plt.ylabel("Total de vendas (R$) ")
    plt.tight_layout
    plt.savefig("./output/sales_chart.png") #salva o gráfico como imagem
    plt.show()

else:
    print("Não foi possível carregar os dados.")
