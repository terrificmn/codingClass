
## postman 을 이용해서 api 사용하기
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
