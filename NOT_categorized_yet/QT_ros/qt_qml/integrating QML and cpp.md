[물론 메뉴얼이 먼저겠지만 qtqml-cppintegration-topic](https://doc.qt.io/qt-6.2/qtqml-cppintegration-topic.html)   
qmake 기반으로 되어 있는 듯 하다. cmake를 사용할 때 어떤 식으로 해야하나  


[참고한 사이트 잘 정리가 되어 있다](https://scythe-studio.com/en/blog/how-to-integrate-qml-and-c-expose-object-and-register-c-class-to-qml)



## cmake 빌드로 사용할 경우
먼저 Qt Quick Application으로 만들어준다  

- Build system은 cmake로 해준다  
- Minimum required Qt version은 그냥 6.2로 했다

이렇게 하면 프로젝트 디렉토리와 그 안에 main.cpp, main.qml, CMakeLists.txt 파일을 만들어주는데   
qt creator IDE에서는 파일 자체로 안 보여주고 Source Files를 눌러주면 main.cpp가 보이게 된다  

필요한 파일은 Backend 클래스를 만들기 위한 헤더파일과 cpp 파일이 필요하다  

먼저 클래스를 만들어준다  
> File메뉴에서 New File로 해서 C++ Class 를 선택하면 header파일과 같이 만들어주니 편하다

이렇게 해도 왼쪽의 파일메뉴(?) (Projects선택)로 선택해도 cpp파일과 h파일이 보이지 않는다  

CMakeLists.txt 파일에 파일을 추가해준다 예를 들어
```
qt_add_executable(appintegrating_qml_cpp
    main.cpp
    backend.cpp
)
```


## qml에서 사용할 클래스 만들기

위의 executable에 추가한 파일이 클래스로 사용할 파일  

class이름은 예제처럼 BackEnd 로 만들고 QObject를 상속받아서 만든다  
매크로로 Q_OBJECT와 Q_PROPERTY()를 생성해주는데  
이것들이 qml에서 사용할 수 있게 되는 property가 된다  

> 아직 매크로에 대해서는 공부를 좀 더 해야겠다  

그리고 클래스 생성자에는 QObject를 포인터로 파라미터로 받고 시작  
그 밖에 QML로 만든 화면에서 사용할 버튼 등에 쓰일 slots: signals: 등을 정의해준다   

헤더파일 예
```cpp
#ifndef BACKEND_H
#define BACKEND_H

#include <QObject>
#include <QString>

class BackEnd : public QObject {
	Q_OBJECT
	// Q_PROPERTY macro delclares a property that could be accessed from QML
	Q_PROPERTY(QString userName READ userName WRITE setUserName NOTIFY userNameChanged)
	
	// QML_ELEMETN macro makes the BackEnd class available in QML
	// QML_ELEMENT

public:
	explicit BackEnd(QObject *parent = nullptr);
	QString userName();
	bool isNightMode = false;

public slots:
	void setUserName(const QString &userName);
	void setNightMode();

signals:
	void userNameChanged();

private:
	QString m_userName;

};
#endif // BACKEND_H
```

위의 macro중에 QML_ELEMENT는 qml에서 현재 Backend 클래스가 사용할 수 있게 해주는 것인데  
아마도 qmake 빌드 일 때 되는 것 같다  
저거와 같이 .pro 파일에 몇 줄 추가해줘야한다  (매뉴얼 참고)


cpp 파일은 아래처럼 
```cpp
#include "backend.h"

BackEnd::BackEnd(QObject *parent) : QObject(parent) {
}

QString BackEnd::userName() {
	return m_userName;
}

void BackEnd::setUserName(const QString &userName) {
	m_userName = userName;
	emit userNameChanged(); // this function emits userNameChanged signal
	// signal can be handled from QML using the onUserNameChanged handler
}

void BackEnd::setNightMode() {
	this->isNightMode = true;
}

```

cpp랑 연동이 될려면  클래스의 slots와 signals가 정의가 되어야 된다   
그래서 setUserName() 메소드가 실행이 되면 qml에서 버튼을 눌렀을 때 onClick 부분에서 작동  

이렇게 되면 메소드에서 내용을 처리하고 emit을 (signals)를 처리하게 되면 이것 역시 QML에서 사용이 가능해진다  

> 아직 정확하게 다 알지는 못해서 더 공부가 필요하다  


## 이제 main.cpp파일에서 인쿠르드 및 객체 생성

main.cpp 파일에서 new로 다이나믹(?)할당으로 생성을 해주게 된다 

QGuiApplication app()으로 만들어진 QObject를 생성을 하면서 파라미터로 넘겨준다   
```cpp
main{ 
	QGuiApplication app(argc, argv);
	QQmlApplicationEngine engine;

	// exposing C++ Object to QML
	BackEnd *backEnd = new BackEnd(&app);
	engine.rootContext()->setContextProperty("backend", backEnd);
	// by calling setContextProperty(), C++ Object is accessible from QML
...생략
```

QQmlApplicationEngine으로 만들어진 객체를 이용해서 setContextProperty를 해서 넘겨주게 되면  
QML에서 C++ object를 사용할 수 있게 된다  


전체파일 예는 
```cpp
#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <backend.h>

int main(int argc, char *argv[]) {
	QGuiApplication app(argc, argv);
	QQmlApplicationEngine engine;
	
	// exposing C++ Object to QML
	BackEnd *backEnd = new BackEnd(&app);
	engine.rootContext()->setContextProperty("backend", backEnd);
	// by calling setContextProperty(), C++ Object is accessible from QML

	const QUrl url(u"qrc:/프로젝트명/main.qml"_qs);
	QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
					 &app, [url](QObject *obj, const QUrl &objUrl) {
		if (!obj && url == objUrl)
			QCoreApplication::exit(-1);
		}, Qt::QueuedConnection);

	engine.load(url);

	return app.exec();
}
```


## 이제 마지막 qml

qml로 작성할 부분  
Window 안에 Column 부분으로 나눠 있고  

그 안에 text 표시할 Text, TextField 입력창, 버튼 이게 다임

```qml
import QtQuick 2.6
import QtQuick.Controls 2.0

Window {
    id: root
    width: 360
    height: 480
    visible: true
    title: qsTr("Expose C++ Object test")

    Column {
        anchors.centerIn: parent
        spacing: 20

		Text {
            color: backend.isNightMode ? "#421253" : "#218165"
            text: backend.userName
        }

        TextField {
            id: text1
            text: backend.userName
            placeholderText: qsTr("user name")
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            text: qsTr("emit test")

            onClicked: {
                backend.setUserName(text1.text)
            }
        }

    }
}
```

c++ 객체 backend 로 사용할 수가 있고 . 으로 속성, 메소드 사용가능

입력창 TextField는 의 text 속성에는 backend 객체의 userName을 주게 되고   
입력을 한 후에 버튼을 클릭하게 되면 onClicked 발생하면서  
backend 객체의 setUserName() 메소드 호출 (slots)   
매개변수로 text1 즉 TextField 의 text 값을 넘겨주게 된다 

그러면 setUserName()메소드에서 emit()이 발생하면서 QML에서 신호를(?) 알게 되고  
Text의 text 가 바뀌게 된다 (입력한 값으로..)

> 역시 공부가 더 필요..

