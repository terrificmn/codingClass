Reset Password
1. click 'forgot Password'
2. fill out a form with their email address
3. prepare a unique token and associate it with the user's account
4. Send an email with a unique link back to out site that confirms email ownership
5. link back to website, confirm the token, and set a new password

일단 .env 파일을 
MAIL_MAILER=log   로 바꾼다

그리고 이메일 찾기 리셋을 누르면

storage/logs 에 가보면 
laravel.log 파일을 열어 맨 아래의 내용을 보면

Reset Password: http://127.0.0.1:8000/password/reset/33a4c88ba5d3ca1a59dc383b494e0b4feb7b2255405ad4c365f4c62b5bb809fb?email=john%40mail.com

여기에서 주소랑 토큰에 주목

그리고 데이터베이스의 paswword_resets 테이블을 보면
token컬럼에 데이터가 들어가져 있는데 
$2y$10$8XAQppwWH4aG8VC6AAIiGuaaUE4bU2rERtpQuxr5yu5Q1hYNSu2Ru
위의 토큰과 다르다. 바로 암호화된 hashed 토큰임

그리고 나면 그 주소를 카피해서 열어보자
그러면 비밀번호 리셋 페이지가 열리는데 여기에서 바로 패스워드를 바꿔주면

Your password has been reset! 
메세지와 함께 비번이 바뀜

그리고 
password_resets 테이블에 데이터는 자동 지워지고 

users 테이블의 패스워드도 바뀌어진다


어떤경로로 패스워드가 바뀌는 route 리스트 보기
$php artisan route:list


강좌에 나온 방식 (나중에 한다고 함: 기본셋팅은 아님)
.env 파일의
MAIL_MAILER=smtp
MAIL_HOST=smpt.mailtrap.io
MAIL_PORT=2525


_______

attacker.test

CSRF 기능이 있음
Cross-site request forgery 인데 
위키피아 내용을 보면
> CSRF attack an innocent end user is tricked by an attacker into submitting a web request that they did not intend

라고 함

