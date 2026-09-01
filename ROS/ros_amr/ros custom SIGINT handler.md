## SIGINT handler
signal.h 을 이용해서 SIGINT를 custom으로 만들 수 있는데  

```cpp
#include <ros/ros.h>
#include <signal.h>
void mySigintHandler(int sig)
{
  // Do some custom action.
  // For example, publish a stop message to some other nodes.
  
  // All the default sigint handler does is call shutdown()
  ros::shutdown();
}
int main(int argc, char** argv)
{
  ros::init(argc, argv, "my_node_name", ros::init_options::NoSigintHandler);
  ros::NodeHandle nh;
  // Override the default ros sigint handler.
  // This must be set after the first NodeHandle is created.
  signal(SIGINT, mySigintHandler);
  
  //...
  ros::spin();
  return 0;
}
```


기본 ros sigint handler를 설정해 줄 수가 있는데   

ros::shutdown()이(기본) 실행 되기 전에 다른 작업을 수행할 수 있게 한다   


## signal 관련 함수에 파라미터 넘기기

기존의 signal() 함수에는 2개의 파라미터, 하나는 SIGINT, 두 번째는 함수 이름을 적게 되어 있는데   

이 함수에는 파라미터를 더 추가 할 수가 없다. 그래서 위의 예처럼 `mySigintHandler` 로 지정하고  
`void mySigintHandler(int sig);` 정의해주는데   

해당 핸들러 함수에서 파라미터를 더 받고 싶은 경우에는 포인터를 이용해서 사용할 수가 있다  

함수 정의는..
```cpp
int mySigHandler(const int signal, void *ptr);

//또는 특정 클래스의 포인터를 넘겨서 처리하고 싶은 경우, 클래스 포인터로 넘겨줄 수도 있다
int mySigHandler(int signal, MyClassA *myClassAPtr);
```

이제 함수 안에서 종료될 때 사용할 수 있는 것을 짜준다
```cpp
int mySigHandler(int signal, MyClassA *myClassAPtr) {
    // 뭔가를 save? 이런게 있다고 가정
    myClassAPtr->saveFunction("exit time");

    if(signal == SIGINT) {
        // ros같은 경우
        ros::shutdown();
    }
    return 0;
}
```

이제 signal() 함수를 main 함수 내에서 사용하고 싶은 곳에 넣어주고 사용하면 된다 
보통 처럼 하나의 파라미터가 있으면 `signal(SIGINT, mySigintHandler);` 처럼 쓰겠지만..   

파라미터가 더 추가되어서 포인터를 받았기 때문에   
```cpp
signal(SIGINT, (void (*)(int))mySigHandler); 
```
처럼 해주면 된다. 

> 사실 이 부분은 공부가 더 필요하다. 완벽하게 이해하지는 못했지만.. void *ptr 이든, 클래스 *ptr 이든   
실행은 잘 된다.  


ros를 사용할 때 ros::shutdown() 등이 메인 while loop 아래쪽에 있지만, 실제로 ctrl+c 로 종료를 하게 되면   
거기 까지 도달을 안해서 특정 함수를 실행할 수가 없는데, 이때 활용하면 좋다.  





