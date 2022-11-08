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

### docker-compose 확인
debian engine을 설치하면서 docker-compose 도 설치가 됨   
이게 업데이트가 되었는지 debian 만 그런지는 잘 모르겠음

하지만 PATH 변수에 등록이 안되어 있기 때문에 실행이 안됨.
```
bash: docker-compose: command not found
```

설치는 여기에 되어 있다. 일단 이동해준다
```
cd /usr/libexec/docker/cli-plugins
```

ls로 파일을 확인해보면 실행가능한 파일로 755로 되어있다. 바로 환경변수에 등록하자
```
export PATH=`pwd`:$PATH
```

다른 곳으로 이동한 후에 .. cd.. 혹은 cd  한 후에 `docker-compose` 입력하면 안내메세지가 잘 나온다면 성공

이제 bashrc파일에 넣어준다
```
vi ~/.bashrc
```

맨 아래줄에 아래 내용을 추가해준다
```
export PATH="$PATH:/usr/libexec/docker/cli-plugins"
```
저장을 해준다

> 이번에는 기존 PATH 뒤로 붙을 수 있게 뒤에 추가해줬다. 

이제 `source ~/.bashrc` 를 하거나 새로운 터미널 창을 열어준다

