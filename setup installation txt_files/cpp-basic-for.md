# for문

아무래도 for문은 많이 사용하던거라 꽤 친숙하다  ㅋㅋ

배열을 선언하고 간단하게 배열에 들어가있는 요소를 반복문으로 출력을 해보자

```cpp
#include <iostream>
using namespace std;

int main() {
    string zoo[5] = { "elephant", "zebra", "dolphin", "tiger", "lion"}

    for (int i=0; i < 5; i++) {
        cout << zoo[i] << endl;
    }
}
```

먼저 문자열 배열을 선언해준다. zoo[5]는 5개의 요소를 갖는다는 의미로 선언
c++ 에서는 배열에 값을 넣어줄 때 { }괄호를 사용해서 입력한다

for (초기값; 조건; 증가) 처럼 사용이 되며,

for 문은 역시 c++ 이기 때문에 i 값을 초기화 할때에도 int로 선언을 해줘야하며
이는 for문 내에서만 사용이 가능하게 된다.

그리고 조건이 맞는다면 계속 반복을 하게되는데
한번 반복을 한 후 i 변수는 +1을 시켜주게 된다.

그래서 i가 5가 되면 조건에서 false가 되서 반복문을 빠져나가게 된다

```
elephant
zebra
dolphin
tiger
lion
```

간단하게 정리해 보았다

