# JSON Web Token , JWT
유저 승인을할 때 클라이언트와 서버 간에 사용할 수 있게 하는 인증방식

여러가지 인증방식이 있지만 그 중에 하나이다

[공식페이지에서 보기: https://jwt.io/](https://jwt.io/)

HEADER
PAYLOAD 에 보통 id를 넣어서 보낸다  
db에 id가 있으면 해당아이디를 암호화 시켜서 토큰을 발행한다 

예를 들어서 특정아이디 14번이 데이터베이스에 있다면
14번에 해당하는 것을 JWT를 이용해서 토큰을 (암호화된) 발행한다

그리고 이 토큰을 클라이언트 사용자에게 돌려준다.

이제 사용자가 요청을 할 때에는 특히 인증이 필요할 때에는 
header에 토큰을 넣어서 호출 요청을 해야한다

예를 들어 사용자가 내 정보를 수정한다고 하면 header에 토큰을 넘겨서 보내는 것인데   
서버에서는 JWT로 암호화된 토크를 확인해서 맞으면  
사용자 내 정보를 수정하게 되고, 아니라면 승인 실패코드를 보낸다.  

파이썬에서는 JWT를 사용하기 위해서는  
Flask-JWT-Extended 라이브러리를 사용해야한다

<br>

# 라이브러리 설치하기

[PYPI 해당 라이브러리 설치](https://pypi.org/project/Flask-JWT-Extended/)

```shell
$pip install Flask-JWT-Extended
```

<br>

이제 JWT라이브러리의 함수를 살펴보자  
create_access_token() 
- 암호화 토큰을 만들어 준다
- 예: 회원가입시, 로그인시 발행하게 한다

@jwt_required(optional=False) : 
- 무조건 토큰 필요할 때 사용 
- 만약 True이면 토큰이 필요하지않게 됨  

get_jwt_identity() 
- 유저 정보를 가져올 때 사용
- 암호화된 토큰을 해석해준다 
- 복호화가 되면 user id 값이 나오게 된다

시크릿 키 설정  
- 예: config/config.py 에 시크릿 키를 설정해준다  
- 변수를 만들고 사용하면 됨
- 다른파일에 있다면 import하기

```py
SECRET_KEY =- '1234_secret_jwt'
```

<br>

## jwt 라이브러리 사용해보기

app.py 에는 라이브러리 import및 환경설정을 해준다
```py
from flask_jwt_extended import JWTManager
from user import jwt_blocklist 

# 1-1 JWT 환경 설정
jwt = JWTManager(app)
# 로그인/로그아웃 관리를 위한 JWT 설정
# jwt 매뉴얼에 나와있는 것
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blocklist  #blocklist가 없으므로 user.py에 만들어 준다
```


user.py 에는 아래처럼 만들어 준다

```py
# 유저 인증을 위한 JWT 라이브러리 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

# 로그아웃 기능 구현
from flask_jwt_extended import get_jti

```
