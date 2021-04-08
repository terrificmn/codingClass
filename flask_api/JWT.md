JSON Web Token
유저 승인을할 때 클라이언트와 서버 간에 사용할 수 있게 하는 인증방식

여러가지 인증방식이 있지만 그 중에 하나이다

[공식페이지](https://jwt.io/)

HEADER
PAYLOAD 에 보통 id를 넣어서 보낸다
db에 id가 있으면 해당아이디를 암호화 시켜서 토큰을 발행한다

예를 들어서 특정아이디 14번이 데이터베이스에 있다면
14번에 해당하는 것을 JWT를 이용해서 토큰을 (암호화된) 발행한다

그리고 이 토큰을 클라이언트 사용자에게 돌려준다.

이제 사용자가 요청을 할 때에는 특히 인증이 필요할 때에는 
header에 토큰을 넣어서 호출 요청을 해야한다

예를 들어 사용자가 내 정보를 수정한다고 하면 header에 토큰을 넘겨서 
보내는 것인데 
서버에서는 JWT로 암호화된 토크를 확인해서 맞으면
사용자 내 정보를 수정하게 되고,
아니라면 승인 실패코드를 보낸다.

파이썬에서는 
Flask-JWT-Extended 라이브러리를 사용해야한다

[PYPI 해당 라이브러리 설치](https://pypi.org/project/Flask-JWT-Extended/)

라이브러리들
create_access_token() - 회원가입할 때 발행
@jwt_required(optional=False) : 무조건 토큰 필요할 때 사용, 만약 True이면 토큰이 필요하지않게 됨
get_jwt_identity() - 유저 정보를 가져올 때 사용
get_jwt


config/config.py 에 시크릿 키를 설정해준다
예:
```py
SECRET_KEY =- '1234_secret_jwt'
```

app.py에는 라이브러리 import및 환경설정
```py
from flask_jwt_extended import JWTManager

# 1-1 JWT 환경 설정
jwt = JWTManager(app)
# 로그인/로그아웃 관리를 위한 JWT 설정
# jwt 매뉴얼에 나와있는 것
@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload) :
    jti = jwt_payload['jti']
    return jti in jwt_blocklist  #blocklist가 없으므로 user.py에 만들어 준다
```

user.py 에는 

```py
# 유저 인증을 위한 JWT 라이브러리 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt

# 로그아웃 기능 구현
from flask_jwt_extended import get_jti

```

레시피를 생성하는 API에서 
헤더에 추가
key 추가 Authorization : value 는 Bearer
여기에서 Bearer 한칸띄고 토큰을 넣어준다

회원가입을 하고 나온 토큰을 저장해놨다가...
이런식으로 
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNzg1MTkyNiwianRpIjoiNDlkYjZkZDYtMWQ1OS00NWIyLWExYzItZjYwYjU1N2VhOGM2IiwibmJmIjoxNjE3ODUxOTI2LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoxMiwiZXhwIjoxNjE3ODUyODI2fQ.w4SaL5rZ8ylqGIpDRt5pUVbPEMY9dhbxm_FdZbRcxik

이 토큰은 user 테이블의 id를 JWT를 이용해서 암호화했기 때문에 id 그 자체이다
(암호화를 풀면 id가 나온다)

이제 클라이언트에서는 헤더부분에 토큰을 넣어서 보내야한다

서버에서는 해당 기능을 할 (예를 들어 회원정보 보기)이면 post() 메소드 바로 위에 
```py
@jwt_required() 
def post(self, user_id):
    pass
```
위의 같은 방식으로 넣어주면
헤더를 auth를 추가안하고 보내면 에러가 나게 된다.

그리고 나서 유저 아이디를 암호화 해서 토큰을 한 것을 복화화해서 
이때는 
```py
token_userId = get_jwt_identity()
```
를 해주면 바로 id로 바꿀 수가 있다. 

그리고 나서 db에 SELECT문으로 쿼리를 해서 나온 id와 비교를 해주게 되고 
맞으면 진행
틀리면 에러코드를 진행할 수 있게 해주는 식으로 한다
예를 들어서 
```py
if token_userId != user_id :
    return { "err_code" : 1}, HTTPStatus.UNAUTHORIZED
```
