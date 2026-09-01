# vue 에서 .env 사용하기  (vue 2.7)
**vue install 하는 것만 참고 하고 나머지는 참고만 하자**   
**대신 npm_vs_cdn.md, laravel_mix사용.md 를 참고하자**   

.env 파일을 프로젝트 root 아래에 생성  
예 아래처럼 생성
```
ENV_TEST=hello_world_env
```

처음에 compose.yml에 프로젝트 디렉토리를 web_motor 프로젝트까지 포함시켜서  /var/www/html 로 연결되게 해준다 (volumn)   

물론 `docker compose run --rm` 으로 해줘야한다. 도커니깐..

npm install vue@2.7
npm run dev

npm  run dev를 했을 때
```
npm ERR! Missing script: "dev"
```

package.json에 js 파일이 설정이 안되어 있어서 그렇다.   
```json
"scripts": {
    "dev": "node app.js"
},
```

app.js를 만들고 `console.log()`를 해본다   

정확히 모르겠지만 vue3 이후부터는 dotenv가 필요없지는지도 모르겠지만..  
dotenv가 없으면 읽어오지 못하는 것 같다   

```
npm install dotenv --save
npm run dev
```

require를 한번 해주고 시작   
이제 app.js에 process.env로 접근이 가능하게된다 
예

```js
require('dotenv').config()
console.log(process.env.ENV_TEST)
```

참고
```
https://github.com/motdotla/dotenv
```

> vue3. 이후부터는? 정확하지 않다   
VUE_APP_ 으로 prefix를 붙여서 만들어야하는듯한데.? 일단 상관은 없는듯 하다

단독으로 할 경우에는 잘 되지만, php와 연동을 하면 전혀 안됨   
좀 더 찾아보자

npm run dev를 하면 app.js를 읽어서 환경변수를 읽지만, npm run dev 말고  
nginx 서버를 통해서 하려고 접속하면 오히려 require가 정의가 안 되어 있다고 에러가 발생  



### 빌드를 해야하는 듯 하다 (추후 참고만 하자;; 별로 읽어볼 거리는 아님 ㅋㅋ)
javascript 이니깐 바로 브라우저에서 읽어도 실행되는데는 문제가 없을 것이라고 생각했는데, 그게 아닌 것 같다.   

`npm run dev`를 통해서 특정 파일 root의 app.js 파일을 하게 했고  
.env 파일을 읽어와서 console.log()로 찍는 것이였는데.. 위의 방법대로 하면   
.env 파일에 지정했던 환경 변수 값이 잘 출력이 된다.   

그런데 php를 주로 사용하는 상황에서 그 app.js 파일을 script로 불러와봤자, require 나 import가 정의 된적 없다고 에러가 발생한다   

```
require is not defined
```
(아마도 node와 관련이 있는 것인가? 클라이언트쪽에서는 안 먹히는 듯 하다. )

이런 것을 봐서는 빌드를 해야하는 것 같은데.. 빌드를 하고 나온 파일을 script로 연결을 해줘야 그 내용을 볼 수가 있는 듯하다 

그래서 npm run build 식으로 해봤는데  dist/js/app.ad0fe202.js  에 빌드가 성공적으로 된다  

> npm run build를 하면 package.json의 script 부분에서 vue-cli-service build 로 실행이 되는 듯 하다   

어쨋든 이제 script를 불러들이면 requrire등을 없다는 등의 에러는 없다. 하지만 env 값을 출력해주지는 않는 것 같다

> 역시 기본이 중요한데.. javascript를 더 파악해야할 듯 하지만.. env파일 하나 쓸려다가 여기까지;; ㅠㅠ 추후 공부하자


## laravel-mix
webpack이라는 패키지로 빌드를 하는데 laravel-mix는 이를 쉽고 빠르게 도와준다고 해서 설치를 했다   

결론부터 말하자면 잘 된다. php 프레임워크인 laravel을 사용하지 않더라도 larave-mix를 빌드용으로 사용할 수 있다   

그래서 하게 되었다.  

> laravel-mix md 관련 참고
