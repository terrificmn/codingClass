## docker 사용 시 포트 매칭
일단 docker container 안에서 파이썬 http.server를 가동시키면   
작동이 제대로 되지 않는다. 그래서 localhost:8000으로 브라우저에 입력해도 되지 않는다   

열려있는 아이피 및 포트가 나오는데 전혀 나오지를 않는다.  

왜 안되는 것일까? 기존에 따로 python web 서버를 따로 컨테이너를 만든 것은 아니고   

ros용 컨테이너에서 직접 python http.server 만 실행시킨 것인데   
(컨테이너를 따로 만들려다가 조금 귀찮아져서;;)

이유는 간단했다. 바로 docker의 port를 매칭을 안해줘서 그렇다  
docker-compose.yaml 파일의 컨테이너의 구성파일에 ports 부분을 추가해준다음에  
```
services:

	ros:
	container_name: ros
	build:
		context: . 
		dockerfile: Dockerfile
	
	... 생략...
	ports:
	- "11311:11311"
	- "8000:8000
```

host 컴의 8000과 도커 컨테이너의 8000으로 해주면 된다 

> 저장 후 (요새는 다시 docker-compose up) 으로 실행만 다시 시켜줘도 바로 적용되는 듯 하다    
docker-compose build 안해도 됨   

이제  컨테이너에서 실행을 시키고 (docker exec -it 컨테이너이름 bash)  로 들어가서 직접 실행  

해당 디렉토리로 이동 한 후 `python3 -m http.server`

이제 다시 host 컴퓨에서 netstat으로 검색해보면 
```
netstat -tnlp
```

```
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      9497/python3        
```

요렇게 잘 나오는 것을 확인할 수 있다  

웹브라우저에서도 잘 실행이 된다  

**추가로 rosbridge 기본 포트인 9090 추가해 주자**

> 자동으로 웹 서버를 켜려면 컨테이너로 구성하는 것이 나을 지도 모르겠다    
> 추후 작업을 해봐야겠음   

