QT는 communication은 signal/slot system을 사용한다  
마치 ROS에서 publish와 Subscribe를 하는 것 처럼..  

a signal은 message이고 보내지게 된다 (publish)   
a slot은 그 signal을 받아서 처리를 하게되어 slot function은 ROS의 subscirbe를 하기 위한   
 callback함수와 같은 기능을 하게 된다   

Signal/Slot을 사용하기 위해서는 QtObject를 상속받은 (inherited class) 클래스를 만들어 주면된다  
그러면 signal/slot을 사용을 할 수가 있다  

QObect를 상속 받은 클래스 예
```cpp
class AClass : public QObject {
	Q_OBJECT
public:
	AClass() {}
signals:
	void mySignal1(int);
	void mySignal2(float, int);
	void mySignal3();

public slots:
	void mySlot1(double);
	void mySlot2();
private:
	int memberVar;
};
```

```cpp
class BClass : public QObject {
	Q_OBJECT
public:
	BClass();
	void run();
signals:
	void mySignalFromB(double);
public slots:
private:
	AClass* aClass;
};

void BClass::BClass() {
	aClass = new AClass();
	connect(this, SIGNAL(mySignalFromB(double)), aClass, SLOT())(mySlot1(double)));
}

void BClass::run() {
	std::count << "B: sending signal form b" << std::endl;
	double var = 1.0;
	emit mySignalFromB(1.0)
}

void AClass::mySlot1(double msg) {
	std::cout << "A: received signal from B to slot in A" << std::endl;
	std::cout << "message value: " << msg << std::endl;
}

int main(int argc, char** crgv) {
	BClass bClass;
	bClass.run();

	return 0;
}
```

근데 위의 코드는 디버깅이 필요한 듯 하다  

그래도 코드를 봐보면   
- signal 를 보내는 함수에서는 signals를 로 선언한 mySignalFromB를 이용해서 SIGNAL()함수로 보내게 되는데, 이때 slot을 지정해서 보내게 된다. 여기서 받는 slot은 mySlot1()

- signal은 함수에서 arguments로 넘어가고, 따로  함수로 기능적으로 쓰이는 것은 아님  

- slot function은 ROS callback 함수(subscribe)처럼 사용이 된다  
- 클래스의 constructor에서 connect()함수로 source object address, signal funtion, destination object address, slot 함수를 지정한다
- emit 은 signal을 보낼때의 명령어 임



[참고자료qtcreator-ros편 참고하기](https://roboticsknowledgebase.com/wiki/tools/Qtcreator-ros/)

