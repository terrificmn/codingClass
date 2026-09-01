# humble setuptools
ROS2 humble 버전에서 colcon 빌드를 하니 당장 문제가 아래와 같은 warning이 발생한다
```
SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
```
warning 이면 괜찮을 것이라고 생각했는데 빌드는 계속 실패를 했다.  
찾아보니, python의 setuptools 버전을 낮춰야 하는 듯했다. 

먼저 python3 버전을 알아보자
```
python3
```

뜨헉.. 3.10 , 우분투 20.04 에서는 3.8 이었는데 벌써 기본으로 업그레이드가 되어 있구나 했다.  
```
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
```

setuptools 버전을 확인하는 것은 아래와 같다. >>> 파이썬 cli 모드에 들어간 상태에서   
import와 print() 함수를 사용하면 된다
```
>>> import setuptools
>>> print(setuptools.__version__)
59.6.0
```

버전이 역시 높다. ROS2 humble (우분투 22.04) 에서는 python3 3.10에 셋업툴즈는 59.6 인 듯 했다.   

> 더 높을 수도 있다. 사실 docker image로 설치를 한 것이라;;;

어쨋든 셋업툴즈 58.2가 ROS2와 python 패키지 관련해서 문제가 없는 마지막 버전이라고 한다.   
아직까지는 (on Apr19 2023) 유효한 듯 하다   

> python에서도 예전 방식(old) 으로 설치를 하는 것인듯 한데, 이것도 새로운 방식으로 바뀐듯하다   
pip and ament 방식인듯 하다(새로운 standard 방식이라고 함)


아래 처럼 실행해해서 셋업 툴즈 버전을 낮춰준다 
```
sudo apt install python3-pip
python3 -m pip install setuptools==58.2.0
```

그리고 다시 워크스페이스로 이동을 한 후에 
```
colcon build
```

이제 워닝은 없고, 
```
Summary: 27 packages finished [3.23s]
```
아주 좋다! ㅋㅋ