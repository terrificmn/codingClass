# tinker board 2 에 docker 설치

팅커보드에 Debian Buster 10 버전이 설치되어 있어서 호환이 된다.  
다행히 Docker Engine은 x86_64, amd64, armhf, arm64 architechtures 와 호환이 된다고 한다

설치방법은 몇개가 있으나 그 중에 apt를 이용해서 설치를 함

### repository 셋업
apt 업데이트를 통해 https로 통해 apt 사용할 수 있게 함
```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

official GPG key등록
```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

리파지토리 셋업
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```


### docker engine 인스톨
한번 더 package index를 update
```
sudo apt-get update
```

최신 버전 설치 (docker-compose  까지 설치인데 아직 확인은 못해봄)
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```


### 버전 확인
```
docker --version
```

