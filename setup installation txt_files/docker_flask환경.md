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

