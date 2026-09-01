python의 subprocess 를 이용해서 ROS 의 rosrun 으로 노드 실행시키기 

먼저 import
```python
import subprocess
import os
import signal
```

그리고 어떤 test라는 함수가 있고 반복이 될 때마다 실행 시키고 끄는 것으로 설정하면

```python
class MyApp():
	def __init__(self, **kwargs):
		... 생략...


	def test(self, *args):
		po = subprocess.Popen("rosrun my_pkg my_node", stdout=subprocess.PIPE, shell=True)
		if self.count % 2 == 0 :
			self.screen.ids.center_label.text = 'launch my_node'
		else :
			self.screen.ids.center_label.text = 'my_node terminated'
			os.killpg(os.getpgid(po.pid), signal.SIGTERM)
		
		self.count += 1
```

이런식으로 subprocess.Popen() 으로 열고 
닫을 때는 os.killpg()를 이용해서 pgid 로 죽일 수 있다 


단순히 여는 것은  os.popen()으로도 실행이 가능   
```python
import os

os.popen("rosrun my_pkg my_node")
```


popen() 2, 3, 4 버전? 종류가 많은 듯 하다 

> Popen, popen 은 다르다.  하나는 subprocess, 마지막은 os

[여기 참고하기 Popen 종료하기](https://pythonsolved.com/how-to-close-all-subprocesses-in-python/)

[파이썬 os.popen 종류 및 설명](https://stackabuse.com/pythons-os-and-subprocess-popen-commands/)



## roslaunch 도 있음
아;;; 런치파일을 꼭 만들어야 하는 줄 알았으나,, 꼭 그런것은 아닌 듯 하다.  
패키지와 노드를 입력해주고 그것을 실행시켜주는 듯...   

사실 안해봐서 잘 모르겠다

> ros cli 인 roslaunch 와는 다른 python 내에서 사용하는 라이브러리
