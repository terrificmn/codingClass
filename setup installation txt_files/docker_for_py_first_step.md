참고 매뉴얼 https://docs.docker.com/engine/reference/builder/#workdir

특정디렉토리를 하나 만든다음에
docker-compose.yml, Dockerfile 을 만들어서 내용 복사하면 준비 끝 (하나 파일로는 실행 못함)


docker-compose.yml

version: '3'

services: 
  py:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 8501:8501
    volumes:
      - ./app:/app
  
  # 아직 미 적용
  # mysql:
  # image: mariadb:latest
  # restart: unless-stopped
  # ports:
  #   - 3306:3306
  # environment:
  #   MYSQL_ROOT_PASSWORD: my-secret-pw 
  #   MYSQL_DATABASE: tutorial
  #   MYSQL_USER: tutorial
  #   MYSQL_PASSWORD: secret
  #   SERVICE_TAGS: dev 
  # volumes:
  #   - ./mysqldata:/var/lib/mysql


----------- Dockerfile
FROM python:3.7

# 없으면 컨테이너안에 만든다
WORKDIR /app

#COPY requirements.txt ./
# 최소 필요한 라이브러리 

RUN pip3 install --default-timeout=3000 --no-cache-dir \
    streamlit mysql-connector-python \
    tensorflow numpy scipy matplotlib \ 
    ipython scikit-learn==0.23.2 \ 
    pandas pillow jupyter seaborn joblib


# 인터넷이 느려서 (학교;;) 그래서 --default-timeout=3000 을 넉넉히 줌
# tensorflow를 설치하는데 300mb가 거기에서 에러가 나는 듯
# COPY requirements.txt ./requirements.txt
# RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8501
CMD streamlit run app.py
-----------------------------------------------

위의 mysql-connector-python 추가


그리고 app 디렉토리를 하나 만들고 
그 안에 app.py 를 하나 만든다(테스트용)

내용은 아래 처럼

import streamlit as st

def main():
    st.title('Hello World!')
    st.success('성공했을 때: 성공했습니다!')  

if __name__ == '__main__':  
    main() # main() 함수 호출


--------------------------------------------




처음에 
sudo docker-compose build

그리고 성공하면 이렇게 메세지가 나오고
Successfully built e2f30b1cf00a
Successfully tagged docker_streamlit_py:latest

그 다음은 
sudo docker-compose up

py_1  | 
py_1  |   You can now view your Streamlit app in your browser.
py_1  | 
py_1  |   Network URL: http://172.22.0.2:8501
py_1  |   External URL: http://175.117.241.188:8501

이렇게 나오면 성공 
로컬호스트로 들어가보면 된다

이제 백그라운드에서 작업하게 할려면
sudo docker-compose up -d

실행중지하려면
sudo docker-compose down

이미지 삭제하려면 먼저 조회
docker ps -a

대충 이렇게 나옴
CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS                       
371b93ee4865   docker_streamlit_py   "/bin/sh -c 'streaml…"   3 minutes ago   Exited (137) 2 minutes ago   

그러면 CONTAINER ID 넘버를 적어서 삭제시킬 수 있다
sudo docker rm 371b

* 참고: 겹치는 게 없으면 앞자리만 적어도 됨 (우분투에서는 안될 수도 있음)


해봐야 할것은 
yml의 파일의 volumes 을 지정해줬는데

Dockerfile에서 WORKDIR 은 지정안해도 되는지 테스트 해보자 (학교에서)

