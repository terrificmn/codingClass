## python2, python3 
python 및 python2 를 설치를 했을 때 python3 를 잘 찾지 못하는 에러   

다른 패키지에서 python2 등이 필요 해서 설치를 했더니, catkin build에서 파이썬 3.8 버전을 잘 찾지 못한다.

빌드 시 에러 이하 에러 발생
```
CMake Error at /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:146 (message):
  Could NOT find PythonInterp: Found unsuitable version "2.7.18", but
  required is at least "3.8" (found /usr/bin/python)
Call Stack (most recent call first):
  /usr/share/cmake-3.16/Modules/FindPackageHandleStandardArgs.cmake:391 (_FPHSA_FAILURE_MESSAGE)
  /usr/share/cmake-3.16/Modules/FindPythonInterp.cmake:169 (FIND_PACKAGE_HANDLE_STANDARD_ARGS)
  /opt/ros/noetic/share/catkin/cmake/python.cmake:4 (find_package)
  /opt/ros/noetic/share/catkin/cmake/all.cmake:164 (include)
  /opt/ros/noetic/share/catkin/cmake/catkinConfig.cmake:20 (include)
  CMakeLists.txt:71 (find_package)
```

파이썬을 보게 되면 python2, 2.7, 3.8 등 잘 설치되어 있고, 심링크도 문제 없어 보인다.
```
 ls -l /usr/bin/python*
lrwxrwxrwx 1 root root       7  4월 15  2020 /usr/bin/python -> python2
lrwxrwxrwx 1 root root       9  3월 13  2020 /usr/bin/python2 -> python2.7
-rwxr-xr-x 1 root root 3662000  2월  1 01:23 /usr/bin/python2.7
lrwxrwxrwx 1 root root       9  7월 15 13:52 /usr/bin/python3 -> python3.8
-rwxr-xr-x 1 root root 5490456  3월 25 19:42 /usr/bin/python3.8
lrwxrwxrwx 1 root root      33  3월 25 19:42 /usr/bin/python3.8-config -> x86_64-linux-gnu-python3.8-config
lrwxrwxrwx 1 root root      16  3월 13  2020 /usr/bin/python3-config -> python3.8-config
-rwxr-xr-x 1 root root     384  1월 25  2023 /usr/bin/python3-futurize
-rwxr-xr-x 1 root root     388  1월 25  2023 /usr/bin/python3-pasteurize
```

## 해결 방법은 2가지가 있다.
1. catkin config 에 arg를 추가한다.   

```
catkin config --append-args -DPYTHON_EXECUTABLE=/usr/bin/python3
```

> 그 외에 -DPYTHON_VERSION=3.8 (마찬가지로  --append-args 를 사용하고 이 변수는 크게 도움이 안될 수도 있음)   

catkin build 하게 되면 문제 빌드를 진행한다.


2. 이 방법은 python 버전을 변경 시켜 주는 것 같은데, 심링크만 변경하는 건지 새로 설치하는지  
잘 모르겟다. 이 방법도 가능하다.   
> 하지만 python -> python2 로 사용하는 필요한 상황에서 문제가 발생할 지 모르겠다.

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 3
```
