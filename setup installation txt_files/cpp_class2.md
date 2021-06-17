일반적으로 클래스를 만드는 법

```cpp
#include <iostream>
using std::string;

// incapculation
class Employee {
public :
    string Name;
    string Company;
    int Age;

    //method
    void Introduce() {
        std::cout << "Hello my name is " << Name << std::endl;
        std::cout << "I am " << Age << " year old" << std::endl;
        std::cout << "I work for " << Company << std::endl;
    }

    //constructor
    Employee (string name, string company, int age) {
        Name = name;
        Company = company;
        Age = age;
    }
};  //class는 ; (세미콜론으로 닫아줘야한다)

int main () {
    // 클래스로 오브젝트 만들기
    Employee Anyone("Seongmin", "yh", 38);
    
    // 메소드 호출
    Anyone.Introduce();
}
```

위에서 보면 일단 public 이하로 Employee의 속성을 Name, Company, Age로 만들었다
생성자를 만들어서 처음에 클래스를 이용해서 오브젝트를 만들 때 3개의 파라미터 값을 받는 생성자

그리고 Introduce()라는 메소드를 만들어서 출력을 하게 하는 것


## class의 중요한 기능 중 하나인 캡슐화 encapsulate

먼저 Public으로 만들어진 클래스의 속성 변수들을 Private으로 만들어주는것
이렇게 하면 이제 외부에 접근을 못하게 해서 클래스 내부에 숨기는 기능이다

위의 내용을 조금 바꾸면 Private으로 바꿔주면 된다
대신에 이렇게 하면 외부에서 접근을 할 수가 없어서 setter, getter를 만들어서 할 수 있게 해준다

뭔가 클래스의 속성값을 바꾸려고 하면 메소드를 통해서 값을 바꿀 수 있게 한다
그리고 그 값은 getter 메소드로 값을 출력할 수 있게 한다


```cpp
#include <iostream>
using std::string;

// incapculation
class Employee {
private :
    string Name;
    string Company;
    int Age;

public:
    //method
    void Intorduce() {
        std::cout << "Hello my name is " << Name << std::endl;
        std::cout << "I am " << Age << " year old" << std::endl;
        std::cout << "I work for " << Company << std::endl;
    }

    //constructor
    Employee (string name, string company, int age) {
        Name = name;
        Company = company;
        Age = age;
    }

    //setter
    void setName(string name) {
        Name = name;
    }
    //getter
    string getName() {
        return Name;
    }

    void setCompany(string company) {
        Company = company;
    }
    string getCompany() {
        return Company;
    }

    void setAge(int age) {
        Age = age;
    }
    int getAge() {
        return Age;
    }

};  //class는 ; (세미콜론으로 닫아줘야한다)

int main () {
    // 클래스로 오브젝트 만들기
    Employee Anyone("Seongmin", "yh", 38);
    
    // 메소드 호출
    //Anyone.Intorduce();

    Anyone.setName("Kim");
    std::cout << Anyone.getName() << std::endl;
    Anyone.setCompany("Google");
    std::cout << Anyone.getCompany() << std::endl;
    Anyone.setAge(25); 
    std::cout << Anyone.getAge() << std::endl; 
}

```
위의 코드처럼 바뀌게 되면 이제 외부에서 접근을 할 수 없지만 메소드를 통해서 
클래스의 속성들 (Name, Company, Age)을 바꿔줄 수 있고, 그 값을 받는 것을 메소드를 통해서 가능하게 해준다

