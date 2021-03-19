import streamlit as st

def select_query() :
    st.title('SELECT 쿼리를 선택하셨습니다.')
    st.subheader('맞춤 선택!')

    #booksColumn_list = ['타이틀', '출간년도', '작가', '남은수량', '페이지수']
    booksColumn_list = ['title', 'released_year', 'author_fname', 'stock_quantity', 'pages']
    chosenColumns = st.multiselect('보고 싶은 컬럼 선택하세요', booksColumn_list)
    if st.button('SELECT 하기') :

        connection = db_connection()

        if connection.is_connected() :
            
            cursor = connection.cursor(dictionary=True)  # 중요 딕셔너리 형태로 할려면 파라미터 true
            
            if len(chosenColumns) > 0 :
                selectedColumn = ", ".join(chosenColumns)
                query = " SELECT " + selectedColumn + """ FROM books
                        ; """
            
            # print(query)

                cursor.execute(query) #  쿼리 실행
                results = cursor.fetchall()
                #st.write(type(results))
                
                # 작은따옴표를 쌍따옴표로 바꿈
                # 파이썬의 리스트+딕셔너리 조합을 => JSON 형식으로 바꾸는 것
                json_results = json.dumps(results)

                #st.write(type(json_results))

                df = pd.read_json(json_results)
                st.dataframe(df)
                # for row in results :
                #     st.write(row)
                #     #print(row)
                
                #connection.commit() # update는 꼭 커밋을 해야함
                
                print("{}개 적용됨".format(cursor.rowcount))
            

            else :
                st.warning('한개 이상의 컬럼을 선택을 해주세요')