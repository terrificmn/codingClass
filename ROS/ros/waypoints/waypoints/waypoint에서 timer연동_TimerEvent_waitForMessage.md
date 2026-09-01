ros에서 class를 만들고  callback 함수를 만들어서 timer를 연동시키면  
서브스크라이드 하듯이 계속 콜백 함수에서 원하는 내용을 사용할 수가 있다   

```cpp
class MyClass {
private: 
	ros::NodeHandle nh;
	ros::AsyncSpinner spinner;
	
public:
	MyClass() : nh(""), spinner(0){
		ros::Timer t1 = nh.createTimer(ros::Duration(1.0), &MyClass::myFunc1, this);

		ros::Timer t2 = nh.createTimer(ros::Duration(1.0), &MyClass::myFunc2, this);
	}
}

	void myFunc1(const ros::TimerEvent &) {
		....
	}
	
	void myFunc2(const ros::TimerEvent &) {
		....
	}
```

ros::Duration(1.0) 마다 함수 myFunc1을 호출해서 원하는 내용을 사용할 수가 있다   

그리고 함수에서는 아래처럼 사용
```cpp
void myFunc1(const ros::TimerEvent &) {
	boost::shared_ptr<std_msgs::Empty const> shared_ptr_ready; // std_msgs::Empty::ConstPtr ptr; or std_msgs::Empty::Ptr ptr; both available
	
	shared_ptr_ready = ros::topic::waitForMessage<std_msgs::Empty>("/save_path", ros::Duration(1));
	
	if(shared_ptr_ready) {
		...
	}
}
```

그래서 topic이 발행이 되면 subscribe를 한번 하고 그 내용까지 변수에 담아서 사용할 수 있는 waitForMessage 기능을 위와 같은 방법 처럼 사용할 수가 있다.  

### 단,
단, 특정한 콜백함수 예를 들어 LaserScan을 서브스크라이 하는 함수가 있다고 하던가  
어떤 함수에서 while을 돌려서 spinOnce() 기능을 사용한다면 위의 timer 기능을 사용할 수가 있는 것 같다 . 역시 AsyncSpinner를 사용해야지 함수가 blocking 을 하는 것을 막을 수 있음  

만약 뭔가 서브스크라이를 해서 계속 loop 되는 상황이 아니라면 timer로 연동을 시켜도 한번 작동을 하고 더 이상 실행을 안하는 문제가 발생하는 것 같다.  

그래서 그냥 ros::TimerEvent를 사용안하고 그냥 전통적으로 subscribe를 하는 콜백 함수로 만드는 것도 괜찮은 방법

waitForMessage()가 한번만 서브스크라이드 하고 그것을 이용할 수있는 매력은 있지만,   
어차피 subscribe하는 함수를 만들어도 구독해야할 topic이 퍼블리싱이 안된다면 어차피 대기(?) 상태로 아무것도 안하니 어렵게 생각안하고 subscribe를 하는 것도 방법인듯 하다   



