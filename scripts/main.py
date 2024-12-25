import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

from database_operations import create_data, read_data, update_data, delete_data

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
