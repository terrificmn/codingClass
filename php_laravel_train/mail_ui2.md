라라벨은 javascript 로 만들어진 vue, bootstrap, react 의 프레임워크 등
프리셋을 지원해줌

(원래 preset 명령어 였는데 ui로 바꼈다고 함)
php artisan preset bootstrap 이거 이제 안됨

```
php artisan ui bootstrap
```

위의 vue, bootstrap, react 중에 선택해서 설치할 수 있는 듯

그 다음에 
Bootstrap scaffolding installed successfully.
Please run "npm install && npm run dev" to compile your fresh scaffolding.

이런 메세지가 나오고 

그 전에 
resources/sass 에 가보면
app.scss 파일이 있는데
그 안에 // Bootstrap이 지정이 되어 있는 것을 알 수 있음


npm install && npm run dev 를 실행해야함

npm은 자바스크립트 프레임워크의 패키지 매니저 임

npm과 nodejs 를 설치해야함
먼저 설치되어 있는지 확인해 볼것
```
node -v
npm -v
```

참고 현재 버전은 
node는 v14.16.0, npm은 7.6.0

npm install 한 다음에
```
$npm install
```

run dev를 해줌
```
npm run dev
```
rn dev는 컴파일을 하는 것인데 실제 javascript파일을 라라벨에서 사용할 수 있게 해주는 작업


이제 다시 localhost 페이지를 가보면 
로그인 영역이 깔끔하게 바뀌어 있음!

