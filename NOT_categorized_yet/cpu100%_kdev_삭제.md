# malware "kdevtmpfsi" 확인하기
docker와 laravel의 취약점을 통해서 악성코드가 실행됨;;   

CPU를 100% 사용하게 되는 악성코드이다 

새로 시작한 VPS로 서버 셋팅을 하고 테스트 중인데 갑자기 안내 메일 안내가 와서 알게되었다~

처음에는 재부팅을 시켰는데~ log를 보니~ ssh로 접속하려는 흔적이 엄청 많았다~
그래서 해킹인가 했는데~ 접속이 성공한적은 없었는데~ 그래서 root 로 ssh 접속을 못하게 하는 조치만 했는데  
보니 또 100% 사용을 하고 있다

ssh에 접속을 시도해서  `top`  명령어 실행

아직은 잠잠하다.. docker의 취약점으로 침투가 된 것이라고 한다


## 로그 확인하기

`top` 과 `who` 명령어로 어떤 프로세스가, 누가 접속했는지 알 수 있다





`cat /etc/crontab` 으로 확인하기
다행히 등록되어 있는 것은 없다

/tmp 디렉토리 확인하기. 이상한게 많이 만들어져 있거나 확인

root로 실행된 crontab이 있는지 확인
```
sudo crontab -u root -l
```
다행히 `no crontab for root` 이라고 나오지만 만약 있다면 아래 명령어로 제거할 수 있다

```
sudo crontab -u root -r
```


> 우분투 로그인 로그 보기 
/var/log/auth.log ubuntu 경우   
centos 쪽은 /var/log/secure

그래서
```
sudo cat /var/log/secure
```

마지막 메세지 보기
```
sudo tail -f -n 100 /var/log/secure | grep sshd
```

```
sudo cat /var/log/secure | grep 'session opened'
```

나 외에는 로그인이 없는 듯 하다


일단 감염된 파일을 찾아보자
```
sudo find / -name kdevtmpfsi
```


```
/var/lib/docker/overlay2/fb183971cc4d9edea27fd58236ebdbc5bc74b297e86b47175fd407088729d489/diff/tmp/kdevtmpfsi
```



이런 드러운 놈들
```
Last login: Fri May 27 09:09:44 UTC 2022 from 59.17.172.78 on pts/0
Last failed login: Mon May 30 09:19:11 UTC 2022 on pts/0
There were 1013 failed login attempts since the last successful login.
```

삭제하기

[root@172-104-72-222 overlay2]# find / -iname kdevtmpfsi* -exec rm -fv {} \;
removed '/var/lib/docker/overlay2/fb183971cc4d9edea27fd58236ebdbc5bc74b297e86b47175fd407088729d489/diff/tmp/kdevtmpfsi'

삭제하기2
[root@172-104-72-222 overlay2]# find / -iname kinsing* -exec rm -fv {} \;
removed '/var/lib/docker/overlay2/fb183971cc4d9edea27fd58236ebdbc5bc74b297e86b47175fd407088729d489/diff/tmp/kinsing'


파일을 만들고 읽기전용 파일로 만들어준다
```
touch /tmp/kdevtmpfsi && touch /tmp/kinsing
# echo "kdevtmpfsi is fine now" > /tmp/kdevtmpfsi
# echo "kinsing is fine now" > /tmp/kinsing
# chmod 0444 /tmp/kdevtmpfsi
# chmod 0444 /tmp/kinsing
```

확인해보면 
```
ls -l /tmp/kdevtmpfsi /tmp/kinsing 
-r--r--r--. 1 root root 19 May 30 09:26 /tmp/kdevtmpfsi
-r--r--r--. 1 root root 16 May 30 09:27 /tmp/kinsing
```

파일 만드는 것은 실패할 수도 있음. kdevtmpfsi 가 랜덤으로 이름을 만들기도 한다고 한다


라라벨 프로젝트 .env 파일의 APP_DEBUG를 false로 바꿔준다
```
APP_DEBUG=false
```

그리고 composer로 facade/ignition   ^2.5.1 이상으로 패키지를 업데이트  
```
composer update facade/ignition
```
이미 업데이트가 되어있다,


그리고 docker와 php-fpm을 사용하고 있다면.. 딱 내 경우
```
I've struggled with this miner for few days and in my case it was the php-fpm:9000 port exposed.
I guess it possible to inject some code remotly this way.

So if you use docker & php-fpm, do NOT run your container this way:

docker run -v /www:/var/www -p 9000:9000 php:7.4

Remove the port mapping: -p 9000:9000

Don't forget to re-build & restart your containers.
```

`docker-compose up`을 한 다음에 다른 터미널로 확인을 해보면

[linlb@172-104-72-222 docker-laravel-blog]$ docker-compose ps
NAME                COMMAND                  SERVICE             STATUS              PORTS
artisan             "/var/www/html/artis…"   artisan             exited (0)          
composer            "/docker-entrypoint.…"   composer            exited (0)          
mysql               "docker-entrypoint.s…"   mysql               running             0.0.0.0:3306->3306/tcp, :::3306->3306/tcp
nginx               "/docker-entrypoint.…"   web                 running             0.0.0.0:80->80/tcp, :::80->80/tcp
npm                 "npm"                    npm                 exited (1)          
php                 "docker-php-entrypoi…"   php                 running             0.0.0.0:9000->9000/tcp, :::9000->9000/tcp
phpmyadmin          "/docker-entrypoint.…"   phpmyadmin          running             0.0.0.0:8080->80/tcp, :::8080->80/tcp

9000:9000 맵핑을 없애주자
정 오픈할 일이 있다면 `127.0.0.1:9000:9000` 처럼 자신의 ip에게만 오픈해준다

```
docker-compose run --rm web /bin/bash
```

/var/log/ngink/access.log
/var/log/ngink/error.log
를 보려고 했지만 /var/log/ngink/access.log > /dev/stdout 
로 보내진(?)

docker logs 컨테이너이름
```
docker logs nginx
```
쳐보면 로그를 볼 수 있다

파일로 만들려면 리다이렉트
```
docker logs nginx > ~/nginx.log
```


깃허브로 docker관련 업데이트를 해서 commit을 했고 다시 pull 을 받자

바뀐 내용은 
일단 9000 맵핑을 일단 주석처리, (php-fpm 9000 포트 사용안함)
phpmyadmin도 포트번호를 바꿔서 (예 9532:80) 80이랑 매칭해줬다~ (이것도 로그를 보면 꽤 접속해온다)

그리고 .env 파일의 web_port도 무작위로 바꿔버렸다 (로컬에서 작업할 경우에만, 로컬에서 하니깐 접속을 안할 것 같은데 막 중국, 미국 이런데서 접속하는 로그가 있다. 물론 로그인은 실패했지만)

이제 build
```
error checking context: 'no permission to read from '/home/sgtocta/Workspace/docker-laravel-blog/mysqldata/aria_log.00000001''.
```
이런에러가 발생하면 compose- build 할 때 
권한을 다시 1000 uid로 해준다

```
sudo chown -R 1000:1000 /mysqldata
```

docker-compose build
docker-compose up

을 해준다

서버 마지막 재부팅






