import mysql.connector
from mysql.connector import Error
from dbc import db_connection
import streamlit as st

class DbModel :
    def dbConnection():
        connection = mysql.connector.connect(
                    host = 'com',
                    database = 'db',
                    user = 'it',
                    password = ''
        )
        st.warning('dddd')
        try :
            if connection.is_connected:
                print('inside')
                return connection

        except Error as e:
            print('디비 관련 에러 발생', e)

