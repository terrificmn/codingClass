#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//struct 정의 // 구조체
//구조체 기본
struct student {   
    int num;
    double grade;
};

// 구조체 활용
struct profile {
    char name[20];
    int age;
    double height;
    char *intro;
};

int main() {
    //구조체 기본
    struct student s1; //s1을 변수로 struct student형으로 선언, 
    //이제 s1이라는 이름으로 사용할 수 있음 (약간 클래스 또는 모듈 같으 느낌)
    s1.num = 2;
    s1.grade = 2.7;
    printf("학번: %d\n", s1.num); // (.)으로 접근
    printf("학점: %.1lf\n", s1.grade);
    printf("\n\n");

    // 구조체 활용
    struct profile yun;
    strcpy(yun.name, "서하윤"); //문자열을 배열에 직접 넣을 수 없으므로 strcpy를 이용
    yun.age = 17;
    yun.height = 164.5;

    yun.intro = (char *)malloc(80); //**포인터변수에 (profile 구조체에 정의한 포인터 intro) 문자열을 넣어줄 수 없으므로 
    //** 메모리에 동적 할당을 먼저 해줘야 함, 또는 초기화시에 동적할당
    printf("자기소개: ");
    gets(yun.intro);

    printf("이름: %s\n", yun.name);
    printf("나이: %d\n", yun.age);
    printf("키: %.1lf\n", yun.height);
    printf("자기소개: %s\n", yun.intro);
    free(yun.intro); //동적으로 할당한 메모리 영역 반환

    return 0;

    //TODO: 499p 정리해보기, 구조체 배열 처리하는 함수
}

