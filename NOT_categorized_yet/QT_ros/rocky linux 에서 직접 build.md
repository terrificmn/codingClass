qtcreator-ros를 빌드를 설치하기 위한 dependenceis 이지만..

```
sudo dnf install mesa-libGL-devel ninja-build yaml-cpp-devel utf8proc-devel 
```

Rocky Linux 9.0 이상에서 설치할 경우

```
sudo dnf install mesa-libGL-devel yaml-cpp-devel
dnf --enablerepo=crb install ninja-build
dnf --enablerepo=crb install utf8proc-devel
dnf install libxkbcommon-devel
sudo dnf install cmake g++
sudo dnf install vulkan-loader-devel
sudo dnf install python3-pip
python3 -m pip install pyyaml requests py7zr
```


setup.py를 실행하면  
/tmp/qtc_sdk 에 다운 받은 것들이 압축이풀린다 


```
cmake -B build -GNinja -DCMAKE_BUILD_TYPE=Debug -DCMAKE_PREFIX_PATH="/tmp/qtc_sdk/Tools/QtCreator;/tmp/qtc_sdk/6.4.0/gcc_64"
	cmake --build build --target package

```

호환성 문제로 여러번 빌드하다보면 
```
CMake Error at /tmp/qtc_sdk/Tools/QtCreator/lib/cmake/QtCreator/QtCreatorAPI.cmake:444 (add_library):
  The install of the ROSProjectManager target requires changing an RPATH from
  the build tree, but this is not supported with the Ninja generator unless
  on an ELF-based or XCOFF-based platform.  The
  CMAKE_BUILD_WITH_INSTALL_RPATH variable may be set to avoid this relinking
  step.
```

그래서 여기에 build 디렉토리를 들어가서 안의 파일들을 다 지워준다  

그리고 다시 위의 cmake 명령어를 실행하면 빌드가 잘 된다  

최종적으로 아래처럼 나오면 성공!
```
CPack: - Install project: ROSProjectManager []
CPack: Create package
CPack: - package: /home/sgtocta/ros_qtc_plugin/build/ROSProjectManager-9.1-Linux-x86_64.zip generated.
```

이제 /tmp에 생성된 skd를 전체를 이동시켜준다  

```
cd /tmp
mv qtc_sdk/ ~/
```

qtcreator는 qtc_sdk/Qt/Tool/Qtcreator 에 있음

> PATH 환경 변수를 등록하거나 심볼릭링크를 /usr/bin/ 에 만들어 주면 편하게 사용할 수가 있다

## Ros plugin 등록
Qt creator를 실행을 해서  Help -> About Plugins -> Install Plugin 을 해서 zip파일 통째로 선택해주면 된다 import를 해준다  

New Project를 했을 때 Other Project에서 ROS Workspace를 볼 수가 있다 

완료가 되면 Qt Creator9.0 에 Qt는 6.4 버전이다  



## 의존성 패키지 
~~Could NOT find XKB  XKB 위치를 찾지 못하고, (설치는 되어 있는 듯)~~     
~~Could NOT find WrapVulkanHeaders~~

등의 문제가 있지만 위의 프로그램들 설치하는 것에 해결됨. 만약 추가로 


## dnf 로 설치를 하고 그냥 사용하면 이상 5.15 버전 정도도 호환이 잘 안된다 
dnf 버전이 조금 낮기 때문에 qtcreator 4 버전이다. (Rocky linux 8.5)

```
sudo dnf install qtcreator
```

> rocky linux 8.5 에서는 qt4 버전인가? qtcreator가 4 ? 였는데  
다행히 rocky linux 9.0 이상에서는 dnf 패키지로 했을 때 qt 5.15 정도에  
qt-creator는 7.0 버전 설치되는 듯 하다  
 
 qt 6이상에서 작성한 것은 사용이 안될 수도 있어서 qt5 버전을 사용할 것이면 
 dnf로 설치해도 되지만 호환성이 걱정되서 빌드 버전으로 설치함 (호환성 생각하면 하위 버전이어야겠지만...)   
 따로 우분투에서 사용하고 있는 것은 참고로 qt creator 버전은 8.0.1, QT는 6.3.1 버전이어서   
 Rocky Linux에서도 빌드로 설치를 함
 
> snap버전은 파일 경로를 설정거나 할 때 에러가 발생하며 제대로 실행이 안된다  
> 이것은 ubuntu 에서 snap으로 설치할 때에도 같은 현상..;;;





