# 파이썬-MySQL CONNECTION

스트림릿을 이용해서 웹페이지를 띄울 때  
데이터 베이스와 연동해서 할려면 db접속을 해서 원하는 데이터를 받아와야하는데    
그러려면 먼저 mysql-connector-python 라이브러리가 필요하다  

<br>

## 준비
가상환경이 되어있어야 한다, 없다면 (base)환경에서도 할 수 있지만 서버에도 배포한다면은 개발환경이 동일해야한다.   

먼저 가상환경을 activate로 가상환경이 실행이 되게 한 후,   
pip을 이용해서 설치  

```shell
$pip install mysql-connector-python 
```
을 입력한다 

<br>

## 파이썬 코드로 mysql_connector-phthon 사용하기

먼저 app.py의 파일에서 import를 해줘야한다  
처음으로 db에 접속할 정보들을 이용해서 접속을 한다  

이때 db서버, db이름, user정보, 비밀번호 등을 입력한다  
쿼리를 작성하여서 mysql connector의 메소드들을 이용해서,     
cursor()메소드와 execute()메소드, commit()으로 db를 입력하게 된다.  

<br>

## 먼저 셀렉트 해보기

___
```py
import streamlit as st
import mysql.connector

def main():
    connection = mysql.connector.connect(
        # 호스트명 (localhost가 아닌) AWS의 endpoint를 적는다
        host = '...rds.amazonaws.com',  # 외부 db서버를 사용할 경우
        database = 'mysql_db',
        user = 'mysql_계정',
        password = 'mysql_비번'  #실제 실무에서는 보안관련해서 따로 보관한다고 함 
    )

    # 먼저 mysql.connector.connect안에 host, database, user, password  
    # 파라미터를 이용해서 접속을 시도한다
    

    if connection.is_connected() :
        db_info = connection.get_server_info()
        print('server version: ', db_info)

        # 커서를 가져온다
        cursor = connection.cursor()
        # cursor메소드를 가지고 오면 이제 비로소 query를 할 수 있게 됨

        # execute()메소드로 쿼리를 직접 넣어주면 실행이 된다
        cursor.execute('select database();')
        
        # 이제 fetchone()을 사용해서 데이터를 받아온다
        record = cursor.fetchone()

        print('CONNECTED TO DB: ', record) #최종적으로 확인

if __name__ == '__main__':  
    main() 
```



