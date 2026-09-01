# roslaunch python 

처음에 런치파일을 만들고 그것을 실행시켜주는 것 인줄 알았는데   
그래서 그냥 popen을 사용했는데... 그렇게 안해도 될 듯 하다  

먼저  `import roslaunch` 를 해서 사용하고

자세한 것은 더 공부를 해봐야 함..
아무래도  python 코드 내에서 다른 노드를 실행시키려고 하면 roslaunch 가 더 편할 듯 하다 ㅠ (popen 보다?)

simple 사용법
```python
import roslaunch

package = 'rqt_gui'
executable = 'rqt_gui'
node = roslaunch.core.Node(package, executable)
launch = roslaunch.scriptapi.ROSLaunch()
launch.start()
process = launch.launch(node)
print process.is_alive()
process.stop()
```

[자세한 것은 py roslaunch 관련 API 살펴보기](http://wiki.ros.org/roslaunch/API%20Usage)


