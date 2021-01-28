#include <stdio.h>
int main() {
    char *pDessert = "apple"; //문자열 자체가 주소값
    char str[10] ="mango";
    char *pa;

    int age; 
    char name[20];

    //todo: 문자열 복습 필요
    //str = "직접입력시에러";
    //str[0] = "a";  // 문자열에 값을 직접 넣는 것은 불가능함, 에러 //*처음에 변수선언할 때 초기화 해주어야함
    //todo: pa = str 해볼 것
    pa = str;
    pa = "oldmango"; //포인터 변수로 str의 값을 바꾸는 것이 가능. 단, 정확히는 바뀌는 것이 아니고 주소가 변경되는 것
    printf("%s\n", pa);
    pa = "newmango";
    printf("%s\n", pa + 5);
    
    printf("%c\n", str[0]);

    printf("오늘 후식은 %s 입니다\n", pDessert);
    pDessert = "banana";
    printf("내일 후식은 %s 입니다\n", pDessert);


    printf("--------------------\n");
    printf("나이 입력: ");
    scanf("%d", &age);
    getchar(); //버퍼에 남은 '\n' 개행문자 제거
    //* 같은 기능으로는 scanf("%*c") 또는 fgetc(stdin) 도 버퍼에서 하나의 문자를 읽어서 버림

    printf("이름 입력: ");
    gets(name);
    printf("나이: %d, 이름: %s\n", age, name);
    
    
    return 0;

}