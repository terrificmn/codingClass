# CPP c++에서 do-while 과 while문

먼저 do-while과 while 반복문의 큰 차이점이라고 하면 do while문은 일단 조건과 상관없이 
하나의 코드는 실행을 하게 된다.

간단하게 예로 정리해보았다

```cpp
#include <iostream>
using namespace std;  

int main() {
    
    int count = 0;

    cout << "do while문" << endl;

    do {
        cout << count << endl;
        // 뭔가 빠짐
    } while (count <= 10);
}
```

> 참고로 cout은 출력을 해주고 << 기호와 함께 사용을 한다 


일단 while문에서 조건을 넣어주는데 count <= 10 
이 조건에 의해서 반복문이 실행이 되게 된다. 
위의 코드는 count 변수를 값을 늘려주는 코드가 없으므로 무한루프에 빠지게 된다

```
0
0
0
0
0
0
...

```
그래서 while문에서는 조건 값을 변경시켜서 빠져나갈 수 있게 만들어 줘야한다

```cpp
    int count = 0;

    cout << "do while문" << endl;

    do {
        cout << count << endl;
        count++;
    } while (count <= 10);
```
위 처럼 count++을 해주면 count값이 한번 반복을 할 때마다 +1 되어서 증가하게 된다
그래서 결국 카운트가 11이 되었을 때 while문의 조건이 10보다 크게 되므로 
while문을 빠져나가게 된다.

만약 count 값을 11이라고 넣어 준다면
```cpp
    int count = 11;

    cout << "do while문" << endl;

    do {
        cout << count << endl;
        count++;
    } while (count <= 10);
```

아예  while문의 조건에 false 이므로 반복문 자체를 수행을 안하게 된다. 하지만 do while문은
처음 do 블럭에 있는 코드는 처음에 실행을 하게 된다.
그래서 
```
do while문
11
```
조건과 상관 없이 출력을 한번 하게 된다는 점이 do while문의 큰 특징이다

<br>

# while문

간단하게 살펴보면 

```cpp
#include <iostream>

using namespace std;

int main() {
    
    int count = 0;
    cout << "while문" << endl;

    while (count <= 10) {
        cout << count << endl;
        count++;
    }
}
```

do while 문에서 do만 빠진 상태이고, count값이 0이므로 조건이 true여서
반복문을 실행한다음에 빠져나가게 된다.

만약 do while문에서 했던 것 처럼 count에 11이라는 값을 넣어 주게된다면
while문은 아예 시작도 안하게 된다.



