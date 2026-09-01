# Failed to Start Applicationd에러 build settings하기
qt creator의 왼쪽 하단의 세모 버튼, 세모 버튼(디버깅) 을 누르면 GUI로 디자인 폼을 만들었으면   
window창이 실행이 되거나, CLI 로 만들었으면 Application 에서 찾아볼 수가 있는데  

dnf install 버전과 snap으로 인스톨 한 것들은 디버깅에서 
`qt creator build directory not created`  이라고 나오면서  또는   
permission 관련 에러라고 나오는 듯 하다 . 그래서 살펴보면 빌드 관련 디렉토리가 생성이 되지를 않는다.  

```
Failed to Start Application - Qt Creator
Starting excutable failed:
/home/myuser/qt_ws/build-my_first_project-Desktop-Debug/my_first_project: No such file or directory.
```

하단의 Application을 보면 
```
The process failed to start. Either the invoked program "/home/myuser/qt_ws/build-my_first_project-Desktop-Debug/my_first_project" is missing, or you may have insufficient permissions to invoke the program.
```
이렇게 나온다 

예를 들어서 my_first_project 라는 프로젝트를 만들었으면 build-my_first_project-Desktop-Debug 라는 디렉토리가 자동으로 생성이 되어야 하는데 실제로 만들어지지를 않는다. 

왼쪽화면의 Projects에서 Desktop의 Build 부분의 화면,  Build Settings 에서   
Separate Debug info 라는 부분이 Leave at Default 로 되어 있다  
이것을 Enable 로 바꿔준다 
그러면 recompile 하겠냐고 물어본다 Yes를 누른다 

이제 빌드 또는 녹색세모를 누르면 GUI window 화면이 잘 실행되는 것을 볼 수 있다  
물론 디렉토리에도 
```
drwxrwxr-x. 2 myuser myuser 224 Sep 25 18:16 build-my_first_project-Desktop-Debug
drwxrwxr-x. 2 myuser myuser 146 Sep 25 18:13 my_first_project

```

이제 잘 생성 된다 
