# docker-compose.yml 파일
```yml
version: "3.9"

services: 
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - 5000:5000
    volumes:
      - ./app:/app
    environment:
      PYTHONUNBUFFERED: 1
      FLASK_ENV: development

```

environment: 부분을 Dockerfile의 ENV 환경변수에 직접 넣고 yml파일에서는 빼도 되는지는 테스트 해볼 것
결과: 가능하다.  

```Dockerfile
FROM python:3.7

# 없으면 컨테이너안에 만든다
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# 환경변수 설정 (기본파일로 설정)
# 127.0.0.1 로 하면 웹브라우저에서 실행이 안됨

RUN pip install flask flask-restful mysql-connector-python
# COPY requirements.txt ./requirements.txt  추후 requirements.txt파일로 사용할 경우
# RUN pip3 install -r requirements.txt
#COPY . .  # 파일들을 복사 (requirements에 있는 파일들)

EXPOSE 5000
CMD ["flask", "run"]

```



requirements.txt 파일에 필요한 라이브러리     

Dockerfile 파일에서 RUN으로 pip install을 실행하거나   
RUN으로 직접 pip install 을 실행하지 않고,   
COPY 명령어로 requirements.txt 파일을 복사 한 다음에 (주석해제)   
RUN으로 requirements.txt 파일을 이용해서 pip3 install한다   
```
flask
flask-restful
mysql-connector-python
psycopg2-binary
passlib
email-validator
```

