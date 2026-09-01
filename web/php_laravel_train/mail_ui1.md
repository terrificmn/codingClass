메일 보내기

메일헬프보기
php artisan help make:mail

-m 옵션은 마크다운템플릿을 만들어 주는데 리소스/뷰즈 에 블레이드로 만들어 준다

-m 플래그 뒤에는 경로를 적어준다. (파일은 만들필요없음 아티잔이 만듬)
```
php artisan make:mail WelcomeMail -m emails.welcome
```
즉 emails/welcome.blade.php 가 만들어짐

이제
app/Mail 에 WelcomeMail.php 가 생김 Mailable 의 상속받은 클래스로 만들어짐

그리고 
resources/views/emails 가 생김
그 안에 welcome.blade.php 가 생겨있고 

이제 routes/web.php 파일에서 

블레이드 페이지를 써주고 
```
Route::get('/email', function() {
    return new WelcomeMail(); //만든 WelcomeMail() 리턴/ url로 /email 만치면됨
});
```


http://127.0.0.1:8000/email
브라우저에 입력하면 
메일 입력이 생김

맨 위의 로고를 바꾸려면
.env 파일의 
맨 처음 APP_NAME= 부분을 바꿔주면 되고 띄어쓰기로 쓸 경우에는 "" 로 묶어야 함
예: 
```
APP_NAME="Laravel Cool Application"
```
원래 기본상태
```
APP_NAME=Laravel
```

적용하려면 php artisan serve 를 다시 해야함


또 env 파일을 보면
MAIL_MAILER=smtp
MAIL_HOST=mailhog
MAIL_PORT=1025
부분이 있는데 

먼저 mailtrap을 가입한다. 테스트 메일을 보낼 수 있는 곳임
https://mailtrap.io 에서 로그인 후 
SMTP Settings 를 보면  Integration에서 프레임워크를 선택할 수 있는데 여기에서 Laravel을 선택하면 필요정보가 나옴
Mail_mailer, mail_host, mail_port, username, password를 이거를 .env 파일에 입력한다

그리고
```
MAIL_MAILER=smtp
MAIL_HOST=smtp.mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=3712내아이디296492
MAIL_PASSWORD=c508내비번14141234
```

그리고 serve를 중지하고 재시작한다

다시 email페이지를 새로고침하면 welcome 블레이드 파일에서 수정한것이 바로 메일로 보내짐

근데 에러
 $this->throwException(new Swift_TransportException('Cannot send message without a sender address'))

그래서 일단
env 파일의 대충 보내는 메일 수정해줌
```
MAIL_FROM_ADDRESS=test@email.com 
```

다시 재시작하니 잘 보내짐
암튼 페이지에서 새로고침을 하면 메일화면이 보여지면 됨

그리고 다시 Mailtrap 사이트에 가보면 
메일이 온 것을 알 수 있음

** Mailtrap은 실제로 메일을 보내지 않으면서 테스트를 할 수 있는 곳임

이제 유저가 (customer) 회원가입을 했을 때 자동으로 보내게 할려면

컨트롤러의 store()메소드에 아래처럼 한줄코드 넣어주면 끝
```php
Mail::to($customer->email)->send(new WelcomeMail()); // customer의 email을 가지고 온 다음에 WelcomeMail() 클래스 이용해서 바로 보내줌
        // 현재 mailtrap으로 설정되어 있어서 거기서 메일 확인할 수 있고
        // 위에 use로 import를 해줘야한다. Mail과 WelcomeMail 둘다
        //use App\Mail\WelcomeMail; 
        //use Illuminate\Support\Facades\Mail;
```

지금은 mailtrap 사이트를 이용하기 때문에 보내는 더미 이메일 주소도 상관없다 
이제 회원가입을 해보고
http://127.0.0.1:8000/customers

mailtrap에서 확인해 보면 자동으로 메일이 발송된것을 알 수 있음! 굿!

진짜 메일을 보내려면 서비스를 이용해야하는데
그중 셋팅 쉽고 무료 메일 추천:
> Mailgun.com 쉬운 한달 50,0000건 메일발송까지 free










