aplay 명령어로 실행을 할  수가 있는데 mp3 파일을 잘 재생을 못하는 것 같다 

그래서 vlc 프로그램을 설치를 하고, cvlc 명령을 사용해서 실행해줄 수가 있다 

실행을 하기 위해서는 vlc를 먼저 설치를 하고
```
sudo apt install vlc
```

ros에서 실행을 할 때

일단 다른 노드에서 사용을 할 경우에는 publish를 할 수게 만들어 준다음에   
특정 토픽을 만들고 std_msgs/String type을 이용해서  

스트링 타입으로 file의 경로를 지정해준다  
예를 들어서 이런식으로 작성해서 퍼블리시  
```cpp
//topic 및 publish 지정
sound_pub = nh_.advertise<std_msgs::String>("/sound_file", 1);

std_msgs::String sound_str;
sound_str.data = "file경로/sound.mp3"

ros::Rate lr(1);
while(ros::ok()) {
	sound_pub.publish(sound_str);
	
	ros.spinOnce();
	lr.sleep();
}
```

그래서 

subscribe을 할 노드에서는 string 을 구독한 다음에 특정 시점에 재생을 하면 될 듯 하다
subscribe callback 함수에서 topic으로 받은 다음에 
```cpp
ros::Subscriber sound_sub; 
sound_sub = nh_.subscribe<std_msgs::String>("/sound_file", 1, &클래스명::subSound, this);

subSound(const std_msgs::String::Constptr &msg) {
	// 여기에서 처리하거나 변수에 저장시킨다
}
```


현재 딱히 publish & subscribe를 이용해서 할 필요는 없어서 실행만 해보았다   

> publish & subscribe를 해서 할 때에도 결국은 system() 함수로 리눅스 명령어를 실행해준다   
> 단, 더 좋은 방법이 있다면 당연히 그 방법을 사용을 하도록 하자.  


system()  함수를 사용해서 cvlc 명령어를 실행해주면 된다  
```cpp
std::string sound_file_path = "soundfile경로/sound.mp3 --play-and-exit";
std::string cmd = "cvlc " + sound_file_path;
system(cmd.c_str());
ROS_INFO("Sound played");
```

> 옵션 --play-and-exit 를 넣어주는 이유는 한번만 실행하기 위해서이고 다음에 사운드를 다시 한번 재생하려면 옵션을 넣어야 함. 옵션을 안 넣어준다면 다시 또 실행하려고 하면 안됨   


그리고 재생이 되는 동안 blocking이 되는 것에 주의, 재생 되는 동안 다른 동작이 멈추는데  
딜레이가 싫다면 string에 &를 추가해서 back-ground에서 재생되도록 하자

