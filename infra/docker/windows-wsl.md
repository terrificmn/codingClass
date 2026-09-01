# window wsl 설치
docker를 윈도우에서 사용하려면 일단 windows 하위 시스템으로 linux를 가능하게 해줘야하는데   
powershell을 관리자 권한으로 실행하면 설치를 해준다 

```
wsl --list --online
```
를 하면 distro를 고를 수 있다   

```
wsl --install Ubuntu-20.04
```

또는 기본 ubuntu로 설치
```
wsl --install
```

기본 디스트리뷰션은 ubuntu 임, 

마지막으로 Ubuntu가 설치되었다고 하면 성공. 재부팅 한다 

## windows 용 docker는  
[windows-docker install 여기에서 다운로드](https://docs.docker.com/desktop/install/windows-install/)

설치가 다 되면 로그아웃을 해주게 된다  


## trouble shooting
```
WslRegisterDistribution failed with error: 0x800700e1
```

wsl --install을 할 때 계속 실패해서 실행도 안되고 docker desktop도 실행이 안된다면  
바이러스 프로그램을 의심해보자  

윈도우 백신 프로그램에서 계속 프로세서를 격리(?)시키고 있었다.   
일단 백신을 사용안하도록 했더니 docker desktop 및 wsl-install이 잘 된다  

