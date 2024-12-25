import sqlite3


db_path = './data/database.db'

def create_data(product, quantity, price, date):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = """INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?);"""

    cursor.execute(query, (product, quantity, price, date))

    conn.commit()
    conn.close()

    print("\nDado criado com sucesso!")

def read_data():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "SELECT * FROM sales;"

    cursor.execute(query)

    date = cursor.fetchall()

    conn.close()

    return date

def update_data(data_id, product=None, quantity=None, price=None, date=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    fields = []
    values = []

    if product:
        fields.append("product = ?")
        values.append(product)
    elif quantity:
        fields.append("quantity = ?")
        values.append(quantity)
    elif price:
        fields.append("price = ?")
        values.append(price)
    elif date:
        fields.append("date = ?")
        values.append(date)
    elif not fields:
        price("Nada para atualizar!")
        return
    
    query = f"UPDATE sales SET {', '.join(fields)} WHERE id = ?;"
    values.append(data_id)
    cursor.execute(query, values)

    conn.commit()
    conn.close()
    print("\nDado atualizado com sucesso!")

def delete_data(data_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "DELETE FROM sales WHERE id = ?;"

    cursor.execute(query, (data_id,))

    conn.commit()
    conn.close()
    print("\nDado deletado com sucesso!")
