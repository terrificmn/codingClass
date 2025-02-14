## ros 에서의 ROS_MASTER_URI 설정하기
ros melodic 버전을 쓸 때에는 master를 설정해서 터틀봇3와 PC (원격pc)와   
통신을 했었는데   

이번에 ros2를 보니 가장 크게 눈에 띄는 것은 master를 실행할 수 있게하는   
roscore 명령어가 없는 것이였다

melodic 에서는 ~/.bashrc 파일에 환경 변수 ROS_MASTER_URI , ROS_HOSTNAME 을 이용해서   
ROS_MASTER_URI 에는 Remote PC의 ip주소:11311 지정해주고   
ROS_HOSTNAME 에는 터틀봇3 버거의 라즈베리파이 ip주소를 지정해준다
그래서 원격피씨와 터틀봇3에서 서로 통신을 할 수 있게 되는 것

[역시 e메뉴얼 Melodic sbc 셋팅하기 중에서(상단의 버전 melodic을 클릭) ROS Network Configuration 알 수 있다](https://emanual.robotis.com/docs/en/platform/turtlebot3/sbc_setup/#ros-network-configuration)

melodic 같은 경우에는 우선 라즈베리파이의 ip를 확인한다 
```
ifconfig
```
그리고 PC (본인 컴퓨터(remote pc라고 칭한다))의 ip 주소도 확인해준다 

ip주소가 확인이 되었다면 각각의 .bashrc 파일을 수정해주는데... (Remote PC와 터틀봇3의 라즈베리파이4)   

ROS_MASTER_URI=http://PC의 IP주소:11311   
ROS_HOSTNAME=RASPBERRY_PI의 IP주소   
처럼 적어주게 된다 

먼저 터틀봇3의 라즈베리파이4 부터 확인   
원격 컴퓨터에서 ssh로 접속을 한 후   
```
ssh ubuntu@192.168.0.10
vi ~/.bashrc
```
맨 아래쪽으로 내려와서 i를 누른 후 편집을 시작  
PC가 master가 된다 192.168.0.100 이라고 가정한다면 아래처럼 입력한다  
HOSTNAME은 라즈베리파이의 ip주소를 입력한다  
다 입력했다면 ESC를 누른 후 wq를 눌러 저장 후 빠져나온다. 

```
export ROS_MASTER_URI=http://192.168.0.100:11311
export ROS_HOSTNAME=192.168.0.10
```

그리고 .bashrc파일을 적용시켜준다
```
source ~/.bashrc
```

이번에는 컴퓨터의 (Remote PC) .bashrc 파일을 수정해준다   
ssh로 접속을 했다면 exit를 해서 빠져나오거나 다른 터미널을 열어서 작업한다

위와 같은 방법으로 .bashrc 파일을 수정하는데 이번에는 ROS_HOSTNAME는 PC의 ip주소로 적어주면 된다  
아래 처럼 된다. 
```
export ROS_MASTER_URI=http://192.168.0.100:11311
export ROS_HOSTNAME=192.168.0.100
```
wq로 저장을 한 후 source ~/.bashrc를 적용시키자


<br/>

## ROS2에서 ROS_DOMAIN_ID

그런데 ROS2 foxy버전에서는 위와 같이 IP를 적어주는 방식을 사용하지 않고   
ROS_DOMAIN_ID를 사용해서 같은 네트워크에서 원격pc와 터틀봇의 라즈베리파이의 ID값이 서로 같다면   
서로 네트워크를 할 수 있다고 하는 거 같다

파일을 열고 확인을 해보면 
```
vi ~/.bashrc
```
아래줄을 보게되면 이미 export ROS_DOMAIN_ID=30 #TURTLEBOT3 로 입력이 되어 있다  

> 기본 ROS_DOMAIN_ID는 30으로 설정되어 있으므로 다르게 변경하려면 바꿔주고   
Remote PC와 라즈베리파이를 같게 맞춰준다 

이를 DDS communication이라고 하는 듯하다. ROS2에서는 ros처럼 TCP/IP 방식을 사용하지 않는다고 한다  
기존의 ROS의 publish-subscribe 방식과 비슷하게 publish-subscribe를 제공한다고 한다  
DDS는 요청-응답(request-response)류의 통신방식 있는데 ROS의 서비스 시스템(service system)과 비슷하다   
2개 DDS 프로그램은 ROS master와 같은 툴이 필요없이 통신할 수 있게 해준다고 한다

일단 ROS와 ROS2에서 그런 차이를 보이는 것 같다  
일단 ROS_DOMAIN_ID를 ID를 동일하게 해서 ip를 입력하지 않고도  
turtlebot3과 원격PC에서 서로 topic을 주고 받을 수 있게 되는 것 같다

> 터틀봇3 e메뉴얼에서도 말하고 있는데 ROS_DOMAIN_ID를 같은 네트워크 상에서는    
다른이들과 같은 ID를 사용하지말라고 되어 있다.   
같은 네트워크 망에서는 커뮤니케이션 충돌이 발생할 수 있다고 한다  

[The ROS_DOMAIN_ID 관련 페이지](https://docs.ros.org/en/foxy/Concepts/About-Domain-ID.html)


## localhost 사용
환경변수 `ROS_LOCALHOST_ONLY` 를 설정해주면 된다.

```
export ROS_LOCALHOST_ONLY=1
```

bashrc 파일에 저장하려면 파일을 열어서 위의 내용을 복사 또는 리다이렉트로 바로 복사
```
echo "export ROS_LOCALHOST_ONLY=1" >> ~/.bashrc
```

**>>** 두 개를 사용해야함. 한 개는 파일을 통채로 덮어씌우므로 주의




