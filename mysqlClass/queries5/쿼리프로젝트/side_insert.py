from mysql.connector import connect
from SqlController import SqlController
from mysql.connector.connection import MySQLConnection
import streamlit as st
from dbc import db_connection
from mysql.connector import Error
import datetime

def insert_query() :
    st.write('hello')

    # Duty = SqlController()
    # Duty.sql_insert()
    title = st.text_input('책 이름을 입력하세요')
    lname = st.text_input('작가 성을 입력하세요')
    fname = st.text_input('작가 이름을 입력하세요')
    released_year =st.date_input('출간년도를 입력하세요')
    stocks = st.number_input('재고는?', min_value=0)
    pages = st.number_input('페이지 수는 몇장?', min_value=0)

    connection = db_connection()
    if st.button('저장하세요'):
        try :
            if connection.is_connected :
                cursor = connection.cursor(dictionary=True) 
                query = """ INSERT INTO books 
                            (title, author_fname, author_lname, released_year, stock_quantity, pages)
                            VALUES ('%s', '%s', '%s', %s, %s, %s); """
                
                data = (title, lname, fname, released_year, stocks, stocks) 
                cursor.execute(query, data)
                connection.commit()
        except Error as e:
                print('디비 관련 에러 발생', e)

        finally:
                cursor.close()
                connection.close()
                print('mysql 커넥션 종료')
