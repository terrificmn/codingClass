# css 잘 잡아주기
라즈베리파이 raspberry pi 에서 wordpress 설치 후 외부 (다른 pc에서)
ip로 접속했을 때 css가 제대로 표시되지 않는 경우에 웹 사이트가 제대로 표시가 되지 않는다.

이럴 때는 먼저 웹 브라우저에서 소스 보기를 한번 눌러서 디버깅을 시작

<img src=0>

보면 css link 부분이 다 localhost로 되어 있다. 이렇게 되면 외부에서도 localhost를 찾아서 
css경로를 못 찾게 되어서 css 처리가 안되게 된다.

라즈베리파이에서 웹브라우저 localhost/wordpress 라고 한 후 설정에서 바꿔줘야한다.

설정에서 localhost부분을 ip주소로 바꿔준다. 또는 도메인 이름으로(?) 한번 알아보기

