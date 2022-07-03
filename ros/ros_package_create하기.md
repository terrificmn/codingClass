# ROS 패키지 만들기 - Topics 통신 하기

Need to make a catkin_workspace which is catkin_ws
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```
then catkin_ws/src dir has been created and build, devel directories as well

먼저
이동 catkin_ws 의 src 디렉토리 까지 이동을 하자

```
$ cd ~/catkin_ws/src
```

패키지를 만들자. 패키지를 만들려면 catkin_create_pkg 라는 명령어를 쓰고   
그 다음에 들어가는 것은 패키지명이 되고 그 다음부터는 의존성 패키지를 의미하게 된다  

예: catkin_create_pkg [패키지명] [의존성패키지1] [의존성패키지2] [의존성패키지3]

```
$ catkin_create_pkg yh_tutorial message_generation std_msgs roscpp
```

그러면 아래 처럼 표시가 되면서 만들어 진다.
```
Created file yh_tutorial/package.xml
Created file yh_tutorial/CMakeLists.txt
Created folder yh_tutorial/include/yh_tutorial
Created folder yh_tutorial/src
Successfully created files in /home/ubun/catkin_ws/src/yh_tutorial. Please adjust the values in package.xml.
```

패키지가 생기면서 yh_tutorial 이 생긴다  

위에 나온 메세지 처럼 그 안에는   
기본적으로 CMakeLists.txt, package.xml 파일 2개와 include, src 디렉토리가 각각 생긴다

여기에 생긴 CMakeLists.txt 파일은 현재 yh_tutorial 패키지의 노드들에 대한 패키지를 만들기 위한 설계도면이라고 볼 수 있다
즉, catkin 빌더가 이 안에 있는 노드 들을 패키지를 빌드 할 때 사용하게 된다.

include 디렉토리에는 포함시킬 header파일이 들어 있다

package.xml 안에는 버전, 작성자(maintainer), 설명 들이 간략하게 되어 있고   
xml파일 형식으로 되어 있고

<br>

> 잠깐만 XML? Extensible Markup Language 이며 확장가능한 마크업 랭귀지  
소프트웨어와 하드웨어 간에 데이터를 저장하고 전송하기 위해서 사용된다. 그래서 사람과 기계가 읽기 쉽게 만들어 졌다  
마크업 랭귀지 이기 때문에 HTML 과 비슷하고 <태그>를 이용하고 </태그>로 닫는 식으로 사용이 된다.  
다른점은 XML은 데이터 전송에 초점이 맞춰져 있어서 데이터를 보여주기 위한 HTML과는 다르다고 할 수 있다

<br>

그리고 의존성 관련 패키지 목록이 되어 있다.   

참고로 build_depend태그에 message_generation 한번 만 나오는 이유는 빌드 할 때 한번 만 실행해서 만들어지면 되기 때문이라고 한다

<br>

## msg 디렉토리와 msg파일 만들기 (topic과 관련된 파일)
현재 경로를 다시 리마인드
```
$pwd
```
현재 경로는 /home/ubun/catkin_ws/src/yh_tutorial

에서 그대로 msg 디렉토리를 만들어 주고 이동을 하자
```
$ mkdir msg && cd msg
```
msg 디렉토리는 topics 를 이용한 통신을 하기 위해서 만들어 주는 것인데  
ROS에서는 topic 통신이 기본이어서 이름을 msg로 만들어 준다

> 참고로 srv, action 같은 디렉토리도 만들어 줄 수 있는데, 각각 service, action을 위한 통신 노드를 의미한다

<br>

[파일이름].msg 파일을 만들어 준다 (파일 이름은 변경 가능)
```
$ vi yh_msg_tutorial.msg
```

이 yh_msg_tutorial.msg 파일 열어서 아래의 변수를 적어준다
```
time stamp
int32 data
```
변수 stamp, data를 선언하고, 타입을 각각 time, int32 로 적어준다

[ROS 타입 관련해서 위키 확인하기](https://wiki.ros.org/msg)


<br>

# 노드 파일 c++ 파일 코딩하기
yh_tutorial 패키지 안에 있는 노드파일을 만들 차례입니다~ c++ 로 만듭니다

이제 msg 디렉토리에서 나와서 src 디렉토리로 이동해준다
```
$ cd ../src
```

이제 2개의 cpp파일을 만들어 준다. 이는 각각 node가 된다 (즉 2개의 노드)

하나는 pub_test.cpp 로 만들고 
두번째는 sub_test.cpp 파일을 만들어 준다

원하는 에디터를 열어서 편집을 해준다 
(현재 경로 확인 /home/ubun/catkin_ws/src/yh_tutorial/src)

vscode가 편하니 vscode로 코딩을 하자~ 원하는 에디터로 열면 된다
```
$ code pub_test.cpp
```

아래 내용을 입력 하면 된다. copy & paste
```cpp
#include "ros/ros.h" //ROS 기본 헤더파일 추가하기 - 기본 함수들을 사용하기 위해서
#include "yh_tutorial/yh_msg_tutorial.h" // 패키지 이름/메세지파일이름.h 
// msg 디렉토리에 있는 yh_msg_tutorial.msg 파일인데 빌드를 하면 자동으로 h 파일이 생성이 된다

