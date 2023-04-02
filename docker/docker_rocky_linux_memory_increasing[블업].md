# docker 메모리 문제 memory increasing problem 
Rocky Linux 9으로 설치를 한 이후로 docker 에서 roscore 나 roslaunch 를 실행시키면  
메모리가 순식간에 10G 이상을 사용하고, 결국은 최대로 메모리르 다 잡아 먹어서 거의 아무것도 할 수 없는 상태에   
빠지는 문제가 발생했다.  

그나마 roscore는 10기가 정도 사용하고, roslaunch는 + 10기가 해서 20기가를 넘어가버린다.

<img src=0>

[메모리가 치솟는 걸 볼 수 있다 ㅠㅠ]

이를 해결하기 위해, docker 버전도 낮춰도 보고, 악성코드 검사도 해보고   
결국은 리눅스를 다시 설치까지 했는데 문제 발생 했다.. 이런;;;

> 물론 ubuntu, debian buster 등에서는 문제가 없었다.  
> docker 최신 버전부터 다운그레이드가 가능한 지점까지에도 전혀 문제가 없었고,   
> Rocky Linux 8.5 버전에서도 문제가 없었던 것으로 봐서는 9.0 이상이 되면 생긴 문제 인 듯..   

<br/>

### 해결 방법
해결 방법은 unlimits 설정을 해줘야 한다고 한다   
먼저 /etc/docker 로 이동 후에 daemon.json을 만들어주고 아래처럼 입력 후 저장해 준다   
```
cd /etc/docker
sudo vi daemon.json
```
복사
```json
{
   "default-ulimits": {
    "nofile": {
      "Hard": 64000,
      "Name": "nofile",
      "Soft": 64000
    }
  }
}
```

: 후에 wq 저장 후 빠져나온 후에  

도커 재시작
```
sudo systemctl restart docker
```

<img src=1>

이제 새로 사용해보니 램은 한 100mb 정도 올라가는 것 같다 **YES!!**


<br/>

### cpu 
nofile 제한을 수정해주면 된다는 것이고 unlimit 설정을 안 해놓으면 cpu, ram을 계속 사용하게 되는 듯 하다  

찾아보니 cpu를 100% 사용한다는 사람도 있었는데,   
내 경우는 ros 컨테이너를 사용하면 rosout으로 log파일관련해서 계속 프로세스가 사용되면서 램 사용량이 올라갔다.   
CPU는 별 영향이 없었지만 1초내로 램을 10기가 이상을 사용하는 현상   
정작 log파일은 1k도 안 되었는데 말이다  

[rocky linux 9 docker cpu memory 문제](https://community.netdata.cloud/t/current-issues-under-rocky-9-and-docker/3667/4)

아 감사하다. 한 2~3일 우울했었는데ㅠㅠ Oh thank you! 진짜 God bless you다~ ㅋㅋ
