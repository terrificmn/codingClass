from mysql.connector import connect
from SqlController import SqlController
import streamlit as st
import pandas as pd

def delete_menu() :
    
    st.title('DELETE 메뉴를 선택하셨습니다.')
    
    LIMIT = 7
    Deleter = SqlController()

    columns = ['book_id', 'title', 'author_fname', 'author_lname', 'released_year', 'stock_quantity', 'pages']
    table = "books"
    results = Deleter.sql_select(columns, table, LIMIT)
    
    show_df = pd.DataFrame(results )
    show_df.columns = ['book_id', '책', '이름' ,'성', '출판년도', '재고량', '페이지수' ]
    #show_df = show_df.drop('book_id', axis=1)
    st.dataframe(show_df)

    # selectbox에 사용하기 위한 리스트
    #selection_list = []
    selection_id_list = []
    for row in results:
        selection_id_list.append( row['book_id'])

    #print(selection_id_list)

    selected_id = st.selectbox('지우고 싶은 책 id를 선택해주세요.', selection_id_list)

    if st.button('삭제하기'):
        #st.warning('책 {}번 데이터가 삭제 됩니다.'.format(selected_id))
        if Deleter.sql_delete(selected_id) :
            st.success('책 {}번 데이터가 삭제 되었습니다.'.format(selected_id))
            print('책 {}번 데이터가 삭제 되었습니다.'.format(selected_id))
        else:
            st.warning('DB처리에 실패하였습니다.')