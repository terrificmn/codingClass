# roslaunch & parameter 2
ROS 런치파일에서 쉽게 파라미터를 설정할 수가 있다.

아예 예제를 만들어보자

```xml
<node name="test_nh" pkg="test_nh" type="test_nh_node" output="screen">
    <param name="test_param1" type="string" value="test string"/>
    <param name="test_param2" type="string" value="hello world"/>
    <param name="test_param3" type="bool" value="true"/>
</node>
```

노드 핸들러에서 일반적으로 생성이 되었을 경우에는 node 안으로 들어가 있으므로 이것은 프라이빗 핸들러 처럼 사용된다 

> The <param> tag can be put inside of a <node> tag, in which case the parameter is treated like a private parameter. 

그래서 roslaunch 파일을 실행하면 결과가 안나오게 된다 
```
[ INFO] [1679049195.642436077]: test param1: 
[ INFO] [1679049195.642442321]: test param2: 
[ INFO] [1679049195.642448146]: test param3: false
```

하지만 param을 위로 올리면   
```xml
    <param name="test_param1" type="string" value="test string"/>
        <param name="test_param2" type="string" value="hello world"/>
        <param name="test_param3" type="bool" value="true"/>
    
    <node name="test_nh" pkg="test_nh" type="test_nh_node" output="screen">
    </node>
```

정상적으로 받아진다
```
[ INFO] [1679049378.472731747]: test param1: test string
[ INFO] [1679049378.472738307]: test param2: hello world
[ INFO] [1679049378.472744600]: test param3: true
```

## 이제 private 핸들러로 테스트 해보자

