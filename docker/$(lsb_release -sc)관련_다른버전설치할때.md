물론 ros 이미지로 하면 금방 하지만 key나 sources.list 를 등록할 필요가 없지만  
nvidia 그래픽 관련을 사용하기 위해서 수동으로 ros설치함

ROS를 처음 설치할 때 당연히 우분투 버전에 맞는 ros 버전을 설치를 해야하는데   

그래서 처음에 sources.list 파일을 업데이트 해주는데   
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

이것을 도커로 옮기면 
```
RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list
```

하지만 주의해야할 점은  $(lsb_release -sc) 이 부분에서 focal 이라고 나온다는 점이다  
즉 우분투 20.04를 사용하고 있는데 우분투 18 버전의 ros melodic를 설치하려고 하면 저 부분이   
현재 우분투 20에 맞춰서 환경변수 값이 focal로 되어 있기 때문에   

그 이후에 RUN apt-get update && apt-get install -y ros-melodic-desktop-full 설치부분에서   
오류가 나면서 에러가 나게 된다.  

이 간단한 것 때문에 오류를 잡는데 오래걸렸다. 당연히 focal 우분투 20에서 melodic ros (우분투 18)을 찾고 있으니 안 되지  
그래서 수동으로 melodic으로 바꿔주면 그 다음은 desktop-full 버전을 잘 설치한다  
```
RUN echo "deb http://packages.ros.org/ros/ubuntu bionic main" > /etc/apt/sources.list.d/ros-latest.list && \
```

