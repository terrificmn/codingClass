FROM python:3.7

# 없으면 컨테이너안에 만든다
WORKDIR /src
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=development

# 환경변수 설정 (기본파일로 설정)
# 127.0.0.1 로 하면 웹브라우저에서 실행이 안됨
# windows에서는 됨;;

# RUN pip install flask flask-restful mysql-connector-python \
#                 psycopg2-binary passlib email-validator \
#                 Flask-JWT-Extended
# above it works well!

COPY requirements.txt ./requirements.txt 
RUN pip3 install -r requirements.txt

# # 파일들을 복사 (requirements에 있는 파일들)
COPY . .  

EXPOSE 5000
CMD ["flask", "run"]