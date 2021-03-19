import mysql.connector

def db_connection ():
    connection = mysql.connector.connect(
                host = '',
                database = '',
                user = '',
                password = ''
    )
    return connection


