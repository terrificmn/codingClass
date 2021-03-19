import streamlit as st
import mysql.connector
from mysql.connector import Error
#from datetime import datetime
from db import db_connection

def main():
    book_id_list = []
    try:
        connection = db_connection()
        if connection.is_connected() :
            cursor = connection.cursor(dictionary=True)
            query = """ SELECT *
                        FROM books LIMIT 5; """
            
            cursor.execute(query)
            results = cursor.fetchall()

            for row in results:
                st.write(row)
                book_id_list.append( row['book_id'])

    except Error as e :
        print('Mysql에러:', e)
    finally:
        cursor.close()
        connection.close()
        print ('MySql connection 종료되었습니다.')

    # number_input()을 만들 때 위에서 book_id_list리스트에 추가한 'book_id'컬럼 값을 
    # 첫번째로 (최소 지정값으로 나오게 하고) , 마지막 요소를 (최대 지정값으로 셋팅)
    book_id = st.number_input('책 아이디번호 입력',min_value= book_id_list[0], max_value= book_id_list[-1])

    if st.button('삭제하기'):
        try:
            connection = db_connection()
            
            if connection.is_connected() :
                
                cursor = connection.cursor(dictionary=True)  # 중요 딕셔너리 형태로 할려면 파라미터 true
                
                query = """ DELETE FROM books
                            WHERE book_id = %s; """

                data = (book_id,)  # 꼭 튜플로 만들어야 한다 (한 개일때도 ,  를 찍는다 )
                # , 를 안찍으면 튜플로 생성이 안됨
                cursor.execute(query, data) #  쿼리 실행

                connection.commit() # update는 꼭 커밋을 해야함
                
                print("{}개 적용됨".format(cursor.rowcount))

        except Error as e:
            print('디비 관련 에러 발생', e)

        finally:
            cursor.close()
            connection.close()
            print('mysql 커넥션 종료')


if __name__ == '__main__':
    main()