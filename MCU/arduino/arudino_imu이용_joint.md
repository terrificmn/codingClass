# arduino 이용해서 imu로 전송해보기
아두이노, 아두이노 나노, ESP32 아무거나   

imu 센서를 x축 방향으로, y축 방향, z축 방향으로 움직여서 해당 센서 데이터를 이용해서  
imu_data 와 tf를 이용해서 로봇을 움직이게 된다 

[여기 참고](https://www.youtube.com/watch?v=BOvf4X55WAk)

먼저 imu 관련해서 arduino로 만들어서 mecanum_description 패키지의 gazebo 시뮬레이션 작동시켜보기

mcu에서 imu_data를 pub 하는 노드 하나,  
컴퓨터에서 tf 메세지를 pub 하는 노드 
gazebo나 rviz 띄우는 런치파일 정도로 구성이 될 듯 하다 



ros 시리얼로 연결하거나 그냥 시리얼로 연결 후 작동해보기 

imu_data 를 서브스크라이브 하고 (아두이노에 연결한 imu 이용)   
연결된 콜백 함수에서  

`geometry_msgs::TransformStamped ts_msg` 로 tf를 브로드케스트 하기 위해서 만들고   
link 별로 parent frame_id 와 child frame_id 를 만들어주고  
translation.x,y,z 같은 경우는 들어온 데이터 그대로 입력이 되고(ts_msg 에)   

rotation 같은 경우에는 오일러 앵글에서 quaternion 으로 변환을 해준다   

이렇게 만들어진 TransformStamped 메세지는 sendTransform()을 함수를 통해서 broadcasting 을 해서 퍼블리쉬한다   



프로토타입 만들어 본 후에 테스트 진행 및 업데이트하기!