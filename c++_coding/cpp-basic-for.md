# for문

다행히 C++ for문은 php와 비슷하기 (거의 똑같다 ㅋㅋ) 때문에 꽤 친숙(?)하다 

i값이 증가되는 for문 방식을 살펴보자~

시작하기 전에 파이썬 같은 경우에서는 리스트에서 바로 하나씩 빼오는 방식으로 처리를 해주기 때문에 
c언어 형식은 잘 안 사용했던 것 같다.

파이썬에서는 
```cpp
animals = ["dog", "cat", "turtle"]

for animal in animal:
    print(animal)
```
위 처럼 편했던 것 같다. 

물론 i 값을 줄 수도 있다. for i, animal in enumerate(animals) : 처럼도 쓸 수 있다 
  
C++ 배우는 데 서론이 너무 길었다;; 갑자기 파이썬을 😅   
(사실 안 까먹을려고 한번 더 써봤다 ㅋㅋ)

<br>

## C++ for문 시작하기

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
c++ 에서는 배열에 값을 넣어줄 때 { }중괄호를 (curly brackets) 사용해서 입력한다

**for (초기값; 조건; 증가)** 처럼 사용이 되며,

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

