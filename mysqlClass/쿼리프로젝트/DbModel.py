import mysql.connector
from mysql.connector import Error
import streamlit as st

class DbModel :
    def dbConnection(self):
        
        connection = mysql.connector.connect(
                    host = 'database-1.c03ybmdf5nxq.ap-northeast-2.rds.amazonaws.com',
                    database = 'my_edu_db',
                    user = 'streamlit',
                    password = 'yh123456789'
        )
        
        try:
            if connection.is_connected:
                print('db연결 success!')
                return connection
                
        except Error as e:
            st.warning('디비 관련 에러 발생', e)