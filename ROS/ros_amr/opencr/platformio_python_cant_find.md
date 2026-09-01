# platformio가 갑자기 안됨
파이썬을 못 찾는다.. 

잘 되던 platformIO 가 갑자기 먹통   

셋팅에서 "platformio-ide.useBuiltinPython": true 추가를 해도 소용 없음   

결론은 python3-venv 가 필요하다. 가상환경을 만들어줘야 하는 것 같다. (platforio 내부적으로..)  

근데   
python3-venv 를 설치를 해줘야 하는데 의존성에 달려있는 python3.8-venv 버전이 맞지가 않아서 설치가 안된다  

원래는 
```
sudo apt install python3-venv
```
정도만 해주면 되는데, 이렇게 설치가 되면 바로 넘어가면 된다.  
하지만 의존성 문제가 발생하는 경우에는.. 조금 복잡해진다. 

```
python3.8-venv : Depends: python3.8 (= 3.8.2-1ubuntu1) but 3.8.10-0ubuntu1~20.04.7 is to be installed

python3-venv : Depends: python3.8-venv (>= 3.8.2-1~) but it is not going to be installed
```

위 처럼 python3-venv 를 설치하기 위해서 python3.8-venv 가 필요한데   
이 python3.8-venv 에서 python3.8 버전을 3.8.2-1ubuntu1 을 요구하고 있지만  

이미 파이썬 버전은 3.8.10 버전 (우분투20.04 버전) 으로 설치가 되어 있어서 의존성 문제로 설치가 안된다   

그래서 /etc/apt/source.list 에 있는 카테고리를 조금 변경 해준다   
> 리파지토리를 통해서 다운을 받을 때 어디에서 받을 수 있을 지 추가 변경 가능. 
예: main 은 Canonical이 서포트 한느 open-source software  등..

> security provides security fixes. updates additionally provides fixes for serious bugs.   
backports provides new versions of (some) packages. 


```
sudo vi /etc/apt/source.list
```
파일을 열어서 `focal`을 변경  `focal-security` 로 변경

내용이 이런식이 된다 
```
deb http://us.archive.ubuntu.com/ubuntu/ focal-security main universe restricted multiverse
```

이제 저장을 하고 나와서 
```
sudo apt update
```
해준 후에 이제는 의존성 문제 없이 설치가 된다 

```
sudo apt install python3.8-venv
```
를 설치해준다 (python3-venv 말고 3.8로 해준다)

이제 vscode를 열고 platformio를 선택해주면 platformio 코어를 잘 설치해준다   

> ros2 에서는 `python3-venv` 만 해줘도 된다.

## 이를 해결 하기 위해 (실패)
```
python3 -m pip install virtualenv
```
설치는 잘 되지만, venv 와는 다른 모듈인지(?) platformio 에서 인식을 못함

플랫폼아이오가 가상환경을 만들고 실행이 되는 것이라고 한다  
그래서 /usr/bin/python3, /usr/bin/python3.8 을 python 주소로 적어줘도 작동을 하지 못하고 인식 실패



___

파이썬 3.10 버전 및 설치하고 따로 python3.10-venv 도 설치를 했지만 파이썬을 찾지를 못 함   

```
python3.10 -m venv penv 
```
처럼 가상 환경을 만들고 vscode를 열어도 결국은 에러 발생하면서 안됨   

