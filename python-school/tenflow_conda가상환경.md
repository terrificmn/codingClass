# tensflow 아나콘다 가상환경 만들기
**참고**
아나콘다를 실행해서 파이썬 버전을 3.8 버전으로 설치를 하면서 
가상환경을 만들어 준다
```shell
$conda create -n vitrualtf python=3.8
```
- -n 옵션은 가상환경 이름이 된다.
- 이름은 하고싶은 걸로 아무거나 상관없다

파이썬은 3.8버전으로 했기 때문에 파이썬 3.8을 설치하면서 가상환경을 만들어 준다

<br>

___
이제 가상환경으로 들어가야한다. actviate 시킨다  
```shell
$conda activate vitrualtf
```

실행이 되면 터미널의 프롬포트 앞에 (base) 에서 (vitrualtf)라는 가상환경 이름으로 바뀐다  
예:
```
(vitrualtf)[Octa@localhost ~]$ 
```

이제 텐서플로우 버전 2.2를 pip을 이용해서 설치해준다
```shell
$pip install tensorflow==2.2.0
```

*참고* pip 버전이 pip3 버전별로 설치가 되어 있다면 버전을 확인해서 실 사용하는 pip으로 사용한다
```shell
$pip --version
$pip3 --version
```

tensorflow가 설치가 완료되었다면 잘 되었는지 확인  
파이썬을 실행해서 텐서플로우를 import해본다. 
```shell
$python3.8

Python 3.8.8 (default, Apr  9 2021, 10:26:29) 
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>>
>>> exit()
```
아무런 메세지가 안나와야지 설치가 잘 된 것임.   

<br>

