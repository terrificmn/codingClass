참고 매뉴얼 https://docs.docker.com/engine/reference/builder/#workdir

특정디렉토리를 하나 만든다음에  
docker-compose.yml, Dockerfile 을 만들어서 내용 복사하면 준비 끝 (하나 파일로는 실행 못함)


### docker-compose.yml
```yml
version: '3'

services: 
  py:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 8501:8501
      - 8502:8502
    volumes:
      - ./app:/app
    environment: 
      - PYTHONUNBUFFERED=1
  
  # 터미널에 print() 화면에 볼 수 있게 해주기 PYTHONUNBUFFERED=1
  
```

### Dockerfile
```Dockerfile
FROM python:3.7

# 없으면 컨테이너안에 만든다
WORKDIR /app

# 최소 필요한 라이브러리 
RUN pip install streamlit \
    requests yfinance pystan \
     mysql-connector-python \
    tensorflow fbprophet \
    numpy scipy matplotlib \
    ipython scikit-learn==0.23.2 \
    pandas pillow jupyter seaborn joblib

# COPY requirements.txt ./requirements.txt
# RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8501
EXPOSE 8502
#CMD [ "python", "./app.py" ]
CMD streamlit run app.py
```


- 처음에는 최소 라이브러리만 설치했는데 apt-get으로 필요한 update 해보기     
이것도 해보았지만 fbprophet 달라지는 것은 없다 (legacy방법으로 설치완료됨 deprecation 워닝)
```
RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  libpng-dev \
  apt-utils \
  python-psycopg2 \
  python-dev \
    && rm -rf /var/lib/apt/lists/*
```

- 최소 필요한 라이브러리   
```
RUN pip3 install requests yfinance fbprophet \
    streamlit mysql-connector-python \
    tensorflow numpy scipy matplotlib \ 
    ipython scikit-learn==0.23.2 \ 
    pandas pillow jupyter seaborn joblib
```
참고: --no-cache-dir 아예 새로 빌드할 때 사용하는 옵션  
이미지가 있어도 새로 만듬, 그래서 필요없어서 뺌 (처음엔 몰랐음;;)


<br/>

___

위의 mysql-connector-python 추가


그리고 app 디렉토리를 하나 만들고  
그 안에 app.py 를 하나 만든다(테스트용)

내용은 아래 처럼
```py
import streamlit as st

def main():
    st.title('Hello World!')
    st.success('성공했을 때: 성공했습니다!')  

if __name__ == '__main__':  
    main() # main() 함수 호출
```


처음에 
```
sudo docker-compose build
```

그리고 성공하면 이렇게 메세지가 나오고  
```
Successfully built e2f30b1cf00a
Successfully tagged docker_streamlit_py:latest
```
그 다음은 
```
sudo docker-compose up

py_1  | 
py_1  |   You can now view your Streamlit app in your browser.
py_1  | 
py_1  |   Network URL: http://172.22.0.2:8501
py_1  |   External URL: http://175.117.241.188:8501
```
이렇게 나오면 성공  
로컬호스트로 들어가보면 된다

이제 백그라운드에서 작업하게 할려면  
```
sudo docker-compose up -d
```

실행중지하려면
```
sudo docker-compose down
```

이미지 삭제하려면 먼저 조회
```
docker ps -a
```

대충 이렇게 나옴
```
CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS                       
371b93ee4865   docker_streamlit_py   "/bin/sh -c 'streaml…"   3 minutes ago   Exited (137) 2 minutes ago   
```

그러면 CONTAINER ID 넘버를 적어서 삭제시킬 수 있다
```
sudo docker rm 371b
```

참고: 겹치는 게 없으면 앞자리만 적어도 됨 (우분투에서는 안될 수도 있음)


Dockerfile에서 WORKDIR 은 지정안해도 되는지 테스트 해보자  
-결과 yml 파일에서 volumn으로 app 과 app으로 지정했는데 그거랑은 상관없이  
Dockerfile에서 workdir 지정을 안했더니 app.py 실행은 못함;; 경로를 찾지 못하는 것 같음  
결론은 workdir은 계속 넣어주자  

------------

## --no-cache 사용
Dokerfile에서 파일 설치할 때 RUN 으로 명령어 옵션을 --no-cache 옵션을 넣으면   
--no-cache-dir 은 캐시 사용안하고 다운을 다시 받아버림,   
옵션을 빼고 docker-compose down만 안한 상태에서 뭔가 변경사항이 있을 때 다시 build하면 설치되있는것은 빼고 새로운것만 추가해 준다


---------------
화면에 터미널에서 print를 하면 출력이 안나옴  
그래서 streamlit을 할 때 브라우저에 출력해야하는데 디버그할때는 print()함수가 편해서   
이거를 가능하게 하려면     
docker-compose.yml 파일에  
``` 
environment: 
  - PYTHONUNBUFFERED=1
```
를 추가해주면 된다  
** 참고: 화면에서 \n (new line) 입력이 있을 때까지 버퍼에서 저장을 하고 있다는 데   
그거 관련된 옵션인 거 같다. 그래서 내보내기? flush를 하게 해주는 거 같은데 정확하지는 않다..;;


-------------------



추가 fbprophet 설치 시 설치가 안되는 에러  
일단 gcc+ 가 설치 되있어야 한다. centos는 gcc gcc-c++  
development Tools를 설치하면 된다  
$ sudo yum group install "Development Tools"

우분투는 
$ sudo apt-get install build-essential

그리고 python38-devel 이 필요 (현재 파이썬3.8 사용 중)  
3 이라고 하면 3.6버전이 깔림  
그래서  
$ sudo yum install python38-devel


매번 설치할 때 에러가 나는데, 해결을 못함  
```
ERROR: Command errored out with exit status 1:
   command: /usr/local/bin/python -u -c 'import sys, setuptools, tokenize; 
   ... 생략...
ERROR: Failed building wheel for fbprophet
```

근데 다행이도 DEPRECATION 워닝과 함께 설치는 됨
```
 DEPRECATION: fbprophet was installed using the legacy 'setup.py install' method, because a wheel could not be built for it. A possible replacement is to fix the wheel build issue reported above. You can find discussion regarding this at https://github.com/pypa/pip/issues/8368.
```

어쨋든 설치는 되고, fbprophet import해서 사용해보니 
사용이 된다;;

잡담:
이게 안되서 centos 날려먹음;;; gcc를 지우고 gcc-c++를 설치해야한다는 어느 구글링 답변에 
gcc를 지우는데 뭔가 의존성 패키지를 amd 어쩌구어쩌구를 같이 지운다는게 많이 나오는데 이상하다 싶었는데 일단 진행을 했는데, 
그 다음부터 화면이 안나옴 ㅠㅠ

gcc를 함부로 지우지 말자 

결국 os 다시 설치;;

