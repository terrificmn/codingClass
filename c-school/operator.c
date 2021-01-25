#include <stdio.h>
int main() {
// 1번 문제  
/*
    double a = 4.0, b = 1.2;
    printf("%.1lf + %.1lf = %.1lf\n", a, b, a + b);  #소수 표시는 %lf으로 출력할 때 %.소수점 (예:%.2lf 는 소수점 2자리까지 표시)
    printf("%.1lf - %.1lf = %.1lf\n", a, b, a - b);
    printf("%.1lf * %.1lf = %.1lf\n", a, b, a * b);
    printf("%.1lf / %.1lf = %.1lf", a, b, a / b);
    return 0;
*/
// 2번 문제
/*
    int a, b, tot;
    double avg;

    printf("두 과목의 점수 : ");
    scanf("%d%d", &a, &b);  //* scanf로 입력을 받을 때는 " "로 묶고, 2개 이상이면 붙여서 써야한다. 예 "%d%lf"
    tot = a + b;
    avg = tot / 2.0;

    printf("평균 : %.1lf\n", avg);

    return 0;
*/

//3번 문제
    int kor, eng, mat;
    int credits;
    int res;
    double kscore = 3.8, escore = 4.4, mscore = 3.9;  //변수를 한번에 초기화해서 값을 할당해 줄 수 있다
    double grade;

    kor = 3;
    eng = 5;
    mat = 4;
    credits = kor + eng + mat;

    // kscore = 3.8;
    // escore = 4.4;
    // mscore = 3.9;
    grade = kscore + escore + mscore / 3.0; //실수형태로 구하기 위해 3.0으로 나눔
    
    //* c언어는true,false가 없다고 함, 숫자로만 리턴됨: 참이면 1, 거짓이면 0
    res = grade >= 4.0 && credits >= 10;
    printf("%d", res);

    return 0;

}