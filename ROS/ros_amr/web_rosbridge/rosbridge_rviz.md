먼저 런치파일을 만들어서 실행을 해준다 

arviz_camera.launch   
이 런치파일에는 rosbridge 패키지와 rviz, tf 패키지, rostopic 등의 패키지를 실행 시켜주게 된다  

현재 만들고 있는 webpages 패키지 참고

이 부분은 extrinsics and intrinsics properties 에 관한 부분이 되겠다   

[stream-rviz 관련 참고하기](https://roboticsknowledgebase.com/wiki/tools/stream-rviz/)

[깃소스-rviz_camera_stream보기](https://bitbucket.org/theconstructcore/rviz_camera_stream_examples_tc/src/master/)

[다크프로그래머- 영상 좌표계](https://darkpgmr.tistory.com/77?category=460965)

1. tf 패키지를 이용해서 tf를 생성해주고  (chassis가 부모 프레임이 되는데 이 부분은 맞게 수정해준다)   
로봇(또는 시뮬레이션 상의 로봇)으로 부터 일정거리 떨어져 있는 카메라가 되서 그 로봇을 비추고 있는 카메라라고 생각하면 된다  
예를 들어서 x는 -1 만큼 뒤에서 비추고 있다고 생각하면 됨    
static_transform_publisher 노드에서 지정

2. CameraInfo 메세지를 rostopic 패키지를 이용해서 퍼블리쉬 해준다     
여러 파라미터 등은 위의 stream-rviz 링크 참고   

3. image stream은 압축을 해서 보내야하는데 그래야 메모리도 적게 소모하고 효과적으로 스트림이 된다고 한다   
roslibjs를 이용해서 스트림을 하려면 image는 compressed format이어야 한다   
image_transport 패키지를 이용해서 이미지를 압축

```xml
<node
    pkg="image_transport"
    type="republish"
    name="republish_image"
    output="screen"
    args="raw in:=/camera1/image
          compressed out:=/camera1/compressed/image">
</node>
```

