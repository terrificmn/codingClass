ROS에서 timer에 맞춰서 callback 함수를 연동할 수가 있는데, qt에서도 QTimer라는 좋은 클래스가 있다   

h 헤더 파일 클래스는 QObject를 상속해서 만든다   
함수 생성자 정의와, QTimer 클래스를 이용해서  포인터 timer를 만들어준다  

public slots: 에는 타이머가 작동할 때 사용할 함수를 연결해준다  

```cpp
#include <ros/ros.h>
#include <QTimer>

class MyTimerClass : public QObject {
	Q_OBJECT

public:
	MyTimerClass();
	QTimer* timer

public slots:
	void myTimerSlot();
}
```


이제 cpp 파일에서는 

```cpp
MyTimerClass::MyTimerClass() {
	timer = new QTimer(this);
	connect(timer, SIGNAL(timeout()), this, SLOT(myTimerSlot()));
	timer->start(1000); ///msec
}

void MyTimerClass::myTimerSlot() {
	// 여기에 하고자 하는 것을 사용하면 됨
	ROS_INFO("Hello~");
}
```


timer를 QTimer로 새로 만들어준 후에,  connect() 함수로 4개의 파라미터로 지정해서 입력   
public slots로 연결했던 myTimerSlot()함수가 지정된 1000 (1초) 마다 작동을 하게 된다 

[여기 reference...](https://stuff.mit.edu/afs/athena/software/texmaker_v5.0.2/qt57/doc/qtcore/qtimer.html)

[여기 튜토리얼도 .. windows지만(상관없음..) 헤더 및 cpp로 자세히 설명이 되어 있다 굿!](https://www.bogotobogo.com/Qt/Qt5_QTimer.php)








