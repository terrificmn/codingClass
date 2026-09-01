# 파이썬 설치 
소스코드 이용해서 파이썬 설치 

## pre빌드 되어 있는 파이썬 설치
yum 으로 python 설치하기는 쉬움
```
  $sudo yum install python3
```
설치 후 버전 확인
```
  $python3 --version
```

## 소스파일을 받아서 컴파일을 할 경우
install python on linux CentOs8 (최신버전 source파일로 받아서 설치하기)   

일단 dependencies를 해결해 주기 위해서 필요한 것들을 미리 update 및 설치   
아래 것들이 거의 다 필요   
참고: 일부러 3번째꺼 설치 안했더니 마지막 make 할때 error남   

```
  $sudo yum -y update
  $sudo yum -y groupinstall "Development Tools"
  $sudo yum -y install openssl-devel bzip2-devel libffi-devel
```

참고: 라즈베리파이에 필요한 패키지들
```
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```

python 사이트에서 최신 버전 다운로드 (tar 압축파일로 받으면 됨)   
다운로드 디렉토리에서 압축 풀기   
```
  $tar -xvf Python-파일명.tar
```
압축풀어진 디렉토리로 이동
```
  $cd Python-파일명
```

설정 스크립트를 실행해서 인스톨 관련 셋업을 한다

```
$./configure --enable-optimizations
```
그 다음 (시간 좀 걸림) 위의 작업이 완료 되면  
```  
$sudo make altinstall 
```
(시간 더 걸림.. 만약 에러가 나거나 하면 해당 에러 메세지로 구글링!)

아래와 같이 나오면 설치 성공이라고 함
```
... 생략
Collecting setuptools
Collecting pip
Installing collected packages: setuptools, pip
Successfully installed pip-19.2.3 setuptools-41.2.0
```
요렇게 나오면 설치 성공!!

설치 했으니 버전확인, 참고로 버전 3.9를 설치함
```
  $python3.9 --version
```

pip 버전도 확인  (pip 이 무엇인고? 모름;;)
```
  $pip3.9 --version
```

**참고 pip은 다른프로그램 설치할 수 있게 해주는 관리 프로그램 같은 것?   
예를 들어 mysql 같은 것들도 설치할 수 있게 해주는 것


make 한 후 이렇게 나옴 (추후 알아봐야할 듯)
  WARNING: The script easy_install-3.9 is installed in '/usr/local/bin' which is not on PATH.   
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.   
  WARNING: The script pip3.9 is installed in '/usr/local/bin' which is not on PATH.   
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.    

alias 만들어 주기    
리다이렉트로 넣어주기 또는 vi로 열어서 넣어준다    
```
echo "alias python=/usr/local/bin/python3.8" >> ~/.bashrc
```