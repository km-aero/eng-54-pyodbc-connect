from db_connect_oop import *

class NWProducts(MSDBConnection):

    def __init__(self):
        super().__init__()
        self.table = 'Products'

    def __sql_query(self, query): # private to avoid SQL injection
        return self.cursor.execute(query)

    # Write all the CRUD methods

    # Read ONE based on ID(select)
    def read_one(self, column,id_num):
        row = self.__sql_query(f'SELECT * FROM {self.table} WHERE {column} = {id_num}').fetchone()
        return row

    # Read ALL (select)
    def read_all(self):
        #return data with all products
        data = self.__sql_query(f'SELECT * FROM {self.table}').fetchall()
        for row in data:
            print(row)

    # Create one product (insert)
    def create_one(self, name, value):
        data = self.__sql_query(f'INSERT INTO {self.table} ({name}) VALUES (\'{value}\')')
        self.cursor.commit()
        # return self.__sql_query(f'SELECT * FROM {self.table')
        # tip: search commit for pyodbc


    # Delete product (delete)




