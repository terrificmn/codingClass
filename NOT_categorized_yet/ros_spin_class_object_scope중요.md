# 어느 scope에서 생성하느냐가 중요하다

library로 subscribe하는 class를 만들었는데  
다른 ros pkg에서 CMakeLists.txt 파일에서 find_package()에서 라이브러리로 불러오는데 성공!  
이제 include를 해서 사용을 하면 되는데   

class를 object로 인스턴스화 해놓고 사용하는데 계속 spin()이 되어야 하는데  
정확하게는 ascyncrous 방식으로 spinOnce 처럼 작동을 해야하는데  
계속 한번만 spin을 한 후에 프로그램이 종료가 된다   

그 전에는 특정 publish_pose() 같은 함수에서 while문이 작동을 했는데   
계속 인수로 넘겨주는게 별로 인거 같아서 다른 또 특정한 publish_pose() 함수내의   
내가 사용해야할 예를 들어 createJson() 함수에 넣어주기 위해서 사용을 해야했는데  

인수로 넘기기 보다 createJson() 함수 내에서  함수 scope 안에서 class를 객체화해서 만들었다  

그게 문제 였다. 함수의 로컬 스코프를 벗어나는 순간 소멸이 되는 듯 했다.   
그래서 프로그램이 종료되는 듯(?)했다. 오류는 나지 않음  

결국은 publish_pose() 함수 위의 while문이 시작하기 전에 class를 만들고 사용을 하니  
정상 작동하였다.  

대충 이런식으로 했더니 잘 작동하던 프로그램이 한번만 실행하고 종료
```cpp
void callback(const::nav_msgs::Path::ConstPtr &msg) {
	....
}

void publish_pose() {
	....
	....
	while(ros::ok()) {
		...
		createJson();
		ros::spinOnce();
	}
}

void createJson() {
	myClass classObj;
	classObj.getPose();
	...
	...
	writer.StartObject();
	...
}
```


대충 상위의 scope에서 클래스를 만들고  
그리고 내가 사용하려고 했던 기능의 함수에 인수로 값을 넘겨준다  

```cpp
void callback(const::nav_msgs::Path::ConstPtr &msg) {
	....
}

void publish_pose() {
	myClass classObj;
	classObj.getPose();
	
	....
	while(ros::ok()) {
		...
		geometry_msgs::Pose resutlPose = classObj.getPose();
		createJson(resultPose);
		ros::spinOnce();
	}
}

void createJson(geometry_msgs::Pose pose) {
	writer.StartObject();
	...
}
```

대충 재연을 해봤는데 더 좋은 방법이 있으면 업데이트를 하겠지만  

중요한 것은 **scope 블럭 안에서 효과적**으로 **잘 사용**을 해야겠다  

