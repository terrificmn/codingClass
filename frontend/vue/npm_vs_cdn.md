#### npm 
Node Package Manager  
꼭 javascript가 아니더라도 다른 패키지의 의존성, install, version 등을 관리해준다   
npm을 설치하게 되면 package.json 파일이 생기는데 여기에 패키지, 버전 등이 입력되어 이를 바탕으로 설치를 하게 한다   
결국 npm 설치 및, webpack을 사용해야하는 것 같다  

[추후 읽어보기 how-to-use-npm-as-a-build-tool](https://www.keithcirkel.co.uk/how-to-use-npm-as-a-build-tool/)


#### CDN은  cache 파일
로 서버에 있음    
그래서 쉽게 다운로드 받아서 사용이 가능하고, script에 한줄만 넣어주면 된다   


## npm 으로 vue cli 설치
vue 설치는 `npm install vue@2.7`  으로 한다. (3.0 이상 버전은 해본적 없다)   

확실한 차이점은 npm으로 vue를 설치하는 것은 local에 관련 패키지를 설치하는 것이고,   
CDN으로 include? 하는 것은 암튼 CDN 을 이용해서 하는 것과는 다르게 되는 것 같다.  

vue 프레임워크가 아닌 cli모드에서 할 수 있는 패키지를 설치한다
```
npm install -g @vue/cli
```

> 물론 docker 컨테이너를 사요 해서 해야하므로 `docker compose run --rm npm install .... `   
> 그리고 vue-cli를 사용하는 vue 컨테이너를 만들었으므로, 위의 설치과정은 필요없다.  docker 빌드시에 생성


```
Error: Cannot find module '/var/www/html/vue'
    at Function.Module._resolveFilename (node:internal/modules/cjs/loader:933:15)
    at Function.Module._load (node:internal/modules/cjs/loader:778:27)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:81:12)
    at node:internal/main/run_main_module:17:47 {
  code: 'MODULE_NOT_FOUND',
  requireStack: []
```
이런 에러는 docker-compose.yml 의 volume 지정이 잘 안되서 그렇다  

nginx를 사용하고 있으므로, docker-compose.yml파일의 각 컨테이너의 volumes 부분은  
`./web_src:/var/www/html` 으로 맞춰준 상태   
그리고 working_dir은 `/var/www/html/web_motor` 로 실 web프로젝트로 지정을 해준다

> 현재 web_src 디렉토리안에 web관련 프로젝트(web_motor)가 있는 상황,    

npm, vue 컨테이너 등은 node의 node_modules 이 설치되는 실제 프로젝트 디렉토리에서 실행되야 하므로  
working_dir은 실제 패키지인 web_motor 까지 해준다   

[여기튜토리얼 따라해보기](https://likiipedia.com/getting-started-with-vue/)

npm 컨테이너만 사용할 경우에는 npm 이 엔트리포인트로 되어 있어서   
`docker compose run` 을 할 때 npm 컨테이너 이름만 해주면 자동으로 npm insatll ..    
등 처럼 바로 자연스럽게 사용할 수가 있는데   
대신에 npm으로 설치한 다른 것들은 실행할 수가 없다.  

예를 들어서 npx, vue 이런 것들은 안되기 때문에 docker-compose.yml의 entry 를 주석처리해서  사용하면 사용할 수는 있다 
주석을 해제하면 
```
docker compose run --rm npm npm install 
#또는 
docker compose run --rm npm vue --version
```

> 하지만 이것도 한계가 있는 것이, Working dir 등의 차이 때문에 실행은 되기 하나, 제대로 되기 힘들다 

## 그래서  아예 vue 컨테이너 만듬
vue 컨테이너가 생겼으므로 vue-cli는 여기에서 사용한다 

```
vue --version
```
도커에서는 
```
docker compose run --rm vue --version
```

다행히 제대로 vue-cli를 수행한다   

### vue로 새로운 프로젝트 만들기
`vue create my_project` 라고 하면 이제 vue 버전 2, 3을 고르는 메뉴가 나오고...   
새로운 프로젝트를 만들어준다  

이제 import를 할 때   
cdn 버전은 필요가 없으므로 빼버리고  (script 태그)
```
```

예를 들어 app.js 를 만들고 import를 해주는데   
`import Vue from 'vue';` 으로 하면 안됨 (많은 예제에 나와있지만,vue 3용인가?? 잘 모르겠다 ),   
아래처럼 해야지 제대로 인식한다

```js
import Vue from 'vue/dist/vue.js';

// 이제 Vue를 인스턴스 할 수 있다 
new Vue({ 
  ...블라브라 
  ... });
```

> 위 부분은 내 설정이 이상(?)해서 그럴 수도 있겠다는 생각이 든다..

### 기존 php 프로젝트에 합치기 
이제 만들어진 node_modules 디렉토리와, package.json 등을 포함해서 모두 기존 디렉토리로 이동 시켜준다   

> 아니면 처음부터 vue로 프로젝트를 만들고, 거기에 php 관련 index.php 파일을 넣어도 될 듯 하다  
> 어쨋든, php로 되어 있는 프로젝트여서 그렇게 합쳤다.. (현재까지는 laravel을 쓸 정도는 아닌 듯 하다)

