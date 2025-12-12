# /var/cache 지우기

/var/cache/PackageKit/42 또는 43 에 cached data가 들어 있는데  
용량 때문이라면 지워도 무방하다. 

> 용량이 아쉬울 때는 어쩔 수 없다.

직접 지우는 것 보다는 아래 커맨드 사용 하자

```
sudo pkcon refresh force -c -1
```
