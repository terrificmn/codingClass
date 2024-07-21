# nodejs nvm으로 설치하기

호환성 문제로 node js를 맞춰야 하는 경우  
```
The engine "node" is incompatible with this module. Expected version "8 || 10 || 12 || 14 || 16 || 17". Got "20.12.2"
```

이런식으로 에러가 발생할 수 있다. 

현재 2024년 7월 기준 fedora 에서 dnf로 설치를 하면 20버전이 설치 되는 듯 하다.

nodejs에서 Download페이지에서 nvm 으로 편하게 설치할 수 있다.


# installs nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# download and install Node.js (you may need to restart the terminal)
nvm install 17


# verifies the right Node.js version is in the environment
node -v # should print `v17.9.1`

# verifies the right npm version is in the environment
npm -v # should print `8.11.0`


버전 확인 하기


nodejs 셋팅npm트러블슈팅.md 에서 사용한 방법으로도 테스트 해보기 

