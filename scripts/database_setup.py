import sqlite3
from random import random
from pathlib import Path

# Caminho do banco de dados
DB_PATH = Path("./data/sales.db")

# Conexão com o banco de dados
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Cria tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    date TEXT NOT NULL
);
""")

data = [
    ("Notebook", 10, 2500.00, "2024-01-15"),
    ("Mouse", 0, 30.00, "2024-02-20"),
    ("Teclado", 20, 150.00, "2024-03-05"),
    ("Monitor", 5, 1200.00, "2024-04-12"),
    ("Headset", 0, 300.00, "2024-05-30"),
    ("Notebook", 10, 2500.00, "2024-01-15"),
    ("Mouse", 50, 30.00, "2024-02-20"),
    ("Teclado", 20, 150.00, "2024-03-05"),
    ("Monitor", 0, 1200.00, "2024-04-12"),
    ("Headset", 15, 300.00, "2024-05-30"),
    ("Notebook", 10, 2500.00, "2024-01-15"),
    ("Mouse", 50, 30.00, "2024-02-20"),
    ("Teclado", 0, 150.00, "2024-03-05"),
    ("Monitor", 5, 1200.00, "2024-04-12"),
    ("Headset", 0, 300.00, "2024-05-30")
]

cursor.executemany("INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?);", data)

conn.commit()
conn.close()

print("Banco de dados configurado com sucesso!")
