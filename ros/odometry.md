# odometry
다른 프로그램 등에서는 일반적(?)으로 joint_state 등을 이용해서 값을 받아와서 하는 방식이 있는데  
joint_state 에는 velocity 가 있어서 값을 읽어오는데  

사실 중요한 것은 모터의 엔코더로 부터 값을 읽어와서 joint state 메세지에 넣어서 보내줘야 하는데   
당연히 그 부분은 생략되어 있기 때문에 (거의 bringup에서 취급)   

역시 odom을 구하기 위해서는 직접 모터 encoder로 부터 시리얼 통신으로 받아오는게 먼저 중요할 것 같다   

TT motor가 오면 테스트를 해보자!!! 아자!