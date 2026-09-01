도커 이미지 받기
```
$ docker pull ubuntu:18.04
```
우분투 18.04를 다운 받음  
여기에서 ubuntu만 하면 최신버전을 받게 된다. 또는 ubuntu:latest

```
$ docker image ls
```
어떤 설치된 이미지 파일을 확인할 수 있다

이게 중요한 것이 컨테이너와는 별개로 image도 다운을 받는데..  
컨테이너는 삭제해도 image는 남아 있다...   
예를 들어 위의 명령어를 실행하면 이런식으로 나온다..  

```
REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
docker-tfod_web   latest    509548b54cf2   16 minutes ago   7.1GB
<none>            <none>    2187aad96410   29 minutes ago   3.75GB
<none>            <none>    3c620b1adbea   56 minutes ago   3.75GB
<none>            <none>    d819c9d33791   11 days ago      8.11GB
<none>            <none>    00c681f59ab0   11 days ago      8.11GB
<none>            <none>    3a2bcf168023   11 days ago      8.11GB
ubuntu            18.04     4eb8f7c43909   2 weeks ago      63.1MB
python            3.8.8     b182085023c0   6 weeks ago      883MB
```
테스트 한다고 이것저것 build를 했는데 그때마다 image파일을 다운을 받았다   
그래서 필요없는 것은 삭제를 하자

지우기는 IMAGE ID를 입력해주면 된다. docker image rm 숫자id 이런식   
여기에서 id는 겹치지 않으면 다 안적어도 된다. 필요없는 우분투 이미지를 지워 봄
```
$ docker image rm 4eb8f7c
```
결과는
```
Untagged: ubuntu:18.04
Untagged: ubuntu@sha256:538529c9d229fb55f50e6746b119e899775205d62c0fc1b7e679b30d02ecb6e8
Deleted: sha256:4eb8f7c43909449dbad801c50d9dccc7dc86631e54f28b1a4b13575729065be8
Deleted: sha256:5683b8d625d1dfa13fd9bf36bd007876a10ba7b9d0159e5b751c2e555056b1a4
Deleted: sha256:e40721a5f7d83ef5475788aa771a9cc75312998fb206ba8c2cf4294f9594f46e
Deleted: sha256:5153e1acaabce0d87adbf4a717bdc5e26cf86d851330830589a6b2bf5ede30ee
```

df -h 로 확인한 결과.. 두둥!!   
먼저 before 
```
Filesystem           Size  Used Avail Use% Mounted on
/dev/mapper/cl-root   70G   34G   37G  49% /
```

그리고 after
```
Filesystem           Size  Used Avail Use% Mounted on
/dev/mapper/cl-root   70G   21G   50G  29% /
```

아 참고로.... python 3.8.8 이미지는 자식 이미지가 있어서 의존성 때문에 삭제가 안됨.. 그냥 나두자~

root 쓰고 있는 영역이 무려 13기가나 늘어났다.. 오~      
home 이 주 무대인 실 사용자한테는 전혀 체감이 없지만.. (home 디렉토리도 딱 제한이 있어서;;;)   
서버 쪽에서는 불필요한 이미지는 없는지 확인해 봐야겠다..

도커 명령어 실행하기 (bash 프로그램 열기)

```
$ docker run -it ubuntu:18.04 /bin/bash
```

```
$ dudo docker run -it ubuntu:18.04
```
여기까지만 해도 우분투 실행됨

-t 옵션이 터미널로 열 수 있는 방식으로 -i로 하면 계속 터미널에 열려있게 됨    
바로 /bin/bash 를 열어준다 

옵션 설명  
-i, --interactive   Keep STDIN open even if not attached   
-t, --tty           Allocate a pseudo-TTY     



## Dockerfile에서 명령어들

WORKDIR은 도커 컨테이너안에서 작업할 디렉토리를 지정해준다.. (cd가 포함되어 있다고 생각하면 될 듯..)   
만약 디렉토리가 없다면 만들어 준다. (로컬 호스트에서의 디렉토리와는 상관이 없음)   
(WORKDIR affects the working directory inside the container.)   

RUN 역시 컨테이너 안에서 작동하는 명령어. 뭔가를 실행하거나 할 수 있다.    
예를 들어서    
RUN (cd /tensorflow/models/research/ && protoc object_detection/protos/*.proto --python_out=.)   
컨테이너 안에서 cd로 /tensorflow/models/research/ 경로 변경을 한 다음에    
protoc 이라는 명령어를 실행한다.

차이점은 컨테이너에서 디렉토리가 없다면 먼저 만들어줘야하는데, RUN 명령어로 또 실행   
그리고나서 위의 명령어를 해야함   
즉, RUN mkdir -p /tensorflow/models/research   
이렇게 해 준 다음에 위의 코드를 써주면 실행이 되게 되는 것이고   

WORKDIR은 해당 디렉토리로 이동해서 해당 디렉토리를 현재 위치로 만드는 것, 없다면 만들어 준다는 것이 차이점이다


COPY 는 두개의 파라미터? 라고 생각하면 되는데 로컬 호스트 컴퓨터의 파일에서 도커 컨테이너로 복사시키게 되는 것   
예를 들어   
COPY ./requirements.txt /src

현재 로컬의 디렉토리에 있는 requirements.txt 파일을 도커 파일의 /src 경로로 복사시키되는 것이다.   

주로 이런식으로도 많이 사용   
COPY . .   
현재 디렉토리에 있는 내용을 도커로 복사시킴   


streamlit을 사용할 때에는 만약 실제 로컬에 실행할 수 있는 어플리케이션 파일이 src 디렉토리에 있다고 할 때    
/src/app.py <-----로컬에 있는 파일   

이제 도커 컨테이너에서 streamlit을 실행시켜야하는데 Dockerfile에서 RUN명령어로 실행하게 함   
예를 들어
```
FROM python:3.8.8
COPY requirements.txt ./requirements.txt 
RUN pip3.8 install -r requirements.txt
```
아 requirements.txt에 streamlit 및 라이브러리등 몇개가 들어있다.. 

이렇다고 하면    
파이썬 3.8 이미지를 가지고 와서 requirements.txt 에 있는 파일 컨테이너 안으로 복사   
그리고 pip으로 설치하게 되는데 streamlit 을 포함한 라이브러리등..   

그래서 이제 streamlit을 실행할 수가 있는데
```
CMD streamlit run app.py
```
이라고 했다면.. app.py을 못 찾아서 실행을 할 수가 없다고 한다.

그래서 
```
WORKDIR /src
CMD streamlit run app.py
```

라고 해주면 실행이 제대로 된다.   
WORKDIR은 컨테이너 안에서 실행을 하는 것인데, /src (<--- 이거는 도커 내부) 디렉토리가 없으니깐 만들어 줄 테고   
거기를 베이스로 workdir하게 되는 건데..    
그 다음에 CMD 명령어가 streamlit run  이 나오면 컨테이너의 streamlit을 실행하게 되고..    
그 뒤에가 좀 신기한게 /src (<---- 로컬 호스트의 디렉토리) 안에 있는 app.py를 실행을 시켜주게 된다.   

암튼.. 뭐 신기하네... 아니면 뭔가 잘못했는데 얻어 걸렸는지도 ㅋㅋ
