## 우분투 ubuntu frontend-preset? 설치 할 때 에러 (laravel 프레임워크)
npm으로 먼가 설치할 때 에러가 나면   
아마 설치는 완료되는 마무리가 안되는 듯

yarn 없다고 에러가 나면 
```
sudo apt-get install yarn 
```

npm run development가 실행될 때 mix 부분에서 에러가 남   
```
mix: not found cde 127
```


설치 후에 다시 npm install 진행하던 것을 다시 해주면 됨   

그래도 
```
run dev 
```
했을 때 아래 처럼 나오면
```
[npm err] mix: not found 
```
이런식으로 또 에러가 나면 컴파일이 실패하는 건데

자신의 프로젝트 루트 디렉토리안에서 package.json 을 찾는다   
(라라벨로 만든 프로젝트명 및 디렉토리, exer로 했었음)

package.json 열어서 "devDependenciees" 키에 해당하는 값 중에서  
"laravel-mix": "^5.0.1" 처럼 되어 있는 것을    
버전을 바꿔준다
```
"laravel-mix": "^6.0.6",
```

그 후 컴포져 업데이트
```
composer update
```

그리고 나서 다시 
```
$npm install && npm run dev
```

다시 설치가 진행되고 드디어 이런메세지를 볼 수 있다
```
Laravel Mix v6.0.13
Compiled Successfully

webpack compiled Successfully
```

[참고사이트 깃허브](https://github.com/laravel/laravel/blob/master/package.json#L14)


## 우분투에서 nodejs 설치하기
역시 centos 랑 비슷하게 설치가 되어 있는 버전은 10.19 버전인가가 설치되어 있음   
업데이트는 최신버전이라고 안 되고  

> 일단 버전은 계속 바뀌므로 node 공식 사이트에서 확인할 것

15번 기준으로 설명, 먼저 리포지터리를 추가해서 설치를 해야함  
```
curl -sL https://deb.nodesource.com/setup_15.x | sudo -E bash -
```
만약 14버전: 안정화 버전을 설치하려면 setup_15.x 의 숫자만 바꿔준다

그리고 하려고 하는데 curl 명령어가 없다고 하면
```
sudo apt-get install curl
```

다시 위의 리포지터리 추가하는 명령어 실행

그다음에 진짜 설치
```
sudo apt-get install nodejs
```

버전확인
```
node -v
npm -v
```

각각 버전 15.11.0     
7.6.0

