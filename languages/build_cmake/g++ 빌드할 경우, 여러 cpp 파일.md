## g++ build
g++을 이용해서 빌드를 할 때 main.cpp 외에 다른 cpp파일을 같이 컴파일 할 경우에는 파일명을 같이 적어주면 된다.  vscode에서 지정하는 법은 좀 찾아봐야할 듯.. 전에 해봤던 거 같기도;; 한데;;

클래스를 따로 만들어서(파일로) main 에서 include 한 상태에서 빌드를 하려고 했더니 계속 에러가 발생한다. 그래서 삽질;;;;

```
in function `main':
main.cpp:(.text+0x24): undefined reference to `TestA::TestA()'
```

다른 클래스를 찾지를 못한다.. 왜 빌드 자체를 못했으므로 

어째듯 main.cpp 에서 test_a.cpp 같이 다른 파일도 같이 빌드해주면 된다 (test_a.h 파일도 include한 경우), ...

```
g++ main.cpp test_a.cpp, test_b.cpp, test_c.cpp -o main_test
```

> -o 옵션은 output 파일이 된다

이런식으로 해 주면 잘 컴파일이 된다 


## 파일 버전 명시하기
std::filesystem 같은 류를 사용하려면 c++17 이상부터 가능하다. 그래서 그냥 g++로 빌드하면 에러가 발생   
```
g++ -std=c++17 -o symlink symlink.cpp
```
