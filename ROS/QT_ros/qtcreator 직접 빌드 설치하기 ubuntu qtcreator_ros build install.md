# ubuntu에서 qtcreator_ros 버전이 안되는 경우
결국 되기는 하나 자잘한 버그(?) 등이 있어서 ROS plugin은 따로 빌드를 해보기로 했다.  
다만 현재 최신 버전(?)으로 작동을 해서 Qt 6.3 대로 된다  

[여기 참고를 한다-qtcreator-ros(developers)](https://ros-qtc-plugin.readthedocs.io/en/latest/_source/Improve-ROS-Qt-Creator-Plugin-Developers-ONLY.html)

- 먼저 apt install로 설치한 qtcreator 삭제  
- snap으로 설치한 qtcreator-ros 삭제

snap으로 설치하는 버전과 비슷 한 것 같은데 그래서 snap으로 설치하는 방법도 소개한다  
아무래도 처음에 뭔가 꼬이지 않았으면 잘 실행이 될 것 같은데 뭔가 잘못된거 같다.  

어쨋든   
우분투 기준, dependencies
```
sudo apt update
sudo apt install libgl1-mesa-dev ninja-build libyaml-cpp-dev libqtermwidget5-0-dev libutf8proc-dev
sudo apt install python3-pip
python3 -m pip install pyyaml requests py7zr
```
*추가  
qtcreator 13.0 버전에서는 *tqdm_loggable* 을 필요로 한다.  
없다고 하는 경우
```
ModuleNotFoundError: No module named 'tqdm_loggable'
```
설치
```
python3 -m pip install tqdm-loggable
```

의존성이 더 늘어남. 
```
sudo apt install libxcb-cursor-dev libxkbcommon-dev
```

> Rocky Linux 또는 Fedora 에서는  
rocky linux 에서 직접 build.md 파일 확인하기

깃클론
```
git clone https://github.com/ros-industrial/ros_qtc_plugin.git -b devel
```

*중요* 일단 devel 브랜치도 게속 업데이트 되어 내용 및 버전이 바뀌니 특정 커밋으로 잘라내기 . 6.6 버전쯤  
> 꼭 최신 업데이트가 필요하지 않아서...
```
cd ~/ros_qtc_plugin/
git reset --hard b266e3a09e41b8285ece98e4456b99c0c24c967d
```

setup.py 실행
```
cd ros_qtc_plugin
./setup.py
```

그러면 qt base 포함, qt creator등 패키지등을 다운을 받는다.  
>참고로 다운로드 시간이 꽤 걸리는 듯 하다...   

컴파일을 함 (ros_qtc_plugin 의 root에서 실행).  
6.6버전 일 경우
```
cmake -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH="/tmp/qtc_sdk/Tools/QtCreator;/tmp/qtc_sdk/6.6.0/gcc_64"
cmake --build build --target package
```

트러블 슈팅, 각각 QtCreatorConfig.cmake 또는 Qt6Config.cmake 등으로 못 찾는다는 에러 발생 시   
> 참고로 docker 환경에서 에러가 발생함 (아마도 일반 환경에서는 발생하지 않을 듯 하다..)  
!일단 docker 에서도 설정이 꼬였던 것 같다.. 일단 다시 새로운 docker 환경에서는 발생하지 않음  


```
  Could not find a package configuration file provided by "QtCreator" with
  any of the following names:

    QtCreatorConfig.cmake
    qtcreator-config.cmake

  Could not find a package configuration file provided by "Qt6" (requested
  version 6.2.0) with any of the following names:

    Qt6Config.cmake
    qt6-config.cmake
```

먼저 find 를 이용해서 위치를 파악 
```
find / -name QtCreatorConfig.cmake > result
find / -name Qt6Config.cmake >> result
```
이후
`cat result` 로 확인
```
/tmp/qtc-sdk/Tools/QtCreator/lib/cmake/QtCreator/QtCreatorConfig.cmake
/tmp/qtc-sdk/Qt/6.10.0/gcc_64/lib/cmake/Qt6/Qt6Config.cmake
/tmp/qtc-sdk/6.6.0/gcc_64/lib/cmake/Qt6/Qt6Config.cmake
```
> 대충 이렇게 나왔다면, Qt/6.10.0 은 처음 최신 버전으로 받아져서 다른 버전이 같이 받아진 듯 하다. 

여기에서 cmake 파일이 확인 되었으므로 cmake prefix 를 지정해주면 된다. 
예시는 `export CMAKE_PREFIX_PATH="/path/to/QtCreator/installation:$CMAKE_PREFIX_PATH"`

```
export CMAKE_PREFIX_PATH="/tmp/qtc-sdk/Tools/QtCreator/lib/cmake/QtCreator:$CMAKE_PREFIX_PATH"
export CMAKE_PREFIX_PATH="/tmp/qtc-sdk/6.6.0/gcc_64/lib/cmake/Qt6:$CMAKE_PREFIX_PATH"
```

이후 다시 빌드를 진행하면 빌드가 된다. 


예전 버전, 5.15~~
```
cmake -B build -GNinja -DCMAKE_BUILD_TYPE=Debug -DCMAKE_PREFIX_PATH="/tmp/qtc_sdk/Tools/QtCreator;/tmp/qtc_sdk/5.15.0/gcc_64"
cmake --build build --target package
```

여기에서는 tmp/qtc_sdk/5.15.0/gcc_64 버전인데 
설치되는 버전은 Qt 6.3.0 이다 (Sep30, 2022기준)

> DCMAKE_PREFIX_PATH 를 /tmp/qtc_sdk 로 지정한 것은 setup.py로 실행했을 때 관련 파일을 다운받고 압축을 풀어서 만들어놓음

### 이제 중요한 ROS plugin등록하기
이제 위의 cmake가 끝나면 ROSProjectManage.....zip파일이 생성이 되는데 

Qt creator를 실행을 해서  Help -> About Plugins -> Install Plugin 을 해서 zip파일 통째로 선택해주면 된다 import를 해준다  

또는 Qt/Tools/QtCreator/ 안에 압축을 풀어준다  

?? 하지만 Qtcreator가 없는데 ??  
/tmp에서 만들어진 /tmp/qtc_sdk 를 통째로 복사해서 사용하면 됨
```
mv /tmp/qtc-sdk/ ~/
```
단,  실행파일이 심볼릭 링크가 없으므로 직접 접근해서 실행을 해야함
```
cd ~/qtc-sdk/Tool/QtCreator/bin
./qtcreator
```

만약 이후 qtcreator 를 복사한 후에 다시 한번 export 해준다. qtcreator 실행 시 특정 프로젝트 빌드 수행 시 qt6 를 못찾을 경우  
> 아마도 docker 환경에서만 그럴 듯 하다.;;
```
export CMAKE_PREFIX_PATH="~/qtc-sdk/6.6.0/gcc_64/lib/cmake/Qt6:$CMAKE_PREFIX_PATH"
```

PATH 환경변수에 위의 경로를 등록해주거나, 심볼릭 링크를 만들어준다 

일단 bin 디렉토리 통채로 $PATH 환경변수에 들어가는 것이 싫어서 먼저 심복릭 먼저 만들고 
```
ln -s $HOME/Qt/Tools/QtCreator/bin/qtcreator ~/Qt/qtcreator
```

> 항상 헤깔림. 원본파일~ 그다음이 심볼릭만들Path

그 다음에 PATH 변수에 등록 하고 테스트 
```
export $PATH=$PATH:$HOME/Qt
cd 
qtcreator
```
다른 경로에서도 잘 실행되는 것이 파악 되었으면  bashrc 파일에 넣고 저장해준다
```
vi ~/.bashrc

## 파일이 열리면
export $PATH=$PATH:$HOME/Qt
## 저장 후 빠져나오기
source ~/.bashrc
```

이제 qtcreator를 터미널에서 실행을 할 수가 있고 
Kits 설정에서 qt versions를 6.3의 qmake 파일을 등록해주고    
경로는 `~/Qt/6.3.0/gcc_64/bin/qmake` 에 있는 파일 지정해주고 apply 후 Desktop의 버전을 잘 선택해준다.  

기존 ros(?) 와 함께 기본으로 설치되어 있는 qt 버전은 5.12 버전  
이 버전을 사용해도 된다.   

만약 5.15 버전을 사용하고 싶으면  Qt 공홈에서 opensource 버전으로 다운 후 설치를 하는데  
qt 5.15 만 설치를 해주고 다른 것은 설치를 안해도 될 듯...  
아싸리 다시 설치를 해봐야겠다. 왜? 15기가나 차지했을 까?

> 다시 생각해보면 위의 방식으로 qt_creator 및 qt 6.3을 설치를 하고나서 rosplugin을 import를 해주거나 하면 되고, 5.15를 사용하려면은 공홈에서 다운 받은 후 qt versions - qmake를 등록해보자   

참고로 직접 qt base 버전을 다운받아서 빌드 가능. 굉장히 굉장히 시간 오래걸림;; 
공홈에서 다운 받는 것을 추천(다시 시도해볼 예정 후 업데이트)   

그래도 빌드하려면 -- 하지말자
[여기서 base 버전 다운](https://download.qt.io/official_releases/qt/5.15/5.15.3/submodules/)
할 수 있지만 base 만으로는 안됨. 시간 더럽게 오래걸림~ 실패함;

마지막으로 
ros_qtc_plugin은 삭제해도 된다

### console application 의 freezing 현상
처음에 프로젝트를 console application으로 만들고  
그냥 qDebug() 함수를 이용해서  hello world 를 실행시키는 것 조차 실행이 안된다.  

뭔가 버그이거나 필요한 게 설치가 안되어 있는 듯 하다  

> 일단 console application은 사용 안하는 게 좋을 듯 하다 (해결 전 까지)



## 아래는 그냥 참고만 (snap)설치와 실행은 되나 버그가 있는 듯하다

ubuntu에서 qtcreator_ros 버전이 안되는 경우
snap으로 설치했을 시에 이런 에러가
```
The qmake executable /run/user/1000/doc/dbd746f0/qmake could not be added: qmake "/run/user/1000/doc/dbd746f0/qmake" is not an executable.
```
결국은 직접 해결하는 것은 실패했다.  

뭔가 꼬여있는듯.. Qt 공식홈에서 받은 것을 지우고 다시 snap으로 qtcreator_ros를 설치를 하려고 했는데 
남이 있는 디렉토리는 전부 지웠는데.. 결국 해결은 못하고 다른 방법 사용

Kits 설정에서 qt 버전을 추가하려고 하면 에러가 발생하면서 추가가 안됨  

그래서 apt 에서 제공하는 qtcreator도 설치할 수가 있어서 일단 설치
```
sudo apt install qtcreator
```

그냥 qtcreator 버전으로 실행을 해서 
Tools -> Options 에서 

다행히 kits 설정에서 qt versions이 선택은 되지만
/usr/lib/qt5/bin/qmake   
/usr/lib/x86_64-linux-gnu/qt5/bin/qmake
/usr/lib/qt5/bin/qmake

아차피 셋 다 5.12 버전이라 하나만 추가 해도 된다  

먼저 Qt버전 추가한 후에 Apply 버튼을 눌러서 적용 해준다음에  
Kits에서 Default Desktop을 클릭하고 Qt 버전을 선택해주면 된다 

이제 종료를 하고 나서 
snap으로 설치한 qtcreator_ros를 실행해준다   

다행히 qtcreator와 공유가 되는 부분이 있는 듯.. Kits의 데스크탑에서 qt5 버전이 선택이 되어 있다   

이제 사용이 가능!!

> qtcreator_ros 플러그인은 project를 만들 때 other 부분에서 ros workstation 지정을 지원한다 

- 그리고 qtcreator_ros에 버그가 있는 듯 하다.  파일 경로를 열 때 파일 창에서 디렉토리가 선택으로 끝나는 것이 아니고 계속 하위 디렉토리로 들어가진다. 그래서 project location을 정할 수가 없다   
- 또 하나의 버그는 qrc 파일을 만들어서 resource를 prefix해서 이미지 파일등을 등록 할 수가 있는데 파일이 저장이 안된다 (열리지를 않음)

- 다행히 직접 입력을 해주고 (없으면 빨간색으로 표시됨) Use as default project location에 체크를 해주면 될 듯 하다

- Rocky linux dnf 패키지 버전 qtcreator는 빌드 디렉토리가 직접 생성이 안되어서 Projects의 Build Settings에서 직접 빌드 부분을 enable 해야했는데 다행히 자동으로 build 디렉토리가 생긴다 


