from mysql.connector import connect
from SqlController import SqlController
from mysql.connector.connection import MySQLConnection
import streamlit as st
from mysql.connector import Error
import datetime
import pandas as pd

def update_menu() :
    st.title('UPDATE 메뉴를 선택하셨습니다.')

    st.info('현재 저장되어 있는 책 리스트 입니다.')

    Updater = SqlController()
    columns = ['book_id', 'title', 'author_fname', 'author_lname', 'released_year', 'stock_quantity', 'pages']
    table = "books"
    results = Updater.sql_select(columns, table, limit=10)
    
    show_df = pd.DataFrame(results )
    show_df.columns = ['book_id', '책', '이름' ,'성', '출판년도', '재고량', '페이지수' ]
    #show_df = show_df.drop('book_id', axis=1)
    st.dataframe(show_df)

    # selectbox에 사용하기 위한 리스트
    #selection_list = []
    selection_id_list = []
    for row in results:
        selection_id_list.append( row['book_id'])
        #selection_id_title.append( [ row['book_id'], row['title'] ]  )
        #selection_list.append([row['book_id'], row['title'], row['author_fname'], row['author_lname'], row['released_year'], row['stock_quantity'], row['pages']])

    book_id = st.selectbox('원하는 목록을 선택하세요', selection_id_list)
    amendTitle = st.text_input('책 이름을 입력하세요')
    amendLastname = st.text_input('바꿀 성을 입력하세요')
    amendFirstname = st.text_input('바꿀 이름을 입력하세요')
    amendYear = st.number_input('출판년도', min_value=0, max_value=2200)
    amendQuantity = st.number_input('재고량', min_value=0)
    amendPages = st.number_input('페이지수', min_value=0)

    if st.button('바꾸기') :
        #print(book_id, amendTitle, amendLastname, amendFirstname, amendYear, amendQuantity, amendPages)
        val_result = Updater.update_validation(book_id, amendTitle, amendLastname, amendFirstname, amendYear, amendQuantity, amendPages)
        #print(val_result)
        if val_result :
            if Updater.sql_update( val_result ):
                st.success('수정 완료 되었습니다!')
            else:
                st.warning('DB처리에 실패하였습니다.')