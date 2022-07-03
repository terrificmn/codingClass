```cpp
   // 파라미터 관련
   class 땡땡 {
    private:
    int param_laserRanges;
    float param_turn_limit, param_dist_limit, param_spd_limit;

    public:
    땡땡() {
    this->declare_parameter<int>("laserMsgRanges", 1);
        this->declare_parameter<float>("turnLimit", 0.037);
        this->declare_parameter<float>("distanceLimit", 0.28);
        this->declare_parameter<float>("speedLimit", 0.04);

        this->get_parameter("laserMsgRanges", param_laserRanges);
        this->get_parameter("turnLimit", param_str_odom);
        this->get_parameter("distanceLimit", param_str_cmd);
    }
   };
```

class내에서 declare_parameter를 이용해서 파라미터를 만들고,
get_parameter로 파라미터 값을 받아서 특정 변수로 넘겨줄 수 있다. 예 param_laserRanges 에 저장

그러면 변수를 적극 활용하면 되고 

중요한 파라미터는 런치파일에서 값을 주게 된다

만약 런치파일을 실행하지 않는다면 declare_parameter로 선언한 값이 그대로 적용된다

