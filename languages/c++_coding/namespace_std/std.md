# cpp의 namespace
c++ 네임스페이스에 대해서 공부해보았다  
그리고 std를 네임스페이스로 사용할 때의 주의점(?)도 공부해봄

먼저 간단한게 age라는 변수를 만든다고 하면
```cpp
#include <iostream>
using namespace std;

int main() {
    int age = 25;
    int age = 30;
    
}
```

변수를 사용할 때 위 처럼 하게 되면 변수를 같은 이름으로 했으므로   
‘int age’ previously declared here 라는 에러가 발생한다

네임스페이스를 사용해보자. 사용하는 방법은 아래 처럼 하면 된다

```cpp
#include <iostream>

namespace namespace25 {
    int age = 25;
}

namespace namespace30 {
    int age = 30;
}

int main() {
    
    std::cout << namespace25::age << std::endl;

}

```
namespace 원하는네임스페이스이름 { } 식으로 만들어주면   
같은 이름의 변수를 네임스페이스로 사용할 수가 있게된다.  
그래서 위의 경우에는 namespace25라고 만들어준 것에서  
age라는 멤버로 만들어졌으므로   
어떤 네임 스페이스의 멤버를 특정해서 사용할 수가 있게 된다  
그래서 namespace25, namespace30의 age라는 변수를 각각 사용할 수가 있게 되고  
충돌이 나지 않게 된다.

사용방법은   
namespace25 이후 :: (콜론2개)을 붙여서 사용할 수 있다  

vscode같은 에디터를 사용하면 :: 이후는 자동으로 완성이 되는 모습을 확인할 수 있다.   

<img src=0>
<br/>

위의 프로그램을 실행해 보면 결과는 
```
25
```
로 잘 출력됨을 알 수 있다

<br/>

## std 네임스페이스의 오해(?)
```
using namespace std;
```
위에서도 사용을 했었지만 std를 네임스페이스로 사용을 한다고 선언을 한 후 
사용을 많이 하게 되는데

> 사실 편하니깐 많이 사용하게 된 듯

이렇게 선언을 하게 되면 std에 속해있는 멤버들을 쉽게 사용을 할 수가 있는데  

예를 들어서 string으로 변수를 선언할 수가 있다. 
원래는 std::string 이런식으로 사용을 해야하나   
그냥 string만 적어도 사용이 가능해진다

하지만 이렇게 사용하는 방법이 그렇게 추천할 만한 방법은 아니라고 한다

왜냐하면 std라는 것에는 엄청 많은 멤버들을 포함하고 있는데 이를 다 사용하게 된다고 한다

참고:

<img src=1>
<br/>


먼저 using namespace std; 을 제거해 보자  
이렇게 하게 되면 cout (출력), string (선언) 등에서 에러가 발생하게 된다  

왜냐하면 위의 멤법들은 std에 속해있는데 cout, string 로 바로 사용하게 되면   
마치 누구신지? 하고 알 수가 없게 되는 것

그러면 아래 처럼 선언한다면
```cpp
std::string
std::cout 
```
같은 방식으로 지정을 해주면 에러가 나지 않고 
std에 속해있는 string이나 cout의 주소값을 잘 알고 있어서
이상없이 작동하게 된다

std 네임스페이스를 이용해서 특정 멤버만 사용하게 선언하게 할 수 있다
코드 예:
```cpp
#include <iostream>
using std::cout;

namespace namespace25 {
    int age = 25;
    std::string name = "Tim";
}

namespace namespace30 {
    int age = 30;
}

int main() {
    
    cout << namespace25::age << std::endl;
    cout << namespace25::name << std::endl;
}
```

using std::cout 으로 첫 줄에 선언을 해 줌으로써 
main() 함수에서 cout만 사용을 해도 문제없이 작동을 하게 된다

하지만 string, endl 는 사용한다고 선언을 안 했으므로 
사용할 때 std::string, std::endl 식으로 일일이 적어줘야한다

이제 string, endl 같은 멤버도 같은 방식으로 선언을 해주면 std없이 사용할 수 있게 된다

```cpp
#include <iostream>
using std::cout;
using std::endl;
using std::string;

namespace namespace25 {
    int age = 25;
    string name = "Tim";
}

namespace namespace30 {
    int age = 30;
}

int main() {
    
    cout << namespace25::age << endl;
    cout << namespace25::name << endl;
}
```
위에 처럼 std 빼고 사용할 수 있게 되어서 string, cout, endl 만 사용해서 사용할 수가 있게 된다

<br/>

## using namespace std; 는 비추
위의 코드에서는  
네임스페이스로 만들어놓은 namespace25 에는 age와 name이 있고  
namespace30 에는 age가 있다

마찬가지로 std에는 엄청 많은 멤버들이 있는데 std를 네임스페이스로 사용하게 되면 
많은 멤버를 다 포함하게 되게 된다~

std 를 확인하게 되면 엄청 많은 멤버들이 있는 것을 알 수 있고
이 모든 것을 include하게 되고, 모든 멤버에 접근할 수 있게 하는 것은
좋은 방법이 아닐 수도 있다  

그래서 namespace가 어떤식으로 사용되는 아는게 중요하다고 한다

물론 using std::string 같은 식으로 일일이 적어주면 벌써 3줄이 소요되었고
std만 사용하면 1줄로 끝나서 어떻게 보면 더 편할 수도 있겠지만

사실 그냥 예시라던가 큰 프로그램(?)이 아닌 경우에는 그냥 std를 통채로 사용을 해도
전혀 문제가 안될 것이다

큰 프로젝트나 코드베이스가 많은 프로그램에서는 충돌이나 버그를 유발할 수 있다고 한다
정확히 선언해주면 어떤 멤버를 사용하는지 선언을 했으므로 확실히 알 수가 있을 것이고 

만약 그냥 std를 통으로 사용하게 되면 어딘가에서 에러가 발생해도 어떤 멤버인지 찾기 힘들다던가? 식으로 
상황이 발생할 수 있을 것 같다는 생각을 해보았다

어쨋든 작은 습관이 중요하므로 나름 공부가 된 것 같다.