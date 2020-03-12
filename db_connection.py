import pyodbc

# Server variables
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# Connecting to server
conn = pyodbc.connect('DSN=MYMSSQL;DATABASE='+database+';UID='+username+';PWD='+password)

# Cursors are objects that run code
cursor = conn.cursor()
cursor.execute("select * from Customers")
row = cursor.fetchall()

# Prints output of cursor
print(row)

# fetches one entry/row
row = cursor.fetchone()
print(row)

# if you call fetchone again it calls the second entry
row = cursor.fetchone()
print(row)

# Prints all column names and constraints of the instance
print (cursor.description)

# Close object instance
cursor.close()

# Close connection to server
conn.close()

# Best practice: use while loop with fetchone()
rows = crsr.execute('SELECT * FROM Customers')
while True:
    record = rows.fetchone()
    if record is None:
        break
    print(record.ContactName)