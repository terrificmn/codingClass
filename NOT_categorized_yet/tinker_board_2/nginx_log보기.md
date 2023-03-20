# nginx error log
docker exec로 nginx 의 컨테이너에 접근해서 보려고 했으나 볼 수가 없다   
아마도 /dev/null 로 연결이 되어(?)있어서 그런거 같기도 하다   

그냥 docker logs {컨테이너이름} 명령어로 볼 수가 있다  

```
docker logs nginx
```


### error 
좀 더 연구가 필요.. 일단 이렇게 하라는데 안된다 ㅋㅋ 일단 위의 방식으로 사용한다

참고    
error 로그만 보려면
```
docker logs -f nginx 1>/dev/null
```

access 로그만 보려면
```
docker logs -f nginx 2>/dev/null
```