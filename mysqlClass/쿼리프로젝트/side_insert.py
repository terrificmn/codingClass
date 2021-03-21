from mysql.connector import connect
from SqlController import SqlController
from mysql.connector.connection import MySQLConnection
import streamlit as st
from mysql.connector import Error
import datetime

def insert_menu() :
    st.write('hello')

    # Duty = SqlController()
    # Duty.sql_insert()
    st.title('회원 가입 INSERT를 선택하셨습니다.')
    name = st.text_input('이름: ')
    email = st.text_input('이메일: ')

    if st.button('확인') :
        # 객체 생성
        Inserter = SqlController()
        
        if (Inserter.validation(name, email)) : # validation 통과시 아래 실행
            if Inserter.sql_insert(name, email) :
                st.success('회원 가입되었습니다. (데이터베이스에 입력되었습니다.)')
            else:
                st.warning('DB처리에 실패하였습니다.')
