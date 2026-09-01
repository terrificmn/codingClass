일단 streamlit을 계속 실행이 되게 해줘야하는데  
터미널을 종료하면 세션 종료에 의해서 streamlit run 실행을 했던 것도 종료가 되어서   
더 이상 브라우저에서 접속을 할 수가 없다.

이럴 때는 백그라운드에서 작업이 되게 해줘야하는데 
간단하게 & 기호만 붙여주면 된다
```shell
streamlit run app.py &
```


하지만 재부팅을 하게 된다면 어떻게 될까? 역시 자동실행이 되지 않으므로 서버가 다시   
재부팅이 되어도 어플리케이션은 작동을 하지 않게 된다.

이럴 때는   
rc.local 파일에 쉡 스크립트로 작성을 해주면 된다. /etc/rc.local 
```shell
$sudo vi /etc/rc.local
```

파일을 열어준 후에 
```shell
#!/bin/bash
cd /application/myapp
nohup streamlit run app.py &
exit 0
```
저장을 하고 빠져 나온다. ESC를 누르고 편집모드에서 빠져나와서 : 를 누른 후에 wq 엔터

이제 rc.local 파일이 실행가능한 파일이어야해서 실행이 가능하게 권한을 조정한다
```
$sudo chmod +x /etc/rc.local
```

이제 재부팅시에 자동 실행이 될 것이다. 

## centOS 8 경우에는 ...
/etc/rc.d/rc.local 파일안에 등록해주면 된다.
역시 실행가능하게 해줄 것!

> 예전 기록이라 테스트가 정확히 되었는지 모르겠다. centOS8 이면.. 꽤 지났는데..  
Rocky Linux 에서 안된다면 우분투의 /etc/rc.local 및 rc-local 서비스 등록하는 것을 참고하자


# 방법 2
다른 방법은 /etc/init.d 디렉토리 안에 파일을 넣어주는 것이다.   
이것도 비슷한 방법인데, 이 디렉토리 안에 있는 시스템이 시작될 때 실행하게 된다. 

먼저 파일을 만든다 
```shell
$sudo vi /etc/init.d/streamlit_startup.sh
```

그리고 위에 내용 처럼 쉘 스크립트를 써 준다. 그리고 저장 후 빠져나온 후에   
이것 역시 실행이 가능하게 권한을 수정해 준다. 
```shell
#!/bin/bash
cd $HOME/application/myapp
sudo streamlit run app.py &
exit 0
```

```shell
$cd /etc/init.d
$sudo chmod +x streamlit_startup.sh
```

# 먼저 실행을 해보자
재부팅을 하기전에 실행이 되는지 확인은 (해당 경로로 이동을 하자)
```shell
$sudo sh streamlit_startup.sh
```
오류가 안나면 굿!

<br>

# 도커를 사용하는 경우에는 ..
먼저 systemctl로 enable 를 먼저 해준다
```shell
$sysctemctl enable docker
```

그리고 위의 경우와 마찬가지로 방법1, 방법2를 이용해서 쉘스크립트를 작성해주는데    
내용은 아래 처럼 해준다

```shell
#!/bin/bash
cd $HOME/application/myapp && sudo docker-compose up -d
exit 0
```

위에 처럼 해주면 된다.


# anaconda를 사용하는 경우
아나콘다 conda init을 활용한다 .   
홈 디렉토리의 .bashrc 파일을 열어보면 쉘스크립트가 들어 있다 .   
이부분을 카피해준다.

준비해야할 부분은 conda init 쉘스크립트와   
스트림릿이 설치되어 있는 경로가 필요하다
find ~ -name streamlit
파일 찾기
/home/ubuntu/.conda/envs/streamlit/bin/streamlit 에 있다고 찾아준다 


마찬가지로 
/etc/init.d/ 디렉토리에 쉡 스크립트를 만들어 준다 


아래는 내용...
그리고 콘다 액티베이트 환경id 를 해주고






그리고
