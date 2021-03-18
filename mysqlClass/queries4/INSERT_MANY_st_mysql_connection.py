import streamlit as st
import mysql.connector
from mysql.connector import Error

def main():
    # 예외처리를 사용해서 에러가 발생했을 때 어떻게 에러가 나는지 알 수 있다
    try:
        # 1. 커넥터로부터 커네션을 받는다.
        connection = mysql.connector.connect(
            # 호스트명 (localhost가 아닌) AWS의 endpoint를 적는다
            host = 'your-host-aws',
            database = 'my_edu_db',
            user = 'your-user-name',
            password = 'your-pass-word'  #실제 실무에서는 보안관련해서 따로 보관한다고 함 (추후 배울예정)
        )

        if st.button('save'):

            if connection.is_connected() :
                db_info = connection.get_server_info() 
                st.text('MySQL server version: ')
                st.text(db_info)
                
                # 2. 커서를 가져온다
                cursor = connection.cursor()

                # 3. 우리가 원하는 거 실행 가능
                query = """insert into cats4 (name, age)
                            values ( %s, %s);"""
                
                # cursor.execute()를 시켜주기 위해서는 values 부분은 ( )튜플로 묶어줘야한다
                #cursor.execute('select database();') 바로 쿼리를 넣어주면 db데이터를 받아오거나 입력할 수 있다
                #record = ('야옹이',  1) 한개만 넣은 때는 cursor.execute(query, record)로 실행이 되지만
                #cursor.execute(query, record)

                #여러개를 넣을 때는 리스트로 만든 후에 executemany()를 실행한다
                record = [ ('냐옹이', 1), ('나비', 3), ('단비', 5)]
                cursor.executemany(query, record) # 여러개를 입력할 때
                
                # 마지막 반영은 commit()을 한다
                connection.commit() 

                # 4. 실행 후 커서에서 결과를 빼낸다
                # select일 때는 fetchone을 사용
                #record = cursor.fetchone()
                #print('Connected to db: ', record)
                
                #try except 예외처리로 에러처리를 해준다 (import 필요)
    except Error as e :
        #print('디비 관련 에러 발생', e)  // docker에서는 터미널로 프린트가 안된다 이유는 아직 모름
        st.warning(e)
    
    finally :  
        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다
        # 늦게 한 거 부터 커서, 커넥션 순서로 닫음
        #cursor.close()
        #connection.close()
        st.warning("MySQL 커넥션 종료")

if __name__ == '__main__':  
    main() 