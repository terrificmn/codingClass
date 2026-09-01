# executor

single thread/ multi thread  실행하기   
하나의 executor 방식을 선택해서 해주는 것이 좋을 듯 하다.  


SingleThreadedExecutor  single thread 방식은 결국 add_node를 할 수 있다. block이 된다. 

executor 에 add_node를 해준 후에 spin()을 해주면 사용이 가능하다. 

MultiThreadedExecutor 는 각각의 노드에서 퍼블리쉬를 해도 다른 노드를 block 시키지는 않는다. 



```cpp

void myCallback1() {
    stdInfo("Hello");
}
void myCallback2() {
    stdInfo("callback1");
    std::this_thread::sleep_for(std::chrono::milliseconds(1500));
}
void myCallback3() {
    stdInfo("Single 3");
}

int main(int argc, char *argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::Node::SharedPtr myNode = std::make_shared<rclcpp::Node>("mynode1"); 
    rclcpp::Node::SharedPtr myNode2 = std::make_shared<rclcpp::Node>("mynode2");
    rclcpp::Node::SharedPtr myNode3 = std::make_shared<rclcpp::Node>("mynode3"); 
    rclcpp::TimerBase::SharedPtr eventTimer = myNode->create_wall_timer(
                                                                            std::chrono::milliseconds(500),
                                                                            std::bind(&myCallback1)
                                                                        );
    rclcpp::TimerBase::SharedPtr eventTimer2 = myNode2->create_wall_timer(
                                                                            std::chrono::milliseconds(500),
                                                                            std::bind(&myCallback2)
                                                                        );
    rclcpp::TimerBase::SharedPtr eventTimer3 = myNode3->create_wall_timer(
                                                                                std::chrono::milliseconds(1000),
                                                                                std::bind(&myCallback3)
                                                                                );
    myNode->create_publisher<std_msgs::msg::Bool>("mytopic1", 1);
    myNode2->create_publisher<std_msgs::msg::Bool>("mytopic2", 1);
    myNode3->create_publisher<std_msgs::msg::Bool>("mytopic3", 1);


    /// rclcpp::Node 를 상속 받는 경우에는 이런식으로도 생성 가능
    /// MyClassNode가 있고 rclcpp::Node 를 상속 받아서 사용하는 경우에 사용 가능
    // rclcpp::Node::SharedPtr myClassNode = std::make_shared<MyClassNode>("my_node"); // 셋 다 가능
    std::shared_ptr<MyClassNode> bridge = std::make_shared<MyClassNode>("my_node");
    auto myNode = std::make_shared<MyClassNode>("my_node");


    rclcpp::executors::SingleThreadedExecutor executor;
    rclcpp::executors::MultiThreadedExecutor mulexecutor;
    mulexecutor.add_node(myNode);
    mulexecutor.add_node(myNode2);
    // 만약 싱글 스레드 방식으로 넣게 되면 위의 multithread도 block이 되는 듯 하다.
    executor.add_node(myNode3); /// 여러 방식으로 테스트 해보기 
    // 
    
    executor.spin();
    mulexecutor.spin();

}
```