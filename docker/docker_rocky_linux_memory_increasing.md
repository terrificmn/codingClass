Rocky Linux 9으로 설치를 한 이후로 docker 에서 roscore 나 roslaunch 를 실행시키면  
메모리가 발생하는 문제 

메모리가 순식간에 다 차버려서 아무것도 못하는상태;;
그나마 roscore는 10기가 정도 사용하고, roslaunch는 + 10기가 해서 20기가를 넘어가버린다.

해결하기 위해, docker 버전도 낮춰도 보고, 악성코드 검사도 해보고  
결국은 리눅스를 다시 설치까지 했는데 문제 발생  

### 해결
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
이제 램은 한 100mb 정도 올라가는 것 같다  

YES!!


### cpu 
nofile 제한을 수정해주면 된다는 것이고 unlimit 설정을 안 해놓으면 cpu, ram을 계속 사용하게 되는 듯 하다  

cpu가 100%
사용한다는 사람도 있었는데, 내 경우는 ros 컨테이너를 사용하면 rosout으로 log파일관련해서 계속 프로세스가 사용되면서  램 사용량이 올라갔다. CPU는 별 영향이 없었지만 1초내로 10기가 이상을 사용하는 현상   
정작 log파일은 1k도 안 되었는데 말이다  


[rocky linux 9 docker cpu memory 문제](https://community.netdata.cloud/t/current-issues-under-rocky-9-and-docker/3667/4)

아 감사하다. 한 2~3일 우울했었는데ㅠㅠ Oh thank you! 진짜 God bless you다~ ㅋㅋ
