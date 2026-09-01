# 파이썬에서 mysql-connector-python 로 mysql연결

스트림릿을 이용해서 웹페이지를 띄울 때 (또는 db연결이 필요할 때)  
데이터 베이스와 연동해서 할려면 db접속을 해서 원하는 데이터를 받아와야하는데  
그러려면 python에서는 mysql-connector-python 라이브러리가 필요하다  

<br />

## 설치 
mysql-connector-python 라이브러리 설치하기   
만약 가상환경이 있다면 activate 시켜서 가상환경이 실행되게 한 후 설치하면 좋다.   
가상환경이 없다면 기본 base 환경에서 설치하면 됨  


```shell
$pip install mysql-connector-python 
```

<br />

## 파이썬 코드로 mysql-connector-phthon 사용하기

먼저 app.py의 파일에서 import를 해줘야한다 import mysql.connector  
처음으로 db에 접속할 정보들을 이용해서 접속을 한다  
이때 db서버, db이름, user정보, 비밀번호 등을 입력한다  
쿼리를 작성하여서 mysql connector의 메소드들을 이용해서,     
cursor()메소드와 execute()메소드, commit()으로 db를 입력하게 된다.  

<br />

## 먼저 셀렉트 해보기
아래는 mysql 연결과 간단하게 db연결이 잘 되었는지 확인할 수 있는 코드임
```py
#app.py 

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
위의 코드와 주석 설명을 참고하자

<br/>

## DB 접속 관련 데이터 파일 분리하기
위의 connection을 하는 부분에서는 다른 파일을 만들어서 보관하는게 좀 더 보안성에 좋다.   
(그래서 실제 실무에서도 사용하는 방법이라고 함)

먼저 db_config.py 라는 파일을 따로 만들고 그 안에 db접속에 필요한 데이터만 복사 한다.   
그리고 변수를 만들어서 저장~   
중요한 점은 딕셔너리 형태로 만들어 줘야한다는 것에 주의하자!  

```py
# db_config.py
db_conf = {
    'host' : 'database-1.amazonaws.com',
    'database' : 'my_database_name',
    'user': 'your-username',
    'password' : 'your-secret-password'
}
```

<br/>

이제 app.py 파일을 불러온다  
그리고 위에 만든 db_config.py를 import를 해주고 코드를 조금 수정해준다

```py
# app.py

from db_config import db_conf

# .. 생략..

    connection = mysql.connector.connect( 
            **db_conf
    )

# .. 생략..
```
참고로 ** 을 넣어주는 것은 매뉴얼에 나와 있는 방법이다.  
[참고mysql.connector사용법-매뉴얼](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)  

이제 좀 더 편하게 사용을 하려면 아예 db 연결하는 부분을 함수로 만들어 주는 것이다.  
그리고 다른 코드에서 필요할 때마다 호출해서 쓰게하면 좋다

<br/>

## 함수로 만들고 try , except, finnally 를 활용해서 예외처리 하기

먼저 함수로 만들기. db.py라는 파일을 만들어 준다.
함수로 만든다

```py
#db.py
import mysql.connector

# 위에서 만든 db_conf도 가져온다
from db_config import db_conf

def get_mysql_connection() :
    # mysql reference에 나온 방식 변수(딕셔너리)로 사용할 때에는 **을 넣어준다
    connection = mysql.connector.connect( 
        **db_config
    )

    if connection.is_connected() :
        return connection
```

위에서 만든 get_mysql_connection()함수는 연결이 되면 connection 변수를 리턴하게 된다.  
이제 원하는 곳에서 db연결이 필요하면 함수를 호출하면 된다.  
예:

```py
# any_file.py

#db.py파일의 함수를 임포트
from db.py import get_mysql_connection

conection = get_mysql_connection()
```

db연결에 실패했을 경우에 대비해서 예외처리를 해주자.  
다시 db.py파일을 조금 수정해준다   
이때는 mysql.connector의 Error 객체가 필요하므로 임포트를 하자 

```py
import mysql.connector
from mysql.connector import Error

from db_config import db_conf

def get_mysql_connection() :
    try:
        # mysql reference에 나온 방식 변수(딕셔너리)로 사용할 때에는 **을 넣어준다
        connection = mysql.connector.connect( 
            **db_conf
        )

        if connection.is_connected() :
            print('connection OK!') # 디버깅용~ 확인
            return connection
    
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    
```

끝!

