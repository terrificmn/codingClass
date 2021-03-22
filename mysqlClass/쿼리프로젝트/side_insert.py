from mysql.connector import connect
from SqlController import SqlController
from mysql.connector.connection import MySQLConnection
import streamlit as st
from mysql.connector import Error
import datetime

def insert_menu() :

    st.title(' INSERT를 선택하셨습니다.')
    title = st.text_input('책 이름')
    lastname = st.text_input('성')
    firstname = st.text_input('이름')
    year = st.number_input('출판년도', min_value=0, max_value=2200)
    quantity = st.number_input('재고량', min_value=0)
    pages = st.number_input('페이지수', min_value=0)

    if st.button('확인') :
        # 객체 생성
        Inserter = SqlController()
        
        if (Inserter.validation(title, lastname, firstname, year, quantity, pages )) : # validation 통과시 아래 실행
            if Inserter.sql_insert(title, lastname, firstname, year, quantity, pages ) :
                st.success('책 정보가 입력 되었습니다.')
            else:
                st.warning('DB처리에 실패하였습니다.')
