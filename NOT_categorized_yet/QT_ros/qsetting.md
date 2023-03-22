# qsetting

먼저 `#include <QSettings>` 을 인쿠르드 시키고  

인스턴스를 만들어준다. 
```cpp
QSettings settings("대표_dir", "config파일명");
```

/home의 유저 디렉토리 안에 .config 디렉토리에 파일이 생기게 된다. 파일은 conf 파일이다

예를 들어 
```cpp
QSettings settings("MyProject", "mini_project");
```

/home/user/.config/MyProject/mini_project.conf 파일이 생긴다


## setValue()
값 셋팅 
```cpp
std::string my_str = "hello"
settings.setValue("param1", QString::fromStdString(my_str));
```
QString으로 되어 있기 때문에 std::string 이라면 변환을 해줘야하고, 아니면 아예 QString으로 문자열을 만든다   

>> 2 중의 카테고리화 하려면 /로 구분해서 만들어준다  "category/param1" 이런식으로 작성

그래서 conf파일을 열어보게 되면 

```
[category]
parma1=hello

```
이런식으로 작성 되게 된다   



## value()
불러오기

```cpp
QString param1 = settings.value("hello").toString();
```
value()로 불러올 수 있고, 이때 만들어지는 것은 당연 QString이다. (qt여서)   
만약 std::string으로 바꾸려면 다시한번 QString에서 `.toStdString()` 을 해준다 (맨 뒤에 이어 붙여서 해도 됨)



아주 유용하게 잘 써먹을 수 있겠다.