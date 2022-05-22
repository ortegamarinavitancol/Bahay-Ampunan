import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Marina Ortega\Documents\tblInventor.accdb;')
    print("Database is Connected")

except pyodbc.Error:
    print("Error in Connection")


