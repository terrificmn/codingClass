# yarn 패키지, package.json 로 script 활용

설치는  
[yarn_install_&_build_error 참고](./yarn_install_&_build_error.md)


이후 `packkge.json` 파일의 `"scripts"` 에 키 : value 를 넣어주고 yarn 으로 실행할 수가 있다


```json
{
    // 생략..
    "scripts": {
        "test": "echo \"hello\" ",
    }
    // 생략..
}
```

실행은 핧 수가 있다.
```
yarn test
```


build, serve 등으로 추가해서 사용할 수가 있는데   
`vue-cli-service` 등을 이용해서 서비스를 하려면 해당 라이브러리가 필요할 것   
(아직 해보지는 못함)   


## nvm use 스크립트로 사용
`.nvmrc` 파일을 만들고 버전 명시
```
v14.21.3
```

> 노드 버전을 다르게 사용할 경우에 사용할 경우에 script 로 실행하면 좋은 것 같다.

이제 `nvm use` 명령만 사용하면 되지만 yarn script로 실행하게 되면  
환경 변수를 읽어오지 못해서 nvm 자체를 실행해주지 못한다. 

아예 스크립트로 만들자

해당 프로젝트에 대충 스크립트 파일 만들기
```
cd my_pkg
mkdir script; cd script
touch my_script
```

my_script 파일에는 
```sh
#!/bin/bash

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

nvm use
node main.js
```

이후 파일 실행권한 만들어 주고 
```
chmod +x script/my_script
```

해당 프로젝트의 package.json 파일에   
```json
{
    // 생략..
    "scripts": {
        "serve": "./script/my_script",
    }
    // 생략..
}
```

실행은 
```
yarn serve 

## 또는
yarn run serve
```

