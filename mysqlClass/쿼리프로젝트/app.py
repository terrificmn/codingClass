from SqlController import SqlController
import streamlit as st
import mysql.connector
from mysql.connector import Error
#from datetime import datetime

import pandas as pd
import numpy as np

#from side_select import select_query
from side_select import select_menu
from side_insert import insert_menu
from side_update import update_menu
from side_delete import delete_menu

st.set_page_config(page_title='MYSQL', layout='wide', initial_sidebar_state='auto')
def main():
    sidebar_choice = st.sidebar.selectbox('선택하세요', ['선택하세요', 'SELECT', 'INSERT', 'UPDATE', 'DELETE'])

    if sidebar_choice == '선택하세요' :
        st.title ('안녕하세요.')
        
        st.info(' 보고계시는 현재 이 웹 어플리케이션은 Python으로 제작되었으며,')
        st.info('Streamlit프레임워크와 MySQL를 이용하여')
        st.info('가상의 book store에 데이터를 주고 받는 것을 가정하였습니다.')
        st.info('마음껏 더미 데이터를 테스트 해보세요! 감사합니다.^^')

    elif sidebar_choice == 'SELECT':
        select_menu()

    elif sidebar_choice == 'INSERT':
        insert_menu()
        
    elif sidebar_choice == 'UPDATE':
        update_menu()
    
    elif sidebar_choice == 'DELETE':
        delete_menu()


if __name__ == '__main__':
    main()