from db import DBHelper
class CarsDB:
    def _init_(self):
        self.db_helper = DBHelper()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS cars(
            brand TEXT PRIMARY KEY,
            year_of_make INTEGER NOT NULL,
            price REAL NOT NULL)
        '''
        self.db_helper.execute_query(query)

    def add_car(self, brand, year_of_make, price):
        query = "INSERT INTO cars(brand, year_of_make, price) VALUES (?, ?, ?)"
        self.db_helper.execute_query(query, (brand, year_of_make, price))

    def list_cars(self):
        query = "SELECT * FROM cars"
        return self.db_helper.fetch_all(query)