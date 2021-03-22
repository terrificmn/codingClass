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
    environment: 
      - PYTHONUNBUFFERED=1
  
  # 터미널에 print() 화면에 볼 수 있게 해주기 PYTHONUNBUFFERED=1
  
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

# 최소 필요한 라이브러리 
RUN pip3 install requests yfinance fbprophet \
    streamlit mysql-connector-python \
    tensorflow numpy scipy matplotlib \ 
    ipython scikit-learn==0.23.2 \ 
    pandas pillow jupyter seaborn joblib


# 참고: --no-cache-dir 아예 새로 빌드할 때 사용하는 옵션
# 이미지가 있어도 새로 만듬, 그래서 필요없어서 뺌 (처음엔 몰랐음;;)

# COPY requirements.txt ./requirements.txt
# RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8501
CMD streamlit run app.py
-----------------------------------------------

<br/>

## 학교버전 윈도우 도커 데스크탑 버전
___

FROM python:3.7

# 없으면 컨테이너안에 만든다
WORKDIR /app

# 최소 필요한 라이브러리 
RUN pip install requests yfinance fbprophet 
RUN pip install streamlit mysql-connector-python
RUN pip install tensorflow 
RUN pip install numpy scipy matplotlib 
RUN pip install ipython scikit-learn==0.23.2
RUN pip install pandas pillow 
RUN pip install jupyter seaborn joblib


# 인터넷이 느려서 (학교;;) 
# 라이브러리 설치하는 것도 (학교에서는 매우느림)
# 하나씩 라이브러리를 RUN으로 install 했는데 다음으로 넘어가는 것은 확인, 결론 엄청느림;;
# 일부로 RUN 한줄씩 적은 이유는 그나마 넘어가는게 보여서;;
# 이유를 모르겠다;; 윈도우 데스크톱은 더 느린거 같음;;;
# 암튼 몇백초가 걸려도 깔리고는 있음에 주의 
# COPY requirements.txt ./requirements.txt
# RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 8501
CMD streamlit run app.py
___

<br/>


참고 
 => [ 3/10] RUN pip install requests yfinance fbprophet                  425.4s                                          => [ 4/10] RUN pip install streamlit mysql-connector-python             674.4s                                          => [ 5/10] RUN pip install tensorflow                                  3525.2s                                          => [ 6/10] RUN pip install numpy scipy matplotlib                       106.9s                                          => [ 7/10] RUN pip install ipython scikit-learn==0.23.2                  53.1s                                          => [ 8/10] RUN pip install pandas pillow                                  1.5s                                          => [ 9/10] RUN pip install jupyter seaborn joblib                         5.9s 

걸린시간;;; 학교에서는 너무 느림;;



___



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


Dockerfile에서 WORKDIR 은 지정안해도 되는지 테스트 해보자
-결과 yml 파일에서 volumn으로 app 과 app으로 지정했는데 그거랑은 상관없이
Dockerfile에서 workdir 지정을 안했더니 app.py 실행은 못함;; 경로를 찾지 못하는 것 같음
결론은 workdir은 계속 넣어주자

------------

다음은 모듈 추가될때 매번 build를 하는데 있는 패키지를 계속 다시 다운받아야 하는지 검색해보자
Dokerfile에서 파일 설치할 때 RUN 으로 명령어 옵션을 --no-cache 옵션을 넣으면 
처음부터 build할때 캐시를 안 사용한다는 옵션이어서 한번 뭐가 업데이트 할 떄 --no-cache를 빼고 해봐야겠음

---------------
화면에 터미널에서 print를 하면 출력이 안나옴
그래서 streamlit을 할 때 브라우저에 출력해야하는데 디버그할때는 print()함수가 편해서 
이거를 가능하게 하려면 
docker-compose.yml 파일에 
environment: 
  - PYTHONUNBUFFERED=1
를 추가해주면 된다
** 참고: 화면에서 \n (new line) 입력이 있을 때까지 버퍼에서 저장을 하고 있다는 데 
그거 관련된 옵션인 거 같다. 그래서 내보내기? flush를 하게 해주는 거 같은데 정확하지는 않다..;;


vscode등에서 터미널을 열고 거기에서 docker-compose up 을 했다면 vscode의 터미널에 볼 수도 있겠지만
그냥 터미널에서 실행하면 그 터미널에서만 볼 수 있고 detache?  -d 옵션을 넣어주면 볼 수가 없다
(백그라운드 실행)

-------------------




