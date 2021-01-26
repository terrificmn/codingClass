#include <stdio.h> 
int main() {
    int age;
    double height;
    char name[20];

    printf("나이와 키를 입력하세요: ");
    scanf("%d%lf", &age, &height); //* scanf로 입력을 받을 때는 %d%lf를 붙여서 사용해야함. 변수 연결은 &변수
    printf("나이는 %d살, 키는 %.1lfcm입니다.\n", age, height);

    printf("이름 입력: ");
    scanf("%s", name);  //* 원래 scanf()에서는 변수를 할당할 때 &를 써야하는데 문자열 배열 입력을 받을 때는 &를 붙이지 않는다.
    printf("%s 입니다.\n", name);

    return 0;
    }