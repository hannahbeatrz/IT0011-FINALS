import sqlite3

def create_table():
    conn = sqlite3.connect('Products.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Products (id TEXT PRIMARY KEY, name TEXT, in_stock INTEGER)")
    conn.commit()
    conn.close()
    
def fetch_products():
    conn = sqlite3.connect('Products.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Products")
    Products = cur.fetchall()
    conn.close()
    return Products

def insert_product(id, name, in_stock):
    conn = sqlite3.connect('Products.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Products (id, name, in_stock) VALUES (?,?,?)",(id,name,in_stock))
    conn.commit()
    conn.close()
    
def delete_product(id):
    conn = sqlite3.connect('Products.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Products WHERE id=?",(id,))
    conn.commit()
    conn.close()
    
def update_product(new_name, new_stock, id):
    conn = sqlite3.connect('Products.db')
    cur = conn.cursor()
    cur.execute("UPDATE Products SET name=?, in_stock=? WHERE id=?",(new_name, new_stock, id))
    conn.commit()
    conn.close()
    
def id_exists(id):
    conn = sqlite3.connect('Products.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Products WHERE id=?",(id,))
    if cur.fetchone():
        conn.close()
        return True
    conn.close()
    return False

create_table()