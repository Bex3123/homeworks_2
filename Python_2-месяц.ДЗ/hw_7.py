import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        conn.execute(sql)
    except Error as e:
        print(e)


def create_products(conn, product):
    try:
        sql = '''
        INSERT INTO products(product_name, price, quantity)
         VALUES (?, ?, ?)
         '''
        cursor = conn.cursor()
        conn.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def change_quantity(conn,product):
    try:
        sql = '''
        UPDATE products SET quantity = ? WHERE id = ?
        '''
        cursor = conn.cursor()
        conn.execute(sql,product)
        conn.commit()
    except Error as e:
        print(e)


def change_price(conn, product):
    try:
        sql = '''
        UPDATE products SET price = ? WHERE id = ?
        '''
        cursor = conn.cursor()
        conn.execute(sql, product)
        conn.commit()
    except Error as e:
        print(e)


def delete_product(conn, product):
    try:
        sql = '''
        DELETE FROM products WHERE id = ?
        '''
        cursor = conn.cursor()
        conn.execute(sql, product)
        conn.commit()

    except Error as e:
        print(e)


def select_all_products(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM products''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def select_products(conn, product):
    try:
        sql = ('''SELECT * FROM products WHERE price < ? and quantity > ?''')
        cursor = conn.cursor()
        cursor.execute(sql, product)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(e)


def search_product_by_product_name(conn, product_name):
    try:
        sql = ('''SELECT product_name FROM products WHERE  product_name LIKE ?''')
        cursor = conn.cursor()
        cursor.execute(sql, ("%"+product_name+"%",))
        rows = cursor.fetchall()
        name = []
        for row in rows:
            name.append(row)
        print(name)
    except Error as e:
        print(e)


def add_products(conn):
    create_products(connection, ('pen', 100, 20))
    create_products(connection, ('bread', 30, 15))
    create_products(connection, ('cake', 400, 5))
    create_products(connection, ('banana', 50, 25))
    create_products(connection, ('ice cream ', 250, 6))
    create_products(connection, ('milk ', 50, 10))
    create_products(connection, ('pepsi', 125, 5))
    create_products(connection, ('bacon', 500, 5))
    create_products(connection, ('paper', 20.00, 100))
    create_products(connection, ('toilet paper', 65.00, 3))
    create_products(connection, ('pancake ', 400, 5))
    create_products(connection, ('cheese ', 400, 5))
    create_products(connection, ('potato', 400, 5))
    create_products(connection, ('pizza', 400, 5))
    create_products(connection, ('cheeseburger ', 400, 5))
    create_products(connection, ('juice ', 400, 5))


sql_create_product_table = '''
CREATE TABLE if on exists products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name VARCHAR(200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''
db_name = 'hw.db'
connection = create_connection(db_name)
if connection is not None:
    create_table(connection, sql_create_product_table)
    add_products(connection)
    select_all_products(connection)
    print('all products')
    select_products(connection, (100, 5))
    print('products price < 100 quantity > 5')
    search_product_by_product_name(connection, 'cake')
    print('searched product by name')
    change_quantity(connection, (67, 12))
    print('changed quantity by id')
    change_price(connection,(390, 4))
    print('changed price by id')
    delete_product(connection,(8,))
    print('deleted product')
    print('products after changes')
    select_all_products(connection)
    connection.close()
    print('Successfully connected')