int main(int argc, char **argv) {
    ros::init(argc, argv, "pub_test");  // 위의 ros.h 파일을 가져왔기 때문에 ros를 사용할 수 있다
    // init()으로 노드명을 초기화 해준다
    
    ros::NodeHandle nh; // ROS 시스템과 통신을 위한 노드 핸들을 nh 로 만들어 준다

    // 퍼블리시어 선언, [패키지명] 즉, yh_tutorial 의 [메시지파일] 즉, yh_msg_tutorial을 이용해서
    // 퍼블리시어 작성한다. pub 으로 작성
    // 토픽명은 > "yh_topic", 퍼블리시어 큐 사이즈를 100 개로 설정
    ros::Publisher pub = nh.advertise < yh_tutorial::yh_msg_tutorial >("yh_topic", 100);
    // yh_tutorial(패키지명)::yh_msg_tutorial(msg의 파일명) > 이하는 topic명을 정해준다, 100개의 que를 만들어 준다
    
    ros::Rate loop_rate(10); // 루프 주기를 10Hz로 설정 (1초에 반복되는 횟수) : 루프 한번이 0.1초에 한번 돌아간다

    yh_tutorial::yh_msg_tutorial msg;  //yh_tutorial의 yh_msg_tutorial 의 내가 만든 메시지 파일 형식으로 msg를 선언해준다

    int count = 0;

    while(ros::ok()) { // ros가 실행이 되면 ok()가 활성화가 된다.
        msg.stamp = ros::Time::now();  //현재 시간을 msg 객체의 stamp에 저장
        msg.data = count;   //count값을 msg객체의 data 에 저장

        ROS_INFO("send msg = %d", msg.stamp.sec);  // ros의 prinft 함수 
        ROS_INFO("send msg = %d", msg.stamp.nsec); //Time::now()에서 받아온 시간이 .sec .nsec 이 있으므로 붙여준다
        ROS_INFO("send msg = %d", msg.data);

        pub.publish(msg);  //publish() 함수로 메세지를 발행한다
        loop_rate.sleep();
        ++count; // 0.1초에 한번 루프가 돌아서 1초면 카운트가 10 올라간다
    }

    return 0;
}
```
저장 하고 빠져 나온다, 자세한 내용은 주석을 참고해보자~

vscode가 열려있다면 그냥 옆에서 아이콘 눌러서 만들자 ㅋㅋㅋ
구지 터미널로 하려면
```
$ code sub_test.cpp
```

아래의 내용 저장하기
```cpp
#include "ros/ros.h";
#include "yh_tutorial/yh_msg_tutorial.h";

void msgCallback (const yh_tutorial::yh_msg_tutorial::ConstPtr&msg) { // 파라미터를 상수 형태로 끊어서 사용하겠다
    ROS_INFO("received msg = %d", msg -> stamp.sec); //출력
    ROS_INFO("received msg = %d", msg -> stamp.nsec);
    ROS_INFO("received msg = %d", msg -> data);
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "sub_test"); //ros 초기화 하면서 노드명을 만들어 준다
    ros::NodeHandle nh; //NodeHandle 을 nh로 만들어 준다 . 현재 노드에 해당한다

    //Subscriber 이용해서 sub 객체로 만들어 준다
    //nh.subscribe() 을 사용해서 서브스크라이드를 해주는데 topic은 yh_topic 으로 해준다
    // msgCallback을 호출한다
    ros::Subscriber sub = nh.subscribe("yh_topic", 100, msgCallback);

    ros::spin();
    // spin() 함수는 publisher에서 메세지가 있을 때까지 기다린다

    return 0;
}
```

이로서 2개의 노드 파일이 완성이 되었다.  
첫 번째 pub_test.cpp 파일은 publisher 가 되고,   
두 번째 sub_test.cpp 파일은 subscribe 가 된다

msg 디렉토리에 만들었던 yh_msg_tutorial 은 topic으로   
같은 topic이어야지 publisher가 보내주는 내용을 subscribe 쪽에서 받을 수 있다

그래서 pub_test.cpp 내용에 보면 
```cpp
ros::Publisher pub = nh.advertise < yh_tutorial::yh_msg_tutorial >("yh_topic", 100);
```
yh_tutorial 패키지의 yh_msg_tutorial topic을 사용하게 된다고 되어 있다


<br>

[ros 패키지 만들기 및 topic 통신 하기 - 튜토리얼 2 보러가기 ](/blog/)

