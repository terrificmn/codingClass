## cmake 빌드 에러
g++ 등의 필수 빌드 라이브러리가 없을 경우에 발생   
```
CMake Error at CMakeLists.txt:2 (project):
  No CMAKE_CXX_COMPILER could be found.

  Tell CMake where to find the compiler by setting either the environment
  variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
  to the compiler, or to the compiler name if it is in the PATH.
```

gcc만 설치한 상태에서 아무래도... 에러가 발생하는 듯..   

```
sudo dnf groupinstall "C Development Tools and Libraries"
```
로 설치해주면 cmake를 무리없이 할 수가 있다.

