#include <stdio.h>
/*
    struct student {   //struct 정의하기
        int num;
        double grade;
    };
    // struct으로 정의된 것을 다시 재정의 
    typedef struct student Student;  //struct로 정의된 student를 Student로 다시 재정의 : typedef-type define
*/

// 위의 코드를 아래 처럼 정의할 수도 있다
// 재정의하기 전의 자료형을 굳이 사용할 필요가 없을 때 형 선언과 동시에 재정의 하는 방법
typedef struct {
    int num;
    double grade;
} Student;  // 일반 변수명과 구별하기 위해 대문자로 시작하는게 좋다

void print_data(Student *ps); 

int main() {
    Student s1 = { 315, 4.2 };  //typedef로 정의된 Student를 s1변수로 정의
    print_data(&s1);
    return 0;
}
void print_data(Student *ps) {
    printf("학번: %d\n", ps->num);
    printf("학점: %.1lf\n", ps->grade);
}