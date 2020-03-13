import pyodbc
from dp_products_oop import *

# db_object = NWProducts().read_all()
# db_object

# x = 'Dragon'
# db_object = NWProducts().create_one('ProductName', x)
other_object = NWProducts().read_one('ProductID' ,80)
print(other_object)