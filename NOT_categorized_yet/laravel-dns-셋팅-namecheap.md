# DNS 셋팅
namecheap 을 이용한 DNS 설정 방법.  
웹 호스팅을 사용할 경우에는 웹 호스팅 업체의 nameserver 만 등록을 하는 방식

하지만 직접 ip를 등록할 수도 있다.  
namecheap 같은 경우에는 Advanced option 에서 ip를 직접 셋팅 해주면 됨  

A record 라는 형태로 입력 (IPv4)
예  
| Type | Host | Value | TTL |
|--  |-- | --|-- |  
| A |    @   |    203.0.113.45 |   Automatic |  

> Host 는 root domain 을 의미한다. (example.com 이라면 example.com 를 의미하는 듯 하다)  
Value 는 자신의 public ip를 넣어준다.  
TTL 보통 auto면 30 min - 1hr 

이후 laravel 블로그는 dev 버전으로 ssl 인증을 받아야 한다.  
**필수** 인증을 받은 후에 경우 prod 에 해당하는 config 파일에서 도메인 정보를 수정해줘야 한다.  

설정 후에 반영 되는 시점은 체감상 반나절은 걸린 듯 하다.  


## 방화벽
도커 사용할 경우에는 별다른 방화벽 설정이 필요없는 듯 하지만, 443 포트는 열어준다.  
```
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

