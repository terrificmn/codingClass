C++ 에서는 0으로 initialization 하는 것을 피하는 것이 좋다. 예기치 못한 상황으로 이어질 수 있음  
포인터에서는 0으로 비교하지 말자  

앗 nullptr로 비교하는 것도 별로 좋은 방법은 아니라고 한다 redundant한 방법  

그래서 ! 으로 (false 일 경우 실행) 식으로 비교하는 것이 좋다고 하는 방식이라고 한다  

```cpp
int *ptr;

// nullptr 일 경우
if (!ptr) {
    std::cout << "Not Valid" << std::endl;
} else {
    std::cout << "OK! It's good to go!" << std::endl;
}
```


그래도 사용은 가능하지만 nullptr로 비교할 때의 예 (recommend는 아니라고 함)   
테스트 해보니 작동은 잘 함  

```cpp
geometry_msgs::PoseStamped *pubPosePtr;

if (pubPosePtr != nullptr) {
    std::cout << "valid" << std::endl;
    //clientCoap(pubPosePtr->pose.position.x, pubPosePtr->pose.position.y, this->macAddress);
} else {
    std::cout << "null pointer" << std::endl;
}
```

pubPosePtr은 geometry_msgs::PoseStamped 로 선언한 포인터   
이게 null 이 맞는지 확인  

이게 꼭 필요한 이유가 pubPosePtr 이 널 값인데 어떤 데이터를 함수에 넘기거나 사용하려고 하면  

Segmentation fault (core dumped)

가 발생을 한다  

그래서 꼭 체크 할 수 있게 해야한다  



> 내가 만든 프로그램에서는 ros::spin() 이 계속 발생하는데 어떤 아주 미세한 차이로  
데이터가 담겨서 유효하기도 하고 null 되어 프로그램이 종료가 되는 현상이 발생했다  
그 전에 논리적으로 프로그램이 잘 진행되는 것이 먼저 순서 이겠으나, 예외처리를 꼭 해줘야 할 듯 하다  

