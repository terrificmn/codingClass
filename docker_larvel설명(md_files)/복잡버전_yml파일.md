## 특히 주의할 점은 UID를 변수화 했는데 이것은 .env 파일의 맨 마지막에 입력해준다. 아래처럼 추가해준다 (한줄) 
# UID=1000
## 최상단 디렉토리에 .env파일은 만들면됨 (라라벨 새로운 프로젝트를 시작하면 .env_sample 파일을 복사해서 사용) 
version: '3.5'

networks: 
  laravel:

services:
  php:
    build:
      context: .  
      args:
        uid: ${UID}  #같은 디렉토리에 .env 파일에 정의해준다 
      dockerfile: Dockerfile
    container_name: php 
    ports:
      - 8000:80
    environment:
      - APACHE_RUN_USER=#${UID}
      - APACHE_RUN_GROUP=#${UID}
    volumes:
      - ./src:/var/www/html/  
    networks: 
      - laravel

  db:
    image: mariadb 
    container_name: mariadb
    restart: unless-stopped  
    tty: true 
    ports: 
      - 4306:3306 
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw 
      MYSQL_DATABASE: app_db
      MYSQL_USER: db_user
      MYSQL_PASSWORD: db_user_pass
      SERVICE_TAGS: dev 
    volumes:
      - ./mysql:/var/lib/mysql 
    networks: 
      - laravel

  phpmyadmin:
    image: phpmyadmin
    container_name: pma
    links:
      - db   
    restart: always
    ports:
      - 8080:80
    environment:
      - PMA_ARBITRARY=1
      - PMA_HOST= db  # mariadb 컨테이너 이름 (db로 함)
      - PMA_PORT= 3306
    networks: 
      - laravel

