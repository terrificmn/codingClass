import mysql.connector
from mysql.connector import Error

#임포트해서 사용한다 (변수만 가져옴)
from config.config import db_conf

def get_mysql_connection() :
    try:
        # mysql reference에 나온 방식 변수(딕셔너리)로 사용할 때에는 **을 넣어준다
        connection = mysql.connector.connect( 
            **db_conf
        )

        if connection.is_connected() :
            #print('db connection OK!')
            return connection
    
    except Error as e:
        print('Error While connection to MySQL', e)
        return None