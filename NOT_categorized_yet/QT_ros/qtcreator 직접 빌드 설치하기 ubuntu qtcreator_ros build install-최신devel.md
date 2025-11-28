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
```

최신 devel 버전에서는 py7zr 버전 픽스
```
python3 -m pip install pyyaml requests py7zr==0.21
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
sudo apt install libgl1-mesa-dev ninja-build libutf8proc-dev libcups2-dev
sudo apt install libxcb-cursor-dev libxkbcommon-dev
```

> Rocky Linux 또는 Fedora 에서는  
rocky linux 에서 직접 build.md 파일 확인하기

깃클론
```
git clone https://github.com/ros-industrial/ros_qtc_plugin.git -b devel
```

install-sdk.py 로 변경 됨 (기존 setup.py에서)  

**!TODO:**  
일단 실행하기 전에 깃 리포지터리에서 README를 읽어 본 다음에 binary 를 받는 방법도 있기 때문에  
그걸로 먼저 테스트 해서 처리하자!  
아마도 apt 로 쉽게 처리가 될 듯 하다. 

install-sdk.py 로 변경이 되었는데, 이 부분은 테스트를 해보지 못했다. 기존 버전으로 사용하는 바람에 시도는 실패   

```
./install-sdk.py --install_path ~/Downloads/
```

> (old version) setup.py 실행
> ```
> cd ros_qtc_plugin
> ./setup.py
> ```

그러면 qt base 포함, qt creator등 패키지등을 다운을 받는다.  
>참고로 다운로드 시간이 꽤 걸리는 듯 하다...   

컴파일을 함 (ros_qtc_plugin 의 root에서 실행).  

```
cmake -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH="~/Downloads/qtc-sdk/Tools/QtCreator;~/Downloads/qtc-sdk/Qt/6.9.0/gcc_64"
cmake --build build --target package
```

6.6버전 일 경우
```
cmake -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH="/tmp/qtc_sdk/Tools/QtCreator;/tmp/qtc_sdk/6.6.0/gcc_64"
cmake --build build --target package
```
>참고 5.15 버전  
여기에서는 tmp/qtc_sdk/5.15.0/gcc_64 버전인데  
설치되는 버전은 Qt 6.3.0 이다 (Sep30, 2022기준)


뒷 부분은  
[qtcreator 직접 빌드 설치하기 ubuntu qtcreator_ros build install.md] 참고하기

