# vnc without ssh tunnel
vnc를 사용할 때 ssh tunnel을 이용해서 localhost (정확히는 127.0.0.1)로  
접속하려는 원격pc의 ip를 자신의 localhost으로 묶어서(통해서) 접속할 수 있게 하는 방식인데  

ssh 명령어가 좀 길다. 이게 참 그런게, 터미널을 좋아하는 사람들(나) 같은 경우에는 거부감이 없겠지만   
뭔가 터미널로 긴 명령어를 쳐야하므로 부담스럽다..

그래서 꼭 ssh tunnel 기법을 사용하지 않고 하는 방법을 정리해 본다.  

> 보안이 필요없다고 생각되는 경우에 사용이 될 수도 있을 듯 하다.    
만약 유선 랜선을 이용해서 다이렉트로 랜선끼리 연결을 시켜서 사용하는 경우(remote pc와 내 pc)   
보통 모니터가 없는 로봇등에서 이런식으로 사용할 수 있을 듯 하다.  

그래도 가능하면 ssh tunnel 명령어 *-localhost* 사용하는 것을 **권장** 

## how to
어땟든 보안없는 상태로 접속하고 싶은 경우에 사용할 수 있겠다.

vncserver 명령어로 시작을 할때 -localhost 옵션을 주는데  
이때 -localhost 의 기본 파라미터 값은 yes 로 설정이 되어 있다. no로 입력을 해줘야지 false가 된다.

즉 예를 들어
```
vncserver -localhost no -geometry 1024*768 -depth 24
```
이런식이다. 

> 만약 no 를 생략하게 되면 기본값인 yes가 되어, ssh 터널링을 해야만 접속을 할 수가 있다.   
참고로 geometry 등은 생략하고 사용할 수도 있다.   
예 `vncserver -localhost no`

어쨋든 이후 vncview로 접속할 때에는   
직접 접속하려는 원격 pc의 ip를 입력해서 접속하게 된다.

```
vncviewer 192.168.10.111:5901 
```
> ssh tunnel을 사용하면 localhost:5901 로 접속하게 되는데  
ssh tunnel없이 할 때에는 직접 remote ip를 입력해준다.

ssh tunnel을 사용 안하면 보안에는 허점이 생기는 것은 알겠는데..  
어쨋든 어떤 식으로 정확히 보안에 악영향을 미치는 지 정확히는 모르겠다.    
아마도 어디에서든 직접 다이렉트로 접속할 수 있게 되므로? vnc자체가 암호화가 안 되는 것이므로?   

그래서 편하게 ssh tunnel 이 없이도 vnc를 사용할 수 있는 방법이 있다는 것을 알게되었다.  

