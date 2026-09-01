# public ip address
curl을 이용해서 public ip를 알아낼 수가 있는데, 좀 길어서, ipinfo 사이트를 이용하는게 편하다   
그래서 api를 이용해서 입력해주면 응답으로 자신의 사내망이 연결되어 있는 실제 public ip를 알아낼 수가 있다  

```
curl https://ipinfo.io/ip
```
> 실제 위의 웹사이트를 들어가도 됨.  

보통 router에 연결이 되어 있는 경우에는 computer는 public IP, 기존의 ifconfig 등으로 알기가 어렵다   
자신의 inet (IPV4) 주소만 private network만 알게 된다   

