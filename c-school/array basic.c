#include <stdio.h>
int main()
{

/*
// array초기화 방법들..
int array[5];
array[0] = 10;  //단순히 인덱스별로 주는 방법
array[1] = 20;
array[2] = 30;
array[3] = 40;
array[4] = 50;
// 초기화를 안하면 알 수없는 값 (쓰레기값)이 들어가 있음에 유의
// 또는 한번에 초기화
int arr1[5] = {1, 2, 3, 4, 5};
int arr2[100] = { 0 }; //
int arr3[] = {1, 2, 3};  //배열크기를 정하지 않고 {}의 값으로 정해줄 수도 있음, 3개의 배열이 생김
*/

    int score[5];
    int i;
    int total = 0;
    double avg;

    /* 5번 for문으로 입력받아서 출력하는 코드 - 배열을 이용
    for (i = 0; i < 5; i++)
    {
        printf("입력하세요: ");
        scanf("%d", &score[i]);
        total += score[i];
    }
    avg = total / 5.0;

    for (i = 0; i < 5; i++)
    {
        printf("%5d", score[i]); // %5d의 정렬의 효과가 있다. 변수의 숫자를 5만큼 오른쪽으로 채우고 나머지는 공백으로 채워진다
                                 // 반대는 -5%d로 하면 왼쪽으로 먼저 글자가 배치되고 나머지가 공백으로 채워짐
    }
    printf("\n평균: %.1lf\n", avg);
*/

    for (i = 0; i < 10; i++)
    {
        printf("%d / 3 = %lf\t", i, (double)i / 3);
        //printf("%d / 3 = %lf\t", i, i / 3); // 결과가 0.000000 소수점이하를 제대로 표시못함
        printf("%d %% 3 = %d\n", i, i % 3);
    }
    // 몫과 나머지 부분을 헷갈리지 말자
    // 몫은 double로 type변환해서 소수점 이하로 나온것
    // 나머지는 정수만 표현하는 듯

    return 0;
}