from db import DBHelper

class OrdersDB:
    def __init__(self):
        self.db_helper = DBHelper()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS orders(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_date DATE NOT NULL,
            client_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            total_price REAL NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients(id))
        '''
        self.db_helper.execute_query(query)

    def add_order(self, client_id, order_date, quantity, total_price):
        query = "INSERT INTO orders(client_id, order_date, quantity, total_price) VALUES (?, ?, ?, ?)"
        self.db_helper.execute_query(query, (client_id, order_date, quantity, total_price))

    def list_orders(self):
        query = '''
            SELECT orders.order_id, orders.order_date, clients.name, orders.quantity, orders.total_price
            FROM orders
            JOIN clients ON orders.client_id = clients.id
        '''
        return self.db_helper.fetch_all(query)
