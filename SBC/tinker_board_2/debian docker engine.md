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

설치를 하다가 실패할 수도 있으나, 다시 한번 설치를 시도하면 잘 설치가 됨


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

> 아래 내용은 참고만 하기! docker-compose 는 예전 버전이므로 아래 방법으로 하면 사용가능하나  
그럴 필요 없이 `docker compose` 로 사용하면 된다.(새로운 명령어 한칸 띄움)

**아래는 그냥 참고사항..**   
방법은 2가지가 있다.  
하나는 환경변수로 만들어 주는 것이고, 두 번째는 심볼릭 링크를 만들어 주는 것

1. 먼저 환경변수 등록하기. 설치는 여기에 되어 있다. 일단 이동해준다
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

2. 심볼릭 링크를 만들어주기
이 방법은 docker-compose 파일을 심볼릭 링크를 만들어서 사용할 수 있게 하는 것   

> 환경변수, 심볼릭 링크나 한 개만 수행하면 된다

```
sudo ln -s /usr/libexec/docker/cli-plugins/docker-compose  /usr/bin/
```

> 언제나 심볼릭 링크 걸때는 원본이랑 타겟이 헷갈린다. 원본(타겟) 실제링크만들위치

이렇게 하면 /usr/bin/docker-compose 로 심볼릭 링크가 만들어지고 실제 파일을 가리킨다

이제 어디에서나 실행을 하면 된다 


### 권한 설정
sudo 를 안 할 수 있게 설정
```
sudo usermod -aG docker $USER
newgrp docker
```


## Debian Buster 10 과 Debian Bullseye 11 의 docker

**기존 사용하던 Debian Buster 10** 에서는 docker가 전혀 문제가 없었는데  

Debian Bullseye 11이 나왔길래 OS를 업데이트를 했는데, 다 좋은데 docker가 안 된다. 

docker-ce 를 설치가 마무리 되서 docker service를 시작하려고 하면서 에러가 발생하고  
이후 `systemctl start docker` 를 하게 되면 오류 때문에 시작을 할 수가 없다.  

```
docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: failed (Result: exit-code) since Sat 2023-10-21 05:11:43 UTC; 47s ago
TriggeredBy: ?? docker.socket
       Docs: https://docs.docker.com
    Process: 2476 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.soc>
   Main PID: 2476 (code=exited, status=1/FAILURE)
        CPU: 387ms

Oct 21 05:11:43 linaro-alip systemd[1]: docker.service: Start request repeated too quickly.
Oct 21 05:11:43 linaro-alip systemd[1]: docker.service: Failed with result 'exit-code'.
Oct 21 05:11:43 linaro-alip systemd[1]: Failed to start Docker Application Container Engine.
Oct 21 05:12:06 linaro-alip systemd[1]: docker.service: Start request repeated too quickly.
Oct 21 05:12:06 linaro-alip systemd[1]: docker.service: Failed with result 'exit-code'.
Oct 21 05:12:06 linaro-alip systemd[1]: Failed to start Docker Application Container Engine.
```

뭐, 이후 한 두어 시간 문제를 찾아 볼려고 했는데, 버전을 낮춰보거나, 설정 관련 json 등.. 
인터넷에서 나온 조언들로 시도를 했지만 실패했다.  

> 그래서 그냥 Debian 10 버전으로 다시 돌아가게 되었다. 시간도 없고,  
싱글보드 컴퓨터에서 카메라 프로그램 실행되는 것 하는것인데, Debian 11를 쓸 이유가 없기 때문이다.  
다시 docker는 Debian 10 Buster에서 잘 된다.

