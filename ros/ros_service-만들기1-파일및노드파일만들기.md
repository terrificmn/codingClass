# service 통신 만들기 튜토리얼 1
저번의 ROS의 topics 통신 이후에 service 통신에 대해서 배웠다  
다음에 다시 한번 기억하기 위해서 튜토리얼을 작성했다~

[ROS topic 통신 튜토리얼 보러가기](/tag/catkin_create_pkg)

[ROS topics, services and actions 알아보기](http://54.180.113.157/blog/ROS-topics-services-and-actions-%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90)

<br>

## 먼저 패키지를 만들어 주자
catkin workspace의 src 디렉토리로 이동을 하자

```
$ cd ~/catkin_ws/src
```
그리고 나서 패키지를 만든다

여기에는 catkin_create_pkg 다음에는 [패키지명] [의존성패키지1] [의존성패키지2] [의존성패키지3] [etc...]

```
$ catkin_create_pkg yh_tuto_service message_generation std_msgs roscpp
```

패키지명은 yh_tuto_service로 만들었고 뒤에 오는 것들은 필요한 패키지가 된다

패키지 파일이 만들어진다. 

다음은 srv (서비스) 디렉토리를 만들고 이동해서 파일을 만들자
```
$ mkdir srv && cd srv
$ vi yh_srv.srv
```

파일이 만들어지고 열리면 아래의 내용을 넣어준다

```
int64 a
int64 b
---
int64 result
```

위의 내용은 ---로 구분이 되어 지는데   
---의 윗부분은 Request가 되어질 때 사용되는 변수를 적어준다  
그리고 --- 기준 아래는 Response가 된다

이제 상위 디렉토리의 src 디렉토리로 이동해서 2개의 노드를 만들어 주는데  
각각 server와 client를 노드가 된다

편한 에디터로 편집을 해준다. 개인적으로는 vscode 추천를 합니다 🤩 

파일은 현재 패키지인 yh_tuto_servicec 안의 src 디렉토리 안에 만들어 주면 된다  
각각 srv_server.cpp, srv_client.cpp로 만들어 준다

<br>

## 먼저 srv_server.cpp 노드 만들기

먼저 전체 코드~

```cpp
#include "ros/ros.h"
#include "yh_tuto_service/yh_srv.h"

// 패키지이름::서비스이름::Request 참조연산& 변수
// srv 디렉토리의 yh_srv.srv 파일의 변수들을 참조하게 된다
bool calculation(yh_tuto_service::yh_srv::Request &req, yh_tuto_service::yh_srv::Response &res) {

    res.result = req.a + req.b;

    ROS_INFO("request : x= %ld, y = %ld", (long int)req.a, (long int)req.b); //%ld 는 long int
    ROS_INFO("sending back response : %ld", (long int)res.result);

    return true;  //리턴을 bool 로 선언했음
}

int main(int argc, char **argv) {
    ros::init(argc, argv, "srv_server");
    ros::NodeHandle nh;

    ros::ServiceServer server = nh.advertiseService("hamburger", calculation); //service에서는 advertiseService()를 사용,이하 문자열은 서비스명

    ROS_INFO("ready srv server!!");

    ros::spin(); // 응답이 있을 때까지 계속 spin()함수에서 들어가 있게 됨

    return 0;
}
```
저장을 하자~

서버에서는 클라이언트 요청이 있으면 a, b 변수로 받아서 그 값을 더해서 client에게 
result에 넣은 값을 보내주고 출력해주는 프로그램이다

<br> 

짧게 끊어서 보면은 내용을 확인해 보자!

```cpp
#include "ros/ros.h"
#include "yh_tuto_service/yh_srv.h"

// 패키지이름::서비스이름::Request 참조연산& 변수
// srv 디렉토리의 yh_srv.srv 파일의 변수들을 참조하게 된다
bool calculation(yh_tuto_service::yh_srv::Request &req, yh_tuto_service::yh_srv::Response &res) {

    res.result = req.a + req.b;

    ROS_INFO("request : x= %ld, y = %ld", (long int)req.a, (long int)req.b); //%ld 는 long int
    ROS_INFO("sending back response : %ld", (long int)res.result);

    return true;  //리턴을 bool 로 선언했음
}

```
먼저 실행에 필요한 파일을 인쿠르드 해주고,
yh_toto_service/yh_srv.h 파일은 빌드가 되면 h파일이 만들어 지는데 이것도 사용하므로 
인쿠르드를 해준다

calculation()함수를 만드는 데 리턴 값을 True, False인 값으로 반환하므로 bool로 정의를 해주고

파라미터를 정해주는데 
yh_tuto_service::yh_srv::Request &req, yh_tuto_service::yh_srv::Response &res

처음에 위에서 만든 yh_srv.srv 파일에 정의해둔 Request와 Response로 각각 req, res로 참조연산을 할 수 있게 만들어 준다

res.result에 두 수를 더해서 저장을 해주고

ROS_INFO를 이용해서 터미널에 내용을 출력해준다

<br>

이하 메인함수에서는 

```cpp

int main(int argc, char **argv) {
    ros::init(argc, argv, "srv_server");
    ros::NodeHandle nh;

    ros::ServiceServer server = nh.advertiseService("hamburger", calculation); //service에서는 advertiseService()를 사용,이하 문자열은 서비스명

    ROS_INFO("ready srv server!!");

    ros::spin(); // 응답이 있을 때까지 계속 spin()함수에서 들어가 있게 됨

    return 0;
}
```
이제 메인 함수에서는 
ros::init을 해주고, ros::NodeHandle nh로 만들어 준다
nh로 advertiseeService로 서비스명을 만들어주고 calculation함수를 호출할 수 있게 해준다

클라이언트에서 요청이 없다면 spin()함수에 들어가져서 
ready srv server 만 표시를 해주고 있게 된다


<br>

## 그리고 이번에는 client 노드도 만들자

client.cpp 파일에서는 서비스 클라이언트를 마찬가지로 yh_srv를 사용해서 만들고 

```cpp
#include "ros/ros.h"
#include "yh_tuto_service/yh_srv.h"
#include <cstdlib>  //atoll() 함수를 사용하기 위해서 인쿠르드

int main(int argc, char **argv) {
    ros::init(argc, argv, "srv_client");
    
    if (argc != 3) { // 사용자가 입력값이 안 들어왔을 때 안내 메세지 띄움
        ROS_INFO("cmd: rosrun yh_tuto_service srv_client arg0 arg1");
        ROS_INFO("arg0 : double number, arg1 : double number");

        return 1;
    }
    
    ros::NodeHandle nh;

    ros::ServiceClient client = nh.serviceClient<yh_tuto_service::yh_srv>("hamburger"); //serviceClient를 선언
    // < 안에 자료형이 들어간다 >

    yh_tuto_service::yh_srv srv;  //srv를 만들어 줌
    srv.request.a = atoll(argv[1]);  //입력되는 값을 분리해서 넣어주는 함수
    srv.request.b = atoll(argv[2]);  

    if (client.call(srv)) {  //srv를 요청하는 곳 
        ROS_INFO("send srv, srv.Request.a and b : %ld, %ld", (long int)srv.request.a, (long int)srv.request.b);
        ROS_INFO("receive srv, srv.Response.result : %ld", (long int)srv.response.result);
        
    
    } else {  //에러처리
        ROS_ERROR("Failed to call service"); //에러표시를 빨간색으로 해줌
        // call이 제대로 안되는 경우는 server노드가 작동을 안하고 있거나
        // client에서 서비스명을 제대로 입력을 못했을 경우에 여기 else문에 들어오게 된다
        return 1;
    }
    return 0;

}
```
if (argc != 3) { } 부분에서   
클라이언트에서 실행을 할 때에 파라미터를 2개를 안 넘기게 되면은 
에러가 나게 되어 있다.

그래서 에러가 발생했을 시에 예외처리로 안내 메세지를 출력해주게 되는 코드이고,

추후 rosrun으로 실행할 때 파라미터로 숫자를 2개 넘기게 되는데   
이때 값을 atoll(argv[1])를 이용해서 값을 srv.request.a 와 srv.request.b로 각각 넣어준다

중간에 client.call(srv) 부분에서 요청이 시작되면서 요청이 있다면 
값을 보냈다고 출력을 하고, 

server 쪽에서 계산 한 결과를 넘겨주는데 이게 
srv.response.result에 들어가므로 결과값을 받아서 출력해주는 노드이다  

파일들을 모두 저장하고 빌드를 하기 위해서 준비를 하자~

이제 다음 단계로

[ROS service 통신 만들기 튜토리얼 2 (CMakeLists파일 수정)](/blog/) 수정해야함

