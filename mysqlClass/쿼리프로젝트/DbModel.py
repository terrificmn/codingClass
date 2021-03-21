import mysql.connector
from mysql.connector import Error
import streamlit as st

class DbModel :
    def dbConnection(self):
        
        connection = mysql.connector.connect(
                    host = '',
                    database = '',
                    user = '',
                    password = ''
        )
        
        try:
            if connection.is_connected:
                print('db연결 success!')
                return connection
                
        except Error as e:
            st.warning('디비 관련 에러 발생', e)