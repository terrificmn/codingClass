# image_transport 를 이용 compressed image 만들기
TODO:: 현재 테스트 중인 compressed_cam 패키지 계속 만들어야 함

wiki.ros.org/image_transport 
https://github.com/ros-perception/image_transport_plugins/compressed_image_transport

참고하기 

먼저 ros-noetic-image-transport 패키지를 설치

topic 메세지는 sensor_msgs/CompressedImage 를 사용



보통 ros subscriber/publisher 방식은 비슷하지만 다른식으로 만들어준다.

```cpp
ros::NodeHandle nh;
imgae_transport::ImageTransport it(nh);
image_transport::Subscriber sub = it.subscribe("camera/color/image_raw", 1, imageCallback);
image_transport::Publisher pub = it.advertise("camera/color/compressed_image", 1);
```

node 핸들러로 접근해서 만드는 방식에서   
ImageTransport 를 만들어서 sub/pub을 만드는 방식




