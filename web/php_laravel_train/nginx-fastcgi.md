# nginx
fastcgi_pass 와 proxy_pass

```
fastcgi_pass
    ↓
FastCGI
    ↓
PHP-FPM

VS  

proxy_pass
    ↓
HTTP
    ↓
another HTTP server
```


*fastgic_pass*  
```
Browser
    |
    | HTTP or HTTPS
    ▼
    nginx
    |
    | FastCGI
    ▼
    php container (docker)
    |
    | PHP-FPM : 9000
    ▼
    Laravel
```
이런식으로 사용된다. 


이 부분은 nginx conf 파일의 location 부분에서 확인할 수가 있음, 9000 port 를 사용
```
location ~ \.php$ {
    fastcgi_pass php:9000;
    ...
}
```

HTTPS 를 사용하더라도 같은 server {} 을 사용하고, (ssl_certificate 등이 추가 됨)   
nginx 가 TLS termination 을 해서 (TLS 를 끝냄)  
php:9000  PHP-FPM 으로 전달되게 된다.  

그래서  Laravel 에서는 https 여부를 확인할 필요가 없게 된다.  


*proxy_pass*  
다른 HTTP application server 로 연결해주는 역할을 한다.  

nginx
 |
 |
 Laravel : 8000

이럴 때 
proxy_pass http://larvel:8000; 을 사용한다고 한다.   
