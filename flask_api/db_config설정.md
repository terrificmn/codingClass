# db를 함수화 하기
DB디렉토리를 하위에 하나 만들고, connection을 하기 위해서 
mysql.connector를 import한다
그리고 조금더 보안에 신경쓰기 위해서 
mysql.connector.connect() 부분의 파라미터를 파일화해서 다시 또 import한다

가상환경이라면은 상위 디렉토리에 db디렉토리를 만들어도 되지만 
docker환경에서 특정디렉토리를 workdir로 지정해놓은 경우에는 
해당 특정 디렉토리 하위에 db용 디렉토리를 구성해줘야함

```py
import mysql.connector
from mysql.connector import Error

#임포트해서 사용한다 (변수만 가져옴)
from config.config import db_config

def get_mysql_connection() :
    try:
        # mysql reference에 나온 방식 변수(딕셔너리)로 사용할 때에는 **을 넣어준다
        connection = mysql.connector.connect( 
            **db_config
        )

        if connection.is_connected() :
            print('connection OK!')
            return connection
    
    except Error as e:
        print('Error While connection to MySQL', e)
        return None
```
`from config.config import db_config`  
위에서 모듈을 불러올 때 config.config는 config 디렉토리 안에 config.py를 의미한다

그리고 그 config.py에 db_config라는 변수(딕셔너리 형태)를 만들고 불러오게됨
딕셔너리에는 mysql.connector.connect() 파라미터 값들이 들어가 있음
```py
db_config = {
    'host' : 'localhost',
    'database' : 'data_example',
    'user': 'user1',
    'password' : 'secret_passwd'
}
```
** 2개 붙이는 것은 형식이 그러함

# Config 클래스 
Flask에는 환경 설정용 클래스가 있는데 Config를 만들어서 사용하면 된다
속성 값을 할당해주고 그 값을 사용할 수가 있게 됨
이것도 위의 config.py 파일안에 만든다

DEBUG=True 
PORT="5003"
이런식으로 값을 지정해주면 됨

PORT 속성은 처음에 app.py 에서 
app 객체의 run() 메소드를 실행할 때 인자로 넣어주면 된다

예:
```py
app = Flask(__name__)  # flask 기본구조


if __name__ == "__main__" :
    app.run(port=Config.PORT) 
    
    # app.run()  #보통 아무 인자를 안주고 그냥 실행 시킬 수 있음

```
port=에 Config클래스의 PORT 속성을 이용해서 넣어주는 것 port=5001과 같은 효과