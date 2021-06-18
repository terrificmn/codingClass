# ros 명령줄 인수에 대해서 알아보자
ROS에서 사용하는 main함수에서 인수에 대해서 알아보자~

```cpp
int main (int argc, char** argv) {
    //....생략
}
```
으로 시작을 하는데 메인함수의 파마리터가 2개가 있다, argc와 argv  
argc는 몇 개를 입력 받음을 숫자로 알 수가 있고,
argv는 문자열로 입력된 값을 받는다   

이를 명령줄 인수라고 부른다. 또는 명령어 옵션이라고도 한다   
rosrun을 명령을 할 때 인수를 넘긴다고 해서 그렇게 부르는 듯하다. 

ros에서 노드 실행은 rosrun [패키지명] [노드명] 으로 하는데

이렇게 입력을 하면 노드가 실행되면 메인 함수에서 argc, argv를 받게 되는 것을 말한다

이제 노드(예: main_test_param.cpp)에 코드를 작성하자
```cpp
#include <ros/ros.h>
#include <iostream>
using namespace std;

int main (int argc, char** argv) {
    ros::init(argc, argv, "main_test_param");
    ros::NodeHandle nh;

    cout << argc << endl;

    return 0;
}
```

> 먼저 패키지를 만들어야하고, CMakeLists.txt 파일과 catkin_make로 빌드를 해줘야한다


[ros 패키지 만들기 튜토리얼 보러가기](/tag/catkin_create_pkg)

이제 실행을 해보자. 예를 들어서 이런식으로 만들었다고 하면 (rosrun 패키지명 노드명)
```
$ rosrun main_test main_test_param
```

노드명까지 제대로 입력이 되었으면 argc는 int로 몇개가 인수로 입력이 되었는지를 받는데
위 처럼 하면 결과는
```
1
```
이라고 나온다

일단 기본값이 **1** 이라는 것을 알 수 있다.

이번에는 아규먼트(인수) 값을 넘겨보자

> 노드명 뒤로 스페이스바를 기준으로 하나씩 하나씩 값을 넘겨줄 수가 있다

아래처럼 10이라는 숫자를 넘기면서 rosrun을 실행해보자


> arguments 아규먼트는 인수를 뜻하며, 함수에 정의된 파라미터 (인자) 변수 값들에 해당하는 값을   
넘겨주는 것을 말하는데, 파라미터는 함수에서 정의된 것을 표현할 때 그렇게 말하고   
함수를 호출하는 부분에서 즉 데이터를 주는 부분에서는 arguments 인수라고 한다 (구별해놓음)  
정리하면 아규먼트==인수, 파라미터==매개변수==인자  
즉, 그놈이 그놈이다. 


<br/>

```
$ rosrun main_test main_test_param 10
```
이라고 입력해보면 결과는 
```
2
```
그래서 만약에 노드에서 뭔가 파라미터를 받아서 처리해야한다고 할 때면   
그 수를 **+1** 을 해서 생각을 해주면 된다.

이번에는 2개를 넘겨보자
```
$ rosrun main_test main_test_param 10 20
```

이렇게 한 후 실행을 해보면 2개를 넘겼고 +1이 되어서 

```
3
```
이렇게 나오게 된다

<br/>

서버에서 2개의 파라미터를 받아야 하는 상황이라고 하면   
예를 들어서 클라이언트에서 숫자 2개를 받아서 서버에 요청을 한다고 하면   
(그래서 서버에서는 두 수를 더한 값을 응답해준다 라는 그런 프로그램이라면)

그렇다면은 인수값을 2개만 입력을 받게 해줘야하는데 argc 변수를 이용해서 코드를 짤 수가 있다

```cpp
#include <ros/ros.h>
#include <iostream>
using namespace std;

int main (int argc, char** argv) {
    ros::init(argc, argv, "main_test_param");
    ros::NodeHandle nh;

    if (argc != 3) { // 사용자가 입력값이 안 들어왔을 때 안내 메세지 띄움
        ROS_INFO("cmd: rosrun main_test main_test_param arg0 arg1 ");
        cout << argc << endl;
        return 1;
    }
    
    return 0;
}
```
빌드를 하고   
이제 main_test main_test_param 10 이렇게만 입력하면 argc는 2가 되고 3이 아니므로 
위의 안내 메세지가 뜨게 된다. 마찬가지로 argc가 3 (즉 2개) 보다 큰 인수를 입력해도 결과는 
마찬가지 3이 아니므로 안내를 하고 종료를 하게 된다

> 위의 메세지는 프로그램을 실행하다보면은 뭔가 명령어를 잘못 쳤을 때 안내 메세지가 나온는데 
위의 안내도 인수(arguments)를 몇개까지 쓰라고 나오게 해주는 것이다
에러가 안 나게 안내를 해주고 종료가 되므로 꿀팁 예외처리인 것 같다

<br/>

## 이번에는 ros main함수에서의 argv를 알아보자

```cpp
#include <ros/ros.h>
#include <iostream>
using namespace std;

int main (int argc, char** argv) {
    ros::init(argc, argv, "main_test_param");
    ros::NodeHandle nh;
    
    cout << argv << endl;
    cout << argv[0] << endl;

    return 0;
}
```
catkin_make를 한 후에 프로그램을 돌려보면

```
$ rosrun main_test main_test_param
```
그냥 실행만 했다. 결과는 

```
0x7ffcedbb5be8
/root/catkin_ws/devel/lib/main_test/main_test_param
```
즉 argv는 포인터이므로 주소값을 가지고 있고
그 첫번째 0번째에는 디렉토리 인것을 알 수 있다

이번에는 프린트를 argv[1]을 추가해보고 빌드 후 다시 실행을 해보자
```cpp
cout << argv[1] << endl;
```

```
$ rosrun main_test main_test_param 10
```
결과는 예상 하듯이

```
0x7ffcedbb5be8
/root/catkin_ws/devel/lib/main_test/main_test_param
10
```

숫자를 입력을 해도 문자열로 받기 때문에 10이라는 값을 출력함

이제 1번째가 파라미터 값이 들어 있는 것을 알았으므로  
이제 이를 응용해서 atoll 이라는 함수를 사용해서 서비스 클라이언트를 만들 때
각각 변수에 저장을 해줄 수가 있다. 

그래서 이를 사용한 예는
```cpp
// atoll을 사용하려면 인쿠르드해야함
#include <cstdlib>

... 생략
 srv.request.a = atoll(argv[1]);  //argv로 들어온 값을 문자열로 받아짐 // request.a 에 저장
 srv.request.b = atoll(argv[2]);
```
주석에 설명되어 있듯이 cstdlib를 사용해서 atoll() 함수를 사용할 수 있고
argv로 들어온 것을 atoll()함수를 사용해서 long int 형으로 변환해주는 역할을 한다

> service의 srv파일이 int64로 되어 있어서 그렇다 


만약 파라미터가 int가 아닌 double로 선언되어 있다면 
소수점으로 입력을 하더라도 이것도 마찬가지로 문자열로 받아진다    
이번에는 stod() 함수를 사용할 수 있다. 문자열로 받은 값을 double형으로 바꿀 수가 있다

```cpp
double param1 = std::stod(argv[1]);
```
<br/>

이와 비슷한 문자열 변환 함수는 아래의 함수를 사용하면 된다


| 함수 | 내용 |
| -- | -- |
| std::stof()  | 문자열을 float형으로 변환  |
| std::stold() | 문자열을 longdouble형으로 변환  |
| std::stoi() | 문자열을 int형으로 변환  |


끝!