#include <iostream>
using std::string;

class Employee {
    private:
        //string Name; // 외부에서 접근이 안됨/ 다른 클래스 포함 (상속 받은 클래스도)
        string Company;
        int Year;
    protected:
        string Name;

    public:
    // constructor
        Employee (string name, string company, int year) {
            Name = name;
            Company = company;
            Year = year;
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

        void setAge(int year) {
            Year = year;
        }
        int getAge() {
            return Year;
        }

        void Promote() {
            if (2021 - Year >= 3) {
                std::cout << "Congrats! " << Name << " will be promoted" << std::endl;
            } else {
                std::cout << "Sorry~ " << Name << " is not pormoted" << std::endl;
            }
        }

};


class Developer: public Employee {
    public :
        string FavProgrammingLanguage;
        // contructor
        Developer(string name, string company, int year, string favProgrammingLanguage) 
            :Employee(name, company, year) {
                // 생성자에서도 속성을 만들어 줄 때 상속을 받아서 만들어 준다
                FavProgrammingLanguage = favProgrammingLanguage; //Developer 클래스의 속성 만들어주기
        }

        void FixBug() {
            // 이때 Employee 클래스의 Name 이 private로 되어 있어서 접근이 안됨
            std::cout << Name << " fixed bug using" << FavProgrammingLanguage << std::endl;
            // protected로 바꿔주면 비로서 Name에 접근할 수 있다
        }
};

int main() {
    Developer dev = Developer("Smith", "naver", 2000, "Python");

    std::cout << dev.getName() << ", " << dev.getCompany() << ", " << dev.getAge() << std::endl;

    // 상속받은 클래스의 protected 속성으로 접근해서 출력가능해짐
    dev.FixBug();
    dev.Promote();
}


