# laravel-mix

라라벨 믹스로 빌드
```
npm install laravel-mix --save-dev
npm install cross-env --save-dev
```


## webpack.mix.js 파일 만들기
빌드를 하기 위해서 webpack.mix.js 를 만들거나, node_modules/laravel-mix/webpack.mix.js를 복사해서 사용   

프로젝트의 root 디렉토리 이하에 webpack.mix.js 를 만들고 
```
cd ~/my-project
touch webpack.mix.js
```

내용은 
```js
let mix = require('laravel-mix');

mix.js('src/app.js', 'dist/')
    .sass('src/app.scss', 'dist/');
```

기본 설정이  src 이하이므로 src디렉토리가 없다면 만들어 준다.  그리고 app.js, app.scss 도 만들어준다   
app.js 파일과, app.scss 파일을 빌드해서 dist 디렉토리에 결과물로 만들어준다 
```
mkdir src && touch src/app.{js,scss}
```

그리고 package.json에 스크립트 부분에 추가를 해줘야 한다   
```json
"scripts": {
    "dev": "npm run development",
    "development": "mix",
    "watch": "mix watch",
    "watch-poll": "mix watch -- --watch-options-poll=1000",
    "hot": "mix watch --hot",
    "prod": "npm run production",
    "production": "mix --production"
},
```

기존... vue 2.7 버전 기준이고, (위의 코드를 사용하면 된다 )   
laravel-mix가 이때가 몇 인지는 모르겠지만, 튜토리얼은 vue 기준으로 봤을 때  
아래의 코드를 사용했다고 나오는데 이를 사용하면 에러 발생해서 실행이 안된다.. *참고만 하자*
```json
"scripts": {
    "dev": "npm run development",
    "development": "cross-env NODE_ENV=development node_modules/webpack/bin/webpack.js --progress --hide-modules --config=node_modules/laravel-mix/setup/webpack.config.js",
    "watch": "npm run development -- --watch",
    "watch-poll": "npm run watch -- --watch-poll",
    "hot": "cross-env NODE_ENV=development node_modules/webpack-dev-server/bin/webpack-dev-server.js --inline --hot --disable-host-check --config=node_modules/laravel-mix/setup/webpack.config.js",
    "prod": "npm run production",
    "production": "cross-env NODE_ENV=production node_modules/webpack/bin/webpack.js --no-progress --hide-modules --config=node_modules/laravel-mix/setup/webpack.config.js"
},
```

하지만 이미 laravel-mix는 업데이트 되어서 *--hide-module* 부분에서 에러가 발생한다   
> webpack 5 때부터 바꼈다고 한다     
> 그래서 위의 짧은 코드로 바귄 부분으로 사용한다   
또는 laravel-mix의 버전을 낮춘다. 그리고 다시 재 설치를 하고, 코드는 위에거 그대로 사용

만약 버전 다운그레이드라고 하면 package.json에서 
```
"laravel-mix": "^5.0.9"
```
그리고 `npm install` 을 다시 해주면 다운그레이드가 된다   

> 사실 테스트는 못해봤다   



## 빌드 run 
run watch는 한번 빌드 하고 계속 변경되면 새로 빌드 
```
npm run watch
```
도커 컨테이너는 `docker compose run --rm npm run watch`    
빌드르 한 후 script가 바뀔 때마다 계속 변경이 된다  

또는 아예 production 레벨로 (C++ 치면  release 버전쯤?) 빌드 하려면
```
docker compose run --rm npm run prod
```

중간에 laravel 믹스 후 run 실행 할 때 필요했던 것인가?? 기억이ㅣ;;;  
암튼 자동으로 깔려고 시도하는데, 도커래서 실패하는 듯   
수동으로 해주면 잘 깔림
```
 docker compose run --rm npm install sass-loader@^12.1.0 sass resolve-url-loader@^5.0.0 --save-dev --legacy-peer-deps
```



### webpack

webpack.mix.js 설정  프로젝트 root 아래 (카피, 없으며 만들기)

webpack.config.js 는 카피를 안해도 될 듯 (확인 필요)

패키지의 src에 app.js 와, app.scss 를 만든다   

dotenv-webpack 설치하기
```
docker compose run --rm npm install dotenv-webpack --save-dev
```


이것도 깔아봤는데 소용이 없는 듯 하다.. 에러는 안나지만,, 이미 process 가 된다.  
아마도 cross-env 때문에 이미 되는 것 아닌가 생각도 듬?  
드디어 .env 파일을 사용할 수가 있게 되었는데 꽤 공을 들인 만큼(?) 실망이;;; ㅠㅠ   
.env 로 불러오는 것 까지는 좋았는데   
laravel-mix로 빌드를 하면서 모든 .env 에서 불러온 값들이 다 노출이 되더라;;;;   
이럴 꺼면 뭐하러;;;;;'아놔   


> 다음에 할 때 dotenv-webpack 패키지가 필요한지 검증할 필요가 있을 듯 하다  
> 없어도 dotenv만으로 읽는 듯 하다?  또는 cross-env패키지를 설치해서??

