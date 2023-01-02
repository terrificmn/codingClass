
qt의 slots 이용해서 .h 헤더 파일에 정의를 해준다 
```cpp
Q_DECLARE_METATYPE(geometry_msgs::Pose)

class Example : public QObject {
	Q_OBJECT
public slots:
	void getRosType(std::vector<geometry_msgs::Pose> pose_vec);
}
```

slots 을 이용해서 ROS의 메세지 타입을 사용할려면 QT에서 알 수 있게 metatype을 정의를 해준다   


이제 cpp 파일에서 생성자에서 slot 을 사용할 클래스 및 함수를 연결해준다
```cpp
// 생성자
Example::Example {
	QObject::connect(&사용할클래스명, &사용할클래스::함수, this, &Example::getRosType);
}

Example::getRosType(std::vector<geometry_msgs::Pose> pose_vec) {
	/// 내용 
}

```

대충 위의 내용이 QObject 클래스를 이용해서 connect를 연결해줄 수가 있는데..   
만약 같은 클래스를 사용한다면 같은 클래스명을 사용하면 될 것이고  

다른 클래스에서 사용한다면 다른 클래스 이름을 적어준다.   
예를 들어서 
```cpp
Example::Example {
	QObject::connect(&Sending, &Sending::sendRosType, this, &Example::getRosType);
}
```
위와 같은 방법으로 사용을 해서 만들어주고, Sending이라는 클래스가 보내는 쪽이 되고   
Sending클래스의 sendRosType 메소드에서 emit을 사용해서 호출을 하게 된다     
그러면 Example 클래스의 getRosType이 그 내용을 받을 수 있게 된다   

> Sending 클래스가 없어서 에러가 발생한다면 포인터를 만들어서 사용해야하고, 해당 클래스 헤더파일이 따로 있다면 include 해준다 


그리고 Sending 클래스의 sendPoseType 메소드는 이런식이 된다   

```cpp
void Sending::어떤어떤함수() {
	geometry_msgs::Pose msg;
	// msg를 만들어준다. 
	// msg 만드는 부분 생략..
	emit sendRosType(msg);
}
```

sendRoSType 함수를 따로 만드는 것은 아니고, 클래스에서 사용할 메소드에서 emit 키워드와 함께 호출해서 사용하면 된다   

그러면 마치 Ros의 publish를 한 것 처럼 msg가 전달이 되면   
연결했던 Example클래스에서 getRosType에서 파라미터를 전달받아서 사용할 수 있게 된다 



-- update 필요!

