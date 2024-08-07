# nodejs nvm으로 설치하기
프로젝트에서  
호환성 문제로 node js를 맞춰야 하는 경우  
```
The engine "node" is incompatible with this module. Expected version "8 || 10 || 12 || 14 || 16 || 17". Got "20.12.2"
```

이런식으로 에러가 발생할 수 있다. 

현재 2024년 7월 기준 fedora 에서 dnf로 설치를 하면 20버전이 설치 되는 듯 하다.

nodejs에서 Download페이지에서 nvm 으로 편하게 설치할 수 있다.

dnf로 설치하지 말고 nvm 으로 설치 권장
> `dnf install npm` 으로 설치를 안해도 된다.


installs nvm (Node Version Manager)
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

download and install Node.js (you may need to restart the terminal)
```
nvm install 17
```
> 버전을 17/ 18 이런식으로 선택할 수 있다.

verifies the right Node.js version is in the environment
```
node -v # should print `v17.9.1`
```

verifies the right npm version is in the environment
```
npm -v # should print `8.11.0`
```

nodejs 셋팅npm트러블슈팅.md 에서 사용한 방법으로도 테스트 해보기 


# nvm을 이용해서 삭제하기 
```
nvm deactivate
nvm uninstall 17
```
원래는 다른 버전으로 넘어가야하나, 다른 버전이 설치되어 있지 않으므로 삭제가 안됨   
deactive 한 다음에 지우면 지워진다.

### nvm 지우기
```
nvm deactivate
nvm unload
```
.bashrc 파일에 아래 코드를 지운다.
```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm
```


## node 버전 다르게 하기

노드 리스트 확인
```
nvm list
```
설치된 노드 버전 정보 등이 표시된다. 


버전별로 설치하기   
```
nvm install 14
nvm install 17
```
각 버전이 설치 된다.


사용하려는 버전을 선택해준다. 
```
nvm use 14
nvm use 17
```

> 아마도 default로 선택된 
예를 들어 `default -> 17 (-> v17.9.1)` 되어 있는 노드 버전을 디폴트로 사용하는 것 같고,   
특정 터미널에서 `nvm use` 등을 사용하면 해당 터미널에서는 해당 버전을 사용   
단 터미널을 다시 열면 디폴트 노드로 변경되는 듯 하다



원하는 버전을 선택해서 사용할 수가 있다.


javascript node 프로젝트 안에 (프로젝트의 상단 root)  
.nvmrc 파일을 만들고 단순히 
`v14.21.3` 이런식으로 버전만 적어준다.  

이후 nvm use 만 사용하면 해당 .nvmrc 파일에서 지정된 파일을 골라서 node를 선택해준다.

이후 npm install 원하는라이브러리

특히 라이브러리 등이 호환이 안될 경우에는 node 버전과 관련이 있음


