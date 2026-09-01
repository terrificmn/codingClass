import streamlit as st
import mysql.connector
from mysql.connector import Error

def main():
    try:
        # 1. 커넥터로부터 커네션을 받는다.
        connection = mysql.connector.connect(
            # 호스트명 (localhost가 아닌) AWS의 endpoint를 적는다
            host = 'aws외부db서버',
            database = 'mydb',
            user = '',
            password = ''  #실제 실무에서는 보안관련해서 따로 보관한다고 함 (추후 배울예정)
        )

    
        if connection.is_connected() :
            db_info = connection.get_server_info() 
            print('MySQL server version: ', db_info)
            st.title(db_info)
            # 2. 커서를 가져온다
            cursor = connection.cursor()

            # 3. 우리가 원하는 거 실행 가능
            title = '행복한책'
            author_fname = '나나'
            author_lname = '김'
            released_year = 2020
            stock_quantity = 50
            pages = 361
            query = """insert into books (title, author_fname, author_lname, released_year, stock_quantity, pages)
                        values ( %s, %s, %s, %s, %s, %s);"""
            
            record = (title, author_fname, author_lname, released_year, stock_quantity, pages)

            cursor.execute(query, record)
            connection.commit()

            # 시간 넣어주는 예 - 이 경우는 param을 만들어서 넣어주면된다
            # param = (released_year, pages, order)
            # #record = (name, birth_date, birth_time, datetime.now())
            # record = (name, birth_date, birth_time, datetime.combine(birth_date, birth_time) )
            # #record = ('Mike', datetime.now(), datetime.now(), datetime.now())
            # print(datetime.now())

            #cursor.execute('select database();')

            # 4. 실행 후 커서에서 결과를 빼낸다
            #record = cursor.fetchone()
            #print('Connected to db: ', record)
            
            #try except 예외처리로 에러처리를 해준다 (import 필요)
    except Error as e :
        print('디비 관련 에러 발생', e)
    
    finally :  
        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다
        # 늦게 한 거 부터 커서, 커넥션 순서로 닫음
        #cursor.close()
        #connection.close()
        st.title("MySQL 커넥션 종료")

if __name__ == '__main__':  
    main() 