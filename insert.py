import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Marina Ortega\Documents\tblInventor.accdb;')

    user_id = 11
    Inventors = "Group 2: Bahay Ampunan"
    Invention = "Connecting MS Access Database"
    DateOfInvention = '22/05/2022'
    Description = "A python program that connects to MS Access Database and inserts new record."

    data = connection.cursor()
    data.execute('update tblInventor SET Inventors=? WHERE id=?',(Inventors,user_id))
    data.execute("update tblInventor SET Invention=? WHERE id=?", (Invention, user_id))
    data.execute('update tblInventor SET DateOfInvention=? WHERE id=?', (DateOfInvention, user_id))
    data.execute('update tblInventor SET Description=? WHERE id=?', (Description, user_id))

    data.commit()
    print("Data is updated")



except pyodbc.Error:
    print("Error in Connection")