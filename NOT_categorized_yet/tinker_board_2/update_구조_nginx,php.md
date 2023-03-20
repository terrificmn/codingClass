# tinker board 2 - nginx , php 사용
- 기존 python3 웹 서버 대신에 nginx 로 교체
- server side 에는 php 사용

새롭게 업데이트 된 디렉토리 구조
```
docker-ros
├── docker_ws
│   └── src
│       ├── camera_pub_cpp
│       └── servo_ros
├── nginx_conf
└── web_src
    └── web_motor
```

기존 web_motor 패키지는 web_src 디렉토리로 이동 변경

각각 docker_ws에 있는 패키지, web_src의 패키지는 gitignore 리스트에 들어가 있으므로   
따로 챙겨야 함  (추후 깃 commt하기)

docker관련해서는 docker-ros 의 tinker-noetic 브랜치 참고

## nginx 의 config 
docker-compose 에서 volumn으로 nginx_conf 디렉토리의 default.conf 사용  

defualt.conf 에서 
```
root /var/www/html/web_motor;
```
root가 web_motor로 연결이 되어 있음. web_motor 패키지가 최상단으로 위치하게 됨

web_src 디렉토리가 컨테이너의 /var/www/html으로 연결됨, php, nginx에서 사용
```
./web_src:/var/www/html
```

> public으로 연결해도되지만, 라라벨은 public에 연결이 되어 있고, public에 index파일 위치 함   
하지만 public이 root가 된 상태에서 그 위의 경로로 이동하는지 잘 모름, 실패   
php의 header() 함수를 사용했지만, root의 위로 경로로 이동해서 보여주는 것은 실패   
(예.. public 상에서 상단의 /var/www/html 에 있는 web_motor 가 있다고 했을 때, 즉 public과 web_motor가 html 디렉토리에 같이 있는 경우 )   
어쨋든, root를 /var/www/html 까지만 해주면 그 이하의 어느 디렉토리가 있다고 해도 header()함수로 이동은 잘 됨   
하지만 하나의 웹 서비스만 할 것이므로 web_motor로 root를 지정함  -20Mar 2023


- web_src 경로를 container와 연결시키는 것은 nginx의 root 지정과는 별개로   
컨테이너 /var/www/html 경로로 연결해서 (아마 심링크 비슷할 듯 함) 사용

- ros는 docker_ws 도커 워크스페이스로 연결해서 패키지들 사용

