# nvidia 
우분투에서 nivia 로 설치를 할 때 
ubuntu-nvidia devices 로 검색  후 설치를 할 수가 있는데   

만약 업데이트 된 드라이버를 설치를 할 경우에는 직접 nividia 에서 직접 리눅스 버전으로 다운을 받은 후 설치를 하게 되는데  

이때 ubuntu-nvidia로  먼저 설치가 되어 있다면 지워 준다음에 하는 것이 좋다. 그래야지 업데이트된 드라이버가 잘 작동한다. 

예
```
sudo apt remove nvidia-driver-535
```

이후 다운 받은 파일을 chmod +x 로 실행 권한을 부여 한 후에 
보통 `NVIDIA-Linux-x86_64-570.124.04.run` 파일 이름 처럼 생겼고  
sudo 로 실행을 해서 설치를 하면 된다. 

그러면 nvidia proprietary 또는 open 형식으로 선택하게 되는데 이때  nvidia proprietary 를 선택해주면 된다. 

> 반대로 위의  ubuntu-nvidia로  설치할 경우에는 recommended 로 되는 open 버전을 설치해준다.

실제로 잘 작동하는지는 

`nvidia-smi` 명령어로 확인할 수가 있다.

또는 MissionCenter 프로그램 추천 ( cpu, gpu, ram usage monitoring program)

