import sqlite3

class DBHelper:
    def __init__(self, db_name="cars.db"):
        self.CONN = sqlite3.connect(db_name)
        self.CURSOR = self.CONN.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.CURSOR.execute(query, params)
        else:
            self.CURSOR.execute(query)
        self.CONN.commit()

    def fetch_all(self, query, params=None):
        if params:
            self.CURSOR.execute(query, params)
        else:
            self.CURSOR.execute(query)
        return self.CURSOR.fetchall()

    def fetch_one(self, query, params=None):
        if params:
            self.CURSOR.execute(query, params)
        else:
            self.CURSOR.execute(query)
        return self.CURSOR.fetchone()

    def __del__(self):
        self.CONN.close()
