ros callback 사용해서 할 때  

한 function에서 while(ros::ok()) 조건으로 loop를 실행한다고 하면  
블락킹 현상 때문에 다른 함수들이 실행이 안 된다 

이때 async spinner와 ros timer를 연동해서 함수에 호출을 해주면  
각각 함수가 서로 잘 돌아간다  


```cpp
class AsyncTimer {
private:
    ros::Nodehandle n_;
    ros::AsyncSpinner spinner;

public:
    Asynctimer() : n_(""), spinner(0) {
        ros::Timer timer = nh.createTimer(ros::Duration(1.0), &Asynctimer::func1, this);
        spiiner.start();
        this->func2();
    }

    void func1(const ros::TimerEvent &) {
        boost::shared_ptr<std_msgs::Empty const> wait_msg;  
        wait_msg = ros::topic::waitForMessage<std_msgs::Empty>("/msg_wait", ros::Duration(1));
        while(ros::ok()) {
            try {
                if(....)
            }
        }
    }

    void func2() {
        
        while(!this->loop_ok) {
            try {
                ....
            }
        }
    }
};

```
사실 서로 다른 메소드 (함수) 에서 while 문을 각기 어떻게 돌릴까 고민했는데  
waitForMessage()를 이용해서 할려고 하다보니  while문이 아예 다른 함수를 사용 못하게 된다  

1. 그래서 하나의 방법은 아예 waitForMessage()를 사용하지 말고 subscribe를 해서 받으면 될꺼 같다   
2. 아니면 service를 만들어준다. 이것도 함수가 매칭이 되므로 srv가 하나의 방법이 될 수 있을 수도 

그 외에 timer 연동을 해보고 안되면 위의 2개의 방법을 사용해볼 생각이었으나  
다행히 Timer연동으로 해결이 어느 정도는 되는 듯 하다  
그리고 콜백함수로 계속 호출되니 func1의 while문도 필요가 없어졌다  



[여기ros Timer 튜토리얼 참고](http://wiki.ros.org/roscpp_tutorials/Tutorials/Timers)

