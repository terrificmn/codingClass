



터미널에 프린트를 하고 싶을 때 사용할 수 있다 

```cpp
#include <QCoreApplication>
#include <QDebug>
```
 
사용은  
<< 를 사용해서 할 수도 있고, 함수의 아규먼트로 넘겨서 실행할 수도 있다
```cpp
qDebug() << "print!";

int age = 30;
qDebug("My age is %d", age);
```


그리고 프로젝트 디렉토리안에는 프로젝트이름.pro 파일이 생성이 되는데  
프로젝트의 속성들을 다룬다   

여기에서 콘솔 모드로 프로젝트를 만들었다면  
```
QT -= gui
```
라고 첫 줄에 나와 있는데 이런 경우는 gui를 사용하지 않겠다는 의미이다   

물론 GUI를 이용해서 만든다면  
```
QT += core gui
```
처럼 된다  



## 아주 간단한 버튼 만들기
프로젝트를 gui 로 만들어준다  

forms디렉토리의 mainwindow.ui 파일을 클릭하면 Edit를 할 수가 있는데  
여기에 Push Button을 넣어준다  
그리고 PushButton에서 마우스 오른쪽 버튼을 눌러서 Go to Slot 를 눌러서 이벤트를 선택해준다   

QAbstractButton의   
clicked(), clicked(bool), pressed(), released(), toggled(bool) 등이 있다..  그 외에 더 있음

그러면 자동으로 함수가 생성이 된다    mainwindow.cpp 파일에
```cpp
void MainWindow::on_pushButton_clicked()
{
    qDebug("HI~");
}
```

이제 실행을 시키면 버튼을 누르면 output을 확인할 수 있다 

