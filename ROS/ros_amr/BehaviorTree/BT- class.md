Behavior Tree를 사용하면  

원래는 class도 객체로 만들어줘야지 사용을 할 수가 있지만.. 변수에 할당을 해줘야지 사용을 할 텐데..  

BT를 사용하다보니 아직 정확하지는 않지만   
class를 따로 객체로 만들어서 사용하지 않고, tree에 넣지 않아도 그 클래스를 사용할 수 가 있다.  
상황에 따라 다르겠지만 BT::AsyncActionNode 로 사용을 하고 ROS로 서브스크라이브 해서 뭔가 처리 하는 경우에 ...

계속 메세지가 반복이 되어서 한번만 처리를 하려고 해도 계속 실패를 하고 중복 처리가 되었는데  
클래스를 사용하고 있었고 

BT tree에는 추가를 하지 않고 별개로 사용을 하려고 했었는데  
물론 해당 클래스를 BT를 상속 받지도 않음   

그런데 이미 다 실행이 되고 있다... 아직 이유는 잘 모르겠다  

```cpp
class Myclass {
public:
	Myclass() : nh("~"), spinner(0) {
	
	empty_sub = nh.subscribe<std_msgs::Empty>("/reset", 1, &Myclass::myCallback, this);
	}
	생략..

	myCallback(...생략) {
		..생략
	}
	
};

class SetEntry : public BT::AsyncActionNode, MyClass {
public:
	SetEntry(const std::string& name, const BT::NodeConfiguration& config)
	: BT::AsyncActionNode(name, config) {
	}
	생략..
};


int main() {
	...생략
	MyClass myclassOj; // 이렇게 하면 2번씩 수행이 된다.. BT에서 tick 할 때 더 실행됨
	
	// use the BehaviorTreeFactory class to register nodes
	BT::BehaviorTreeFactory factory;
	
	factory.registerNodeType<SetEntry>("SetEntry");
	factory.registerNodeType<ReadEntry>("ReadEntry");
	...생략
}
```

예를 들어서 위에 같은 경우인데  
Myclass는 주로 ROS에서 서브스크라이를 하고 topic을 받아서 데이터를 저장해주는 것으로 만들었는데 BT class를 상속을 받지 않음. 

하지만 위와 같이 사용을 했더니  
myclassOj도 실행이 되고, BT 에서도 사용이 되는 것 같다.  중복으로 사용되는 듯...

그래서 2번씩 수행이 되버림. 그래서 2번씩 반복되는 것을 잡아낼려고ㅠㅠㅠ

SyncActionNode 방식으로 만들어서 그런 것인가? 의심가는 것은 BT tree에 등록을 시킨  
SetEntry class는 BT와 MyClass도 상속을 받았다는 것...

일단은 MyClass myclassOj; 부분은 지우고 시작하자
```cpp
// MyClass myclassOj; // or delete
```
