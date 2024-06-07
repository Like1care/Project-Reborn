import sqlite3
from sqlite3 import Error as error


connect = sqlite3.connect('request_data.bd')
cursor = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Request_data
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             request_date TEXT,
             request_type TEXT,
             cryptocurrency TEXT,
             request_method TEXT)'''
            )


def update_data(name:str,
                request_date:str,
                request_type:str,
                cryptocurrency:str,
                request_method:str):
    
    try:
        cursor.execute("""INSERT INTO Request_data (name, request_date, request_type, cryptocurrency, request_method)
                       VALUES(?, ?, ?, ?, ? )""", (f'{name}', f'{request_date}', f'{request_type}', f'{cryptocurrency}', f'{request_method}'))
    
    except error:
        return "Error"
          

update_data('Name', 'Current_date', 'Get currency price info', 'Bitcoin', 'get_price_info')

connect.commit()
connect.close()