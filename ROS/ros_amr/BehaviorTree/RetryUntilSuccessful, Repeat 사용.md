BT tree 중에서 RetryUntilSuccessful 을 사용하면 실패했을 때 다시 시도할 수 있게 할 수 있는데...   
횟수를 지정해줄 수 있다.  


```cpp
class SetRetry : public BT::AsyncActionNode {
private:

public:
	SetRetry(const std::string& name, const BT::NodeConfiguration& config) : AsyncActionNode(name, config) {
}
	static BT::PortsList providedPorts() {
		return { BT::OutputPort<int>("attempts") };
	}
	BT::NodeStatus tick() override {
		int try_again_num = 5; 
		// the output set
		setOutput("attempts", try_again_num);
		return BT::NodeStatus::SUCCESS;
	}
};
```

여기에서  `BT::OutputPort<int>("attempts")` 로 리턴하는 부분과, tick() 함수에서 int try_again_num 을 이 설정이 되는데   

위와 같은 방식으로 처리할 수가 있다. SetRetry는 클래스명이고,  main() 함수에서 node를 등록해야한다
```cpp
BT::BehaviorTreeFactory factory;
factory.registerNodeType<SetRetry>("SetRetry");
```

이제 BT tree xml 파일에서  
```xml
<SetRetry name="set_retry_until_success" num_attempts="{try_again_num}" />
<RetryUntilSuccessful num_attempts="{try_again_num}">
```

위의 SetRetry에서 가져온 횟수만큼 반복할 수 있게 해준다  

기억이 안나는데;;;  클래스를 만들필요없이, 그냥 RetryUntilSuccessful 만 넣어줘서 숫자로 넣어서 되는지는 해보지를 않았다;; 하드코딩으로 될 것 같기도 하지만.. 테스트는 나중에;;;

> 횟수를 지정하는 int에 -1 값을 주면 무한 반복이 가능하다   


비슷하게 반복하는 것으로는 Repeat,   KeepRunningUntilFailure 등이 있는데... 조금씩 성격이 다르다   
Repeat도 반복할 숫자를 지정해줄 수 있고 ,   KeepRunningUntilFailure 은 실패할 때 까지 계속 반복한다. 

bt tree xml
```xml
<Repeat num_cycles="3">
	<Sequence name="main_loop">
		.... some action...
	</Sequence>
</Repeat>
```

다행히 따로 클래스를 만들 필요는 없다 .  전체 과정을 반복하고 싶으면 Repeat으로 감싸주니 잘 반복한다  

> Repeat도 RetryUntilSuccessful 처럼 -1 값을 넣어주면 무한 반복한다   






