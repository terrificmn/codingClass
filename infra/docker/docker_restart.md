# docker 컨테이너 자동 재실행
docker-compose 파일에 
```
    ros:
        container_name: ros
        ...생략
        restart: always 
    
    py:
        container_name: py
        ...생략
        restart: always
```

이렇게 설정해주면 컨테이너 실행이 안되거나 할 때 무조건 다시 재실행을 하는데   
실패해도 계속 재실행하게 된다  

## 컴퓨터 reboot 
startup 관련 sh 스크립트를 만들어서... 업데이트하기

컴퓨터 reboot를 하더라도 위의 policy를 적용했다면 자동으로 도커를 백그라운드에 실행한다   

물론 docker를 enable 시켜줘야 한다  
```

```

그리고 테스트는 못해봤지만 -d 모드로 수행
```
```
