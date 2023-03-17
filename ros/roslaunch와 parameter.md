# roslaunch & parameter
ROS 런치파일에서 쉽게 파라미터를 설정할 수가 있다.

```xml
<node name="camera" pkg="camera_pkg" type="camera_pkg_node" output="screen">
    <param name="camera_name" type="string" value="camera1"/>
</node>
```

또는 arg먼트를 설정한 다음에 param 안에 넣어줄 수도 있다
```xml
<arg name="camera_name" default="camera"/>

<node name="camera" pkg="camera_pkg" type="camera_pkg_node" output="screen">
    <param name="camera_name" type="string" value="$(arg camera_name)"/>
</node>
```

## c++에서 파라미터를 처리
c++ 소스코드에서 파라미터를 어떻게 처리하느냐에 따라서 상황이 달라지는 듯 하다   

일단, `ros::NodeHandle nh;` 이런식으로 생성한다면 네임스페이스 없이 생성이 될 것이고, 
이런 상황에서는 위 처럼 파라미터를 설정하면 값이 제대로 안 받아진다.   
파라미터를 node 태그 위로 올려서 마치 root 경로에서 파라미터 값이 쓰여질 수 있게 하면  
값이 제대로 읽혀진다  

예:
```xml
<param name="camera_name" type="string" value="camera1"/>

<node name="camera" pkg="camera_pkg" type="camera_pkg_node" output="screen">
</node>
```

하지만 `ros::NodeHandle nh("~")` 처럼 private 핸들러로 생성을 하게 되면 노드명으로 네임스페이스가 생기게 된다   
이럴 경우에는 파라미터를 노드 태그 안으로 넣어줘야 한다 

```xml
<node name="camera" pkg="camera_pkg" type="camera_pkg_node" output="screen">
    <param name="camera_name" type="string" value="camera1"/>
</node>
```

만약 카메라 노드를 `ros::init(argc, argv, "camera")` 이런식으로 생성했다면  
`/camera/camera_name` 이라는 파라미터로 받아지게 된다.   

그래서 cpp에서는
```cpp
std::string camera_name = "camera"; //default
nh.getParam("/camera/camera_name", camera_name);
```
이런식으로 받야함

## 하지만, 
오픈소스들을 가만히 보면 main() 함수에서 노드 핸들러를 일반과 프라이빗을 각각 만들어서   
특정한 클래스를 생성할 때 넘겨주는 경우도 있는 듯 하다..   

이런 경우에는 좀 더 복잡해지는 듯 하지만... 

어쨋든 프라이빗으로 만들었다면, 런치파일에서는 그룹으로 묶어서 전달해야하는 듯 하다
```xml
<arg name="camera_name" default="camera"/>

<group ns="$(arg camera_name)">
    <node name="camera" pkg="camera_pkg" type="camera_pkg_node" output="screen">
        <param name="camera_name" type="string" value="$(arg camera_name)"/>
    </node>
```

이렇게 하면 `/camera/camera_name` 으로 파라미터를 넘겨줄 수 있게 된다.  

이렇게 하면 프라이빗 핸들러에서 노드이름/파라미터 로 받을 수 있게 되는 듯 하다.. 

> 하지만, 노드이름은 예를 들어 camera_node로 생성했는데.. `ros::init(argc, argv, "camera_node")`   
어찌 /camera_node 가 아닌 camera로 받을 수 있는지는 아직 잘 모르겠다.. 연구가 더 필요 


## 오픈 소스 등에서 실 사용 예
```cpp
main() {
    ros::init(argc, argv, "camera_node");
    ros::NodeHandle nh;
    ros::NodeHandle private_nh;

    // 특정클래스를 인스턴스 에서 위의 노드 핸들러를 넘긴다 
    MyClass myclass(nh, nh_private); 
    //.... 생략.;
}
```

이렇게 하고, MyClass 생성자에서 노드 핸들러 및 상속으로 시작하게 된다 
```cpp
MyClass:MyClass(ros::NodeHandle& nh, ros::NodeHandle& private_nh) : nh_(nh), private_nh_(private_nh) {
    ... 그리고 시작
    this->setParam();
}
```

그래서 reference로 받은 node 핸들러를 이용해서 파라미터를 설정하게 된다 
```cpp
void MyClass:setParam() {
    camera_name = private_nh_.param<std::string>("camera_name", "camera1");
    // ... and so on
}
```


