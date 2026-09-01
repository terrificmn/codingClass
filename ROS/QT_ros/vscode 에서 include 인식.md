vscode로 qt 프로젝트를 열게 되면 Qt파일들을 인식을 못하는데  

main.cpp 등에서 지렁이 표시가 나는 곳을 마우스를 가져가면 source file을 찾을 수 없다고 나오면서  
Quick fix를 클릭할 수가 있는데 클릭해준다  

> 또는 ctrl+shift +p 를 눌러서 C/C++ 눌러주면 바로 자동완성이 되는데 이중에   
> C/C++ Edit Configurations (Json)
> C/C++ Edit Configurations (UI) 를 선택해주면 된다   

자동으로 생성되는 /usr/include/x86_64-linux-gnu/qt5 이 경로는 현재 설치되어 있는 Qt 버전과 맞지 않으므로 무시하고   

Edit "includePath" setting 을 눌러준다   

C/C++ Configurations 창이 뜨는데 마우스를 스크롤해서 아래쯤에 Include path 부분에서  
One include path per line 부분에 추가 해준다 

```
${workspaceFolder}/**
${HOME}/Qt/6.3.0/gcc_64/include/**
```

QT가 어디에 설치되어 있느냐에 따라서 지정을 해주면 된다 


## Json으로 설정

ctrl+shift +p 를 눌러서 C/C++ 눌러주면 바로 자동완성이 되는데 이중에   
C/C++ Edit Configurations (Json) 선택   

이부분의 블럭에 채워준다 
```json
..생략..
"includePath": [
	"${workspaceFolder}/**",
	"${HOME}/Qt/6.3.0/gcc_64/include/**"
],
```


참고로 위의 include 경로에는 QtCore QtQuick 등등 라이브러리가 다 들어있음


`/usr/local/include` 등에 있는 include 파일을 추가할 때도 사용이 가능하고  
/** 없이, 또는 sub디렉토리 이름 없이 넣어주면 잘 작동한다.  
> 오히려 sub directory 이름까지 넣으면 intellisense가 못 찾는 듯 하다.

```json
..생략..
"includePath": [
	"/usr/local/include"
],
```

