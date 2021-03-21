import streamlit as st
import pandas as pd
import json
from SqlController import SqlController

def select_menu() :
    st.title('SELECT 쿼리 메뉴를 선택하셨습니다.')
    st.subheader('맞춤 선택!')

    booksColumn_list = ['title', 'released_year', 'author_fname', 'stock_quantity', 'pages']
    chosenColumns = st.multiselect('보고 싶은 컬럼 선택하세요', booksColumn_list)
    
    limit = st.slider('몇개의 데이터를 보기 원하세요?')

    st.title('추가할것: 어떤 컬럼으로 정렬할지까지만 추가 (select 메뉴에서는)')
    if st.button('SELECT 하기') :
        Selector = SqlController()
        print('inside title cliced')
        table='books'
        result = Selector.sql_select(chosenColumns, table, limit)
        

        if result != False:
            json_results = json.dumps(result)
            df = pd.read_json(json_results)
            st.dataframe(df)
        