# 텐서플로우 Git clone 하기
텐서플로우 공식 깃허브 사이트에 방문
[git.hub tensorflow](https://github.com/tensorflow/models)

원하는 작업 디렉토리를 만들어준다. 그리고 해당 디렉토리로 이동
```shell
$mkdir tensorflow
$cd tensorflow
```

그리고 해당 디렉토리에다가 git clone을 해준다. 위의 깃허브를 들어가서 깃 리파지터리 주소를 복사해온다

초록색 code 아이콘을 누르면 주소를 복사할 수 있다 

그리고 다시 터미널로 돌아와서 깃 클론을 해주면 오픈소스의 많은 내용들을 사용할 수 있다.
```shell
$git clone https://github.com/tensorflow/models.git
```

<br>

# Protocol Buffer 설치하기
dnf 나 yum 으로 다운받기
```shell
$sudo dnf install protobuf-compiler
```
패키지 매니저로 설치했다면 아래는 skip

<br>

zip파일로 받아서 설치하기 (수동)

https://github.com/protocolbuffers/protobuf/releases  
에서 리눅스x64 버전으로 다운받는다 

파일명 protoc-3.15.8-linux-x86_64.zip  

다운받은 zip파일의 압축을 풀어준다. 
```shell
$unzip protoc-3.15.8-linux-x86_64.zip -d protoc
```

이재 현재 디렉토리 내에서 protoc이라는 디렉토리가 생성되면서 압축이 해제됨  
이제 이 압축푼 디렉토리를 위에서 만든 tensorflow로 이동시켜준다.

```shell
$mv protoc/ ~/tensorflow/
```

이제 protoc (압축풀린 디렉토리)가 이동이 되었을 것이다. protoc/bin 에 보면   
protoc이라는 파일이 있는데 다른디렉토리에서도 사용할 수 있게 환경변수 $PATH에 등록을 시켜준다.

먼저 해당 bin 디렉토리까지 이동하거나 절대경로를 다 써준다
```shell
$cd ~/tensorflow/protoc/bin
$export PATH=$PATH:`pwd`

#또는
$export PATH=$PATH:"~/tensorflow/protoc/bin"
#또는
$export PATH="~/tensorflow/protoc/bin:$PATH"
```

환경변수는 재부팅을 하면 환경 변수값이 없어지기 때문에..  
계속 사용하려면 홈디렉토리에 .bashrc 에 추가해 준 후에 저장  
그리고 source .bashrc 를 해준다 

그다음 source 해주기
```shell
export PYTHONPATH="$PYTHONPATH:$HOME/Workspace/tensorflow/models/research:$HOME/Workspace/tensorflow/models/research/slim"
```
도커 사용시
```shell
export PYTHONPATH="$PYTHONPATH:$HOME/Workspace/docker-tfod/src/models/research:$HOME/Workspace/docker-tfod/src/models/research/slim"
```


이제 protoc 을 이용해서 컴파일하기

깃허브에서 클론 한 tensorflow/models 로 이동하자. 서브 디렉토리 research 까지 이동
```shell
$cd ~/tensorflow/models/research
```

```
$protoc object_detection/protos/*.proto --python_out=.
```


<br>

# COCO API 사용하기 (COCO dataset)
COCO is a large-scale object detection, segmentation, and captioning dataset. COCO has several features:

https://cocodataset.org/#home  
https://github.com/cocodataset/cocoapi  

먼저 cython설치를 해준다
```shell
$pip install cython
```

coco api 깃 허브를 clone 해준다
주소는 위의 사이트 주소에서 참고 한다  
현재 디렉토리 위치에서 만들어지므로 원하는 디렉토리로 이동한 후에 명령어를 실행  
```
$git clone https://github.com/cocodataset/cocoapi.git
```

cocoapi의 README를 보면 (깃허브 사이트)  
파이썬으로 사용할 때에는 coco/PythonAPI 로 이동한 후에 
make를 하라고 되어 있다 
```shell
$cd cocoapi/PythonAPI
$make 
```
원래 매뉴얼에는 make를 실행해야하는데 python을 못 찾는다. 그래서 직접 입력을 해준다 

이 부분에서 너무 많이 애를 먹어서;;
centOS 8에는 기본으로 파이썬3.6이 설치가 되어 있는데. 나는 따로 파이썬3.8을 설치를 했고  
아나콘다 가상환경에서도 파이썬3.8을 설치했다  
그래서 이부분에서 파이썬 3.8로 실행할 수 있게 해야한다. 이게 안되면 계속 꼬이고 설치가 잘 안된다.  

python 환경변수 설정 및 심볼릭 링크 수정을 참고하자!

실행은 아래처럼..

```shell
python3 setup.py install
```

(pycocotools를 설치는 안하고 했는데 잘 설치되었음)
만약 pycocotools 가 없다고 하면 설치해주기
```
$pip install pycocotools
```

# object detection Api 설치
다시 tensorflow/models/research 로 이동한다. (설치된 경로로 이동)

```shell
$cd ~/tensorflow/models/research
```

research의 하위 경로에 들어있는 setup.py파일을 현재 경로(research) 로 복사시킨다
```shell
$cp object_detection/packages/tf2/setup.py .
```

ls 를 해보면 현재 경로 (research)에 setup.py 가 설치되어 있음

현재 경로에서 pip install하기 . (점)이 있음에 주의
```shell
$python -m pip install .
```

테스트를 해보자
다시 research디렉토리에서 테스트. 탭으로 자동완성을 시켜서 하자
```shell
$python object_detection/builders/model_builder_tf2_test.py 
```
[      OK ]...  
[ RUN     ]...  
이런식으로 테스트가 진행이 된다.  

마지막으로 이렇게 나오면 잘 된것임~  
Ran 21 tests in 33.745s  
OK (skipped=1)

<br>


모델 다운로드 받기
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md


매뉴얼 참고
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/auto_examples/plot_object_detection_saved_model.html#download-the-model


<br>

<br>

<br>

추후 정리 예정
___




심볼릭 링크 /usr/bin/pyhothn3 -> /etc/alternatives/python3  
를 가리키고 있고 (이놈도 심볼릭링크다)   
다시 이 심볼릭링크 /etc/alternatives/python3 -> /usr/bin/python3.6   
(실제실행 파일을 가리키고 있음)

그래서 이 부분을 수정해주면 원래 소스 실행될 파일 파이썬3.8을 기존의 3.6으로의 연결을 끓고   
다시 연결해준다 
```
sudo ln -sf /usr/local/bin/python3.8 /etc/alternatives/python3
```

그리고 확인 
```
ls -li /etc/alternatives/python3*
```
68080898 lrwxrwxrwx. 1 root root 24 May  2 08:22 /etc/alternatives/python3 -> /usr/local/bin/python3.8  
녹색으로 잘 나오면 됨~ 빨간색이면 연결이 잘 안된거니 주의

이제 파이썬 python3 이라고 입력하면 3.8이 실행된다.

python이라고 치면   
```
bash: python: command not found...   
```
명령어가 없다고 한다..   
위에 처럼 python 심볼릭 링크를 만들어 주거나 

또는   
.bashrc 파일에 alias 를 설정해주면 된다.

(나중에 업데이트)






실패이력!!!! 

먼저 .bashrc 파일에 alias 라고 해서 python python3 으로 입력하게 되면  
모두 파이썬 3.8로 하게 되어 있는데..  
그래서 평상시 python 또는 python3 , python3.8 이렇게만 쳐주면   
3.8.8 버전이 뜨게 되고,   
오직 python3.6 이라고 해야지 3.6버전 인터프리터가 실행된다

하지만 python setpu.py install 같이 설치할 때에는 이게 제대로 작동을 안한다   
계속 python 을 못찾게 된다.

어찌어찌 python이 실행되게 하면  
python3 이 3.8이 아닌 3.6을 가리키는 바람에 계속 호환성 때문에 안되다가, 

그래서 심볼릭 링크를 수정을 해줬는데.. 이 부분을 했음에도   
뭔가 꼬였는지 numpy가 없다고 한다.. no module found  
그래서 다 지우고 다시 해서 설치를 성공함;;

.local/lib/python3.8/site-packages  
디렉토리를 날려버리고 , 단 아나콘다를 설치한 후 pip을 사용해서 아직까지는 python3.8 만들어 지지 않고 있음  
(이걸 한 이유는 cocoapi를 설치할 때 계속 3.6으로만 실행되다가 3.8로 실행이 되게 했더니...  
setuptools가 없다고 하고, numpy가 없다고 하고,, 거의 미칠 지경 ㅋㅋㅋ 왜냐면 다 설치가 되어 있으니;;;   
어딘가에서 꼬인거 같아서 삭제해버림-- 일단 추천하지는 않음)

파이썬 3.8 소스 파일에서 다시 인스토를 함  
아나콘다도 지우고 다시 설치

