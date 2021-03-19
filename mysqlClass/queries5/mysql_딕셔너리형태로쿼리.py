import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from db import db_connection

def main():
    st.text('몇년도 이후, 몇페이지 이상되는 책을 검색하고 싶으십니까?')
    released_year = st.number_input('년도 입력', min_value=0)
    pages = st.number_input('페이지수 입력', min_value=0)

    if st.checkbox('내림차순 정렬하기'):
        order = 'DESC'
    else :
        order = 'ASC'

    if st.button('전송'):
        try:
            connection = db_connection()
            
            if connection.is_connected() :
                db_info = connection.get_server_info()
                #print(released_year, pages, order)

                print('MYsql server version: ', db_info)

                cursor = connection.cursor(dictionary=True)  # 중요 딕셔너리 형태로 할려면 파라미터 true
                
                query = """ SELECT title, released_year, pages
                        FROM books
                        WHERE released_year > %s and pages > %s
                        ORDER by released_year """ + order + ';'
                
                param = (released_year, pages)
                

                cursor.execute(query, param) #  쿼리 실행

                results = cursor.fetchall()
                
                # 딕셔너리 형태로 받으려면 cursor를 받아올 때 dictionary=True 로 설정
                print(results)
                for data in results:
                    print(data['title'], data['released_year'])


                #connection.commit()  
                print("{}개 적용됨".format(cursor.rowcount))

                #cursor.execute('select database();')
                #record = cursor.fetchone()

        except Error as e:
            print('디비 관련 에러 발생', e)

        finally:
            cursor.close()
            connection.close()
            print('mysql 커넥션 종료')

if __name__ == '__main__':
    main()
    