# ros::Rate
while()에서 ros::Rate 로 rate 객체를 만들어서 sleep을 걸어주면   
ros::spin() 을 할 때 지정한 시간만큼 슬립을 해줄 수가 있는데,, 

예
```cpp
ros::Rate rate(10);
while(ros::ok()) {

    // do sothing...

    rate.sleep();
    ros::spin();
}
```


만약 런치파일에서 `<param name="/use_sim_time" value="true" />` 로 되어 있으면    
시간 자체가 1970- 으로 셋팅이 되면서 타이머가 제대로 작동이 안되는 듯 하다.   
그래서 sleep() 계속 하게 되면서 해당 구간에서 block 된다.

ros::Timer 도 마찬가지로 작동(block)

> 단, 콜백 함수는 잘 작동한다.

그래서 block을 막아줄려면 위의 use_sim_time 을 false로 설정해주면 된다. 

> 위의 use_sim_time 같은 경우는 파라미터 서버 등에 저장(?) 되어서 한번 실행해서 파라미터 셋 하면   
그 다음부터는 계속 그 설정을 유지한다.  true / false를 다시 바꾸려면 다시 한번 실행해줘야 함

