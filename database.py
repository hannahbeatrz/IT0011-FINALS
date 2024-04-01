import sqlite3

def create_table():
    with sqlite3.connect('Products.db') as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Products (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        in_stock INTEGER
                    )""")

def fetch_products():
    with sqlite3.connect('Products.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Products")
        return cur.fetchall()

def insert_product(id, name, in_stock):
    with sqlite3.connect('Products.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO Products (id, name, in_stock) VALUES (?,?,?)", (id, name, in_stock))

def delete_product(id):
    with sqlite3.connect('Products.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM Products WHERE id=?", (id,))

def update_product(new_name, new_stock, id):
    with sqlite3.connect('Products.db') as conn:
        cur = conn.cursor()
        cur.execute("UPDATE Products SET name=?, in_stock=? WHERE id=?", (new_name, new_stock, id))

def id_exists(id):
    with sqlite3.connect('Products.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Products WHERE id=?", (id,))
        for row in cur:
            return True
    return False

create_table()