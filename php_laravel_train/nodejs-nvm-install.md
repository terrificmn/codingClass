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




## yarn 설치하기 (global)
```
npm install --location=global yarn
```

또는 `npm install -g yarn`
> 단, -g, --global 은 deprecated 되었다고 하나, 사용은 가능하다