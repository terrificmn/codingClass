# cmake 시 에러
```
CMake Error at /usr/share/cmake-3.10/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find GTest (missing: GTEST_LIBRARY GTEST_MAIN_LIBRARY)
Call Stack (most recent call first):
```

gtest를 설치를 해줘야하는데 이미 설치가 되어있을 수도 있다 
```
sudo apt install libgtest-dev cmake
```

다시 cmake 시도
```
cd ~/BehaviorTree.CPP/build
cmake ..
```

같은 에러가 발생한다면 gtest를 다시 빌드해준다 
```
cd /usr/src/gtest
sudo cmake CMakeLists.txt
sudo make
```
그리고 .a 파일을 복사 하거나 심볼릭 링크를 걸어주는데 일단 cp를 해줬다 
```
sudo cp *.a /usr/lib/
```

이제 다시 cmake 를 해보면 잘 된다 

