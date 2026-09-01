# c++ class incapculation 클래스 만들기
c++ 클래스 1편 보려면   
[class 1편 보고 오기](/blog/cpp-c-시작해보기-class-1편)

클래스의 중요한 점 중에 하나인 캡슐화에 대해서 공부해보았다

먼저 Employee라는 클래스를 만들어 준다

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

 // 클래스로 오브젝트 만들기
    Employee Anyone("John", "good_company", 38);
    
    // 메소드 호출
    Anyone.Introduce();
```

위에서 보면 일단 public 이하로 Employee의 속성을 Name, Company, Age로 만들었다  
생성자를 만들어서 처음에 클래스를 이용해서 오브젝트를 만들 때 3개의 파라미터 값을 받는 생성자

```cpp
class Employee {
public :
    string Name;
    string Company;
    int Age;

...생략
```

그리고 Introduce()라는 메소드는 Employee의 속성들 (변수들)을 이용해서 출력하는 함수이고
```cpp
//method
void Introduce() {
    std::cout << "Hello my name is " << Name << std::endl;
    std::cout << "I am " << Age << " year old" << std::endl;
    std::cout << "I work for " << Company << std::endl;
}
```
클래스의 중간에 public: 이하는 모두 public으로 만들어서 외부에서 접근이 가능하게 만들었다

그리고 생성자는 최초로 파라미터로 값들을 받아서 class의 속성을 생성해준다. 클래스명과 같게 만들어 줘야한다
```cpp
//constructor
    Employee (string name, string company, int age) {
        Name = name;
        Company = company;
        Age = age;
    }
};  //class는 ; (세미콜론으로 닫아줘야한다)
```

이제 main함수에서 
Anyone 이라는 오브젝트를 만들 때 클래스를 만들 때 필요한 파라미터에 맞게 변수를 넘겨주면 클래스 오브젝트가 만들어 진다
```cpp
 // 클래스로 오브젝트 만들기
    Employee Anyone("John", "good_company", 38);
    
    // 메소드 호출
    Anyone.Introduce();
```

그래서 객체 Anyone에서 Introduce() 메소드를 호출하면

아래와 같은 결과를 볼 수가 있다
```
Hello my name is John
I am 30 year old
I work for good_company
```

<br/>

## class의 중요한 기능 중 하나인 캡슐화 encapsulate

먼저 Public으로 만들어진 클래스의 속성 변수들을 Private으로 만들어 주면 외부에서 접근이 안 된다  
이렇게 하면 이제 외부에서 접근을 못하게 해서 클래스 내부에 숨기는 기능이다. 

말그대로 캡슐화이니깐 약 캡슐처럼 약의 가루를 캡슐안에 넣어서 밖에서 안 보이지만 약의 기능은 그대로 인 것을 말함

위의 코드의 class 부분에서 public으로 되어 있던 것을 조금 바꿔서 Private으로 바꿔주면 된다
여기에서는 class의 속성들을 바꿔준다 

대신에 이렇게 하면 외부에서 접근을 할 수가 없어서 통칭 setter, getter 만들어서 접근 및 받을 수 있게 있게 해준다

> 왜 Private으로 만드는 것일까? 만드는 사람 마음?! 어떤 값들이 다른 요인들 또는 외부에서 접근을 해서   
변경되거나 하는 것을 원치 않아서 이런 기능들이 만들어진다고도 한다. 뭔가 바뀌거나 하면 안되는 것들을 작업할 때 
private으로 선언을 하나 보다. 아직까지는 그냥 그렇구나~ 한다 ㅠ 

어쨋든 setter는 뭔가 값을 저장하거나 설정하는 것이라고 생각하면 될 듯하고,    
반대로, getter라는 내용을 받는 통칭 하는말이라고 생각하면 되고       
그래서 뭔가 클래스의 속성값을 바꾸려고 하면 메소드를 통해서 값을 바꿀 수 있게 한다  
그리고 그 값은 getter 메소드로 값을 출력할 수 있게 한다  

코드를 살펴보자

```cpp
#include <iostream>
using std::string;

// incapculation
class Employee {
private :  // 이 부분을 private로 해주기
    string Name;
    string Company;
    int Year;

public:
    //method
    void Intorduce() {
        std::cout << "Hello my name is " << Name << std::endl;
        std::cout << "I work for " << Company << "from " << Year << std::endl;
    }

    //constructor
    Employee (string name, string company, int year) {
        Name = name;
        Company = company;
        Year = year;
    }
};  //class는 ; (세미콜론으로 닫아줘야한다)

int main () {
    // 클래스로 오브젝트 만들기
    Employee Anyone("John", "yh", 2010);
    
    Anyone.Intorduce();
    Anyone.Name = "Sara";
}
```

이제 main()함수에서 Name속성에 접근해서 다른 값을 저장하려고하면 에러가 발생한다

<img src=0>
<br/>

private으로 선언되어 있기 때문에 접근이 안되는 것

> 선언한 부분을 public으로 바꿔주면 빌드가 잘 된다. 하지만 private을 연습을 하고있는 것이므로 
getter와 setter을 사용해보자

class 내에 아래코드를 추가해준다
```cpp
... 생략 
class Employee {

    ... 생략
    
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

    void setYear(int year) {
        Year = year;
    }
    int getYear() {
        return Year;
    }
}; 
```
이제 main함수에 아래 코드로 바꿔서 수정해준다
```cpp
int main() {
    Employee Anyone("John", "yh", 2010);
    
    Anyone.Intorduce();

    Anyone.setName("Kim");
    std::cout << Anyone.getName() << std::endl;
    Anyone.setCompany("Google");
    std::cout << Anyone.getCompany() << std::endl;
    Anyone.setYear(2021); 
    std::cout << Anyone.getYear() << std::endl; 

    Anyone.Intorduce();
}
```

위의 코드처럼 바뀌게 되면 Anyone.Name 으로 하면 에러가 발생하고 외부에서 접근을 할 수 없지만 
이제 메소드들을 통해서 메소드를 만들어서 setName(), setCompany(), setAge() 등
클래스의 속성들 (Name, Company, Age)을 바꿔줄 수 있고, 
그 값을 받는 것을 메소드를 getName(), getCompany(), getAge() 통해서 가능하게 해준다

이렇게 setter와 getter 메소드들을 통해서 private으로 되어 있는 것도 접근이 가능하다

이제 결과를 보게 되면 

<img src=1>
<br/>


처음 클래스 생성자를 통해서 만들었던 것들에서 이후에 
setter메소드로 private 속성값인 변수들에 접근해서 바꾼 이후에 
getter메소도로 출력을 하게 되고 

다시 Introduce() 메소드를 실행하면 값들이 바뀌어 있는것을 알 수 있다

