ENV_TEST=hello_world_env

It works, but not sure if it is working with php 

처음에 compose.yml에 프로젝트 디렉토리를 web_motor 프로젝트까지 포함시켜서  /var/www/html 로 연결되게 해준다 (volumn)   

물론 `docker compose run --rm` 으로 해줘야한다. 도커니깐..

npm install vue@2.7
npm run dev

npm  run dev를 했을 때
```
npm ERR! Missing script: "dev"
```

package.json에 js 파일이 설정이 안되어 있어서 그렇다.   
```
"scripts": {
    "dev": "node app.js"
},
```

app.js를 만들고 `console.log()`를 해본다   

정확히 모르겠지만 vue3 이후부터는 dotenv가 필요없지는지도 모르겠지만..  
dotenv가 없으면 읽어오지 못하는 것 같다   

npm install dotenv --save
npm run dev

require를 한번 해주고 시작   
이제 app.js에 process.env로 접근이 가능하게된다 
예
```
require('dotenv').config()
console.log(process.env.ENV_TEST)
```


참고
```
https://github.com/motdotla/dotenv
```

.env 파일을 만들고 변수를 만들어준다 

> vue3. 이후부터는? 정확하지 않다  
VUE_APP_ 으로 prefix를 붙여서 만들어야하는듯한데.? 일단 상관은 없는듯 하다


단독으로 할 경우에는 잘 되지만, php와 연동을 하면 전혀 안됨   
좀더 찾아보자


확실한 차이점은 npm으로 vue를 설치하는 것은 local에 관련 패키지를 설치하는 것이고,   
CDN으로 include? 하는 것은 암튼 CDN 을 이용해서 하는 것과는 다르게 되는 것 같다.  

시도해 볼 것 cli 모드

```
npm install -g @vue/cli
```

