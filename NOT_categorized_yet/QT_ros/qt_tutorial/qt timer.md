ROS에서 timer에 맞춰서 callback 함수를 연동할 수가 있는데, qt에서도 QTimer라는 좋은 클래스가 있다   

먼저 QObject를 상속 받는 클래스를 만든다음에  만든는데...

기본 형식은 아래처럼 ...사용을 한다

```
QTimer *timer = new QTimer(this);
connect(timer, SIGNAL(timeout()), this, SLOT(updateFunc()));
timer->start(1000); ///msec
```


자세한 형태는 추후 업데이트 및 스터디... 

[여기 reference...](https://stuff.mit.edu/afs/athena/software/texmaker_v5.0.2/qt57/doc/qtcore/qtimer.html)

[여기 튜토리얼도 .. windows지만(상관없음..) 헤더 및 cpp로 자세히 설명이 되어 있다 굿!](https://www.bogotobogo.com/Qt/Qt5_QTimer.php)








