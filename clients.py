

from db import DBHelper

class ClientsDB:
    def __init__(self):
        self.db_helper = DBHelper()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT NOT NULL)
        '''
        self.db_helper.execute_query(query)

    def add_client(self, name, phone_number, email):
        query = "INSERT INTO clients(name, phone_number, email) VALUES (?, ?, ?)"
        self.db_helper.execute_query(query, (name, phone_number, email))

    def search_client_by_name(self, name):
        query = "SELECT * FROM clients WHERE name=?"
        return self.db_helper.fetch_all(query, (name,))

    def search_client_by_id(self, client_id):
        query = "SELECT * FROM clients WHERE id=?"
        return self.db_helper.fetch_one(query, (client_id,))

    def list_clients(self):
        query = "SELECT * FROM clients"
        return self.db_helper.fetch_all(query)

    def delete_client(self, client_id):
        query = "DELETE FROM clients WHERE id=?"
        self.db_helper.execute_query(query, (client_id,))
        query = "DELETE FROM orders WHERE client_id=?"
        self.db_helper.execute_query(query, (client_id,))
