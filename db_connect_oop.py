import pyodbc

class MSDBConnection:
    def __init__(self, database = 'Northwind', username = 'SA', password = 'Passw0rd2018'):
        self.database = database
        self.username = username
        self.password = password
        # Connecting to server
        self.conn = pyodbc.connect('DSN=MYMSSQL;DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        # Cursors are objects that run code
        self.cursor = self.conn.cursor()

    def sql_query(self, query):
        return self.cursor.execute(query)



# nw_db_objct = MSDBConnection()
# x = nw_db_objct.sql_query('SELECT * FROM Products')
#
# print(x.fetchone())