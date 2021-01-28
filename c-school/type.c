#include <stdio.h>

int main(){
    /*
    int age;
    double height;
    char name[20];

    printf("나이와 키를 입력하세요: ");
    scanf("%d%lf", &age, &height); //* scanf로 입력을 받을 때는 %d%lf를 붙여서 사용해야함. 변수 연결은 &변수
    printf("나이는 %d살, 키는 %.1lfcm입니다.\n", age, height);

    printf("이름 입력: ");
    scanf("%s", name);  //* 원래 scanf()에서는 변수를 할당할 때 &를 써야하는데 문자열 배열 입력을 받을 때는 &를 붙이지 않는다.
    printf("%s 입니다.\n", name);
    
    */

/*
    //강제 형 변환
    int a = 10;
    //double d = a; //이렇게 하면 에러가 남 type이 일치해야한다
    double d = (double)a; // type을 바꿀 수 있음
    
    double res = (double)5 / (double)2;  //5.0 / 2.0 으로 바꿔 줌
    printf("%.1lf\n", res);

    //자동 형 변환
    int aa = 10;
    double dd = aa;  //double형에 int를 넣으면 자동으로 double로 바꿔준다
    printf("%lf\n", dd);

    double result = 5 / 2; //자동으로 double형으로 바뀌지만, 정수로 나누면 나머지를 버린 결과가 변수에 넣어진다
    double result2 = (double)5 / 2; //하나를 실수로 바꾸면 5.0 / 2.0 의 결과가 나옴
    printf("%lf\n", result);
    printf("%lf\n", result2);
    printf("한글");
*/  
    int num1 = 10;
    printf("%p", &num1);

    

return 0;
}


