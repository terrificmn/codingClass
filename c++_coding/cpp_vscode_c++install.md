# vscode 와 C++ 설치
vscode에 C/C++ 를 설치해보자~

먼저 cpp 확장자로 파일을 만들었다면 vscode에서 설치를 하겠냐고 물어본다 (자동 추천)

<img src=0>
<br/>

아니면 왼쪽 블럭모양의 아이콘을 눌러서 검색 또는 추천에 나오는 것을 설치를 해주면 된다

<img src=1>
<br/>

(설치화면이 나오면 install을 눌러주기만 하면 된다)


<br/>

## 설치가 다 되면 이제 hello world를 출력해보자~
먼저 테스트로 cpp 코딩을 할 차례

테스트 디렉토리를 만들고 vscode를 열어준다
```
$ mkdir test
$ cd test
$ code .
```

다음과 같이 간단한 코드를 작성
```cpp
#include <iostream>

int main() {
    std::cout << "Hello World" << std::endl;
    
}
```

<img src=2>
<br/>

이제 터미널(Terminal) 메뉴를 클릭하고 Run Build Task... 를 눌러준다

<img src=3>
<br/>

그러면 여기에서 build task를 해주면 되는데 이 중 2번째 g++ 컴파일러를 선택해준다~  
(컴퓨터에 설치된 것에 따라 다르게 나올 수 있음)

> 첫 번째 cpp 빌드는 실행가능한 파일로 안 만들어져서 불편했음

<img src=4>
<br/>

참고로 g++ 설치되어 있는지 확인은 터미널에 입력해본다
```
$ g++ --version
```
아래 처럼 비슷하게 나오면 설치가 되어 있는 것 
```
g++ (GCC) 8.3.1 20191121 (Red Hat 8.3.1-5)
Copyright (C) 2018 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

> G++, the GNU C++ Compiler is a compiler in Linux which was developed to compile C++ programs.   
G++는 GNU C++ 컴파일러라고 부르는 데 리눅스에서 C++ 프로그램을 컴파일 하기 위해서 만들어진 컴파일러라고 합니다

만약 설치가 안 되어 있으면 설치를 해보자  
우분투 기준으로 (집에서는 우분투를 사용 안하지만 ㅋㅋ 암튼 참고 해주세요 😋)
```
$ sudo apt install g++
```
또는 build-essential 패키지를 설치를 해준다. 
```
$ sudo apt install build-essential
```

자 이제 다시 본론으로 돌아와서 빌드를 실행하게 되면   
바로 왼쪽아래에 빌드가 완료 되었다고 나오고~ (아무키나 누르면 꺼짐)

<img src=5>
<br/>

그러면 왼쪽에 보면 파일이 하나 생겨있는데 실행 가능한 파일이 생성이 된다

<img src=6>
<br/>

이제 실행을 위해서 터미널을 열어주자~  
아니면 vacode 안에서 터미널을 열어도 된다

<img src=7>
<br/>

이제 실행을 시켜보자~ test라고 하면 실행이 안될 수 있으므로 현재 디렉토리를 의미하는 **.**(닷)을 사용하자
```
$ ./test
```

그러면 화면에 **Hello World** 라고 출력이 된다. 이로써 C++로 만든 프로그램이 잘 작동하는 것 확인~ 😊

<img src=8>
<br/>

마지막으로 vscode에서 c++는 자동완성 기능도 지원하니 유용하게 잘 써먹자

<img src=9>
<br/>

<br/>

진짜 마지막으로 리눅스에서는 g++를 컴파일러를 사용하는데 

윈도우에서는 g++이 없기 때문에 MinGW 라는 컴파일러를 다운/설치하면 된다   
(Minimalist GNU - 컴파일러 및 디버거)

맥OS에서는 clang 이라는 툴을 사용하면 된다고 한다

[vscode 매뉴얼 보러가기](https://code.visualstudio.com/docs/languages/cpp)


끝!
