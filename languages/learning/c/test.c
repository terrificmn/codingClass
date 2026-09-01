/*
#include <stdio.h>
int main()
{
    int i, j, nbr, count;
    /*
    // �Ҽ� �����
    printf("�Է��ϼ��� :");
    scanf("%d", &nbr);
    for (i = 2; i < nbr; i++)
    {
        for (j = 2; j < i; j++)
        {
            if (i % j == 0)
            {
                break;
            }
        }
        if (i == j)
        {
            if (count == 5)
            {
                printf("\n");
                count = 0;
            }
            printf("%d ", i);

            count++;
        }
    }
    return 0;
*/

/*
    int hour, min, sec;
    double origin, time = 3.76;

    origin = time;
    hour = (int)time;
    time -= hour;
    time *= 60;
    min = (int)time;
    time -= min;
    time *= 60;
    sec = (int)time;

    printf("%.2lf��\t%d�ð� %d�� %d�� �Դϴ�.", origin, hour, min, sec);
    return 0;
*/

//더블포인터 사용
#include <stdio.h>
void user_print(char **dou_p_abc, int size) //더블 포인터로 받기- 포인터는 포인터로 받음
{
    int i;
    for (i = 0; i < size; i++)
    {
        //dou_p_abc[i] = "hithere"; //바꾸는 것 가능
        printf("%-10s", dou_p_abc[i]); //! *로 참조하면 안됨 에러남, 이중포인터를 배열명처럼 사용하는 것
        //printf("%s\t", *(dou_p_abc + i)); //같음
    }
}

int main()
{
    int size;
    char abc[4][10] = {"hello", "my", "friend", "good"};
    char *p_abc[] = {abc[0], abc[1], abc[2], abc[3]}; //포인터에 직접 문자열상수를 할당하지 않고

    // 이미 만들어진 문자열 배열 주소 주기
    // * 문자열 자체가 주소이므로 &을 붙이지 않는다

    //p_abc[0] = "hi"; //이런식으로  포인터 p_abc는 abc의 주소를 가지고 있어서 수정이 가능
    //?복사가 되는 것인지는 확인이 필요
    //printf("%s", p_abc[0]); //어쨋든 수정이 된 것 확인

    /* //직접 포인터 변수에 문자 넣어주기
    char *p_abc[] = {"hello", "my", "friend", "good"}; //직접 포인터 변수에 문자 넣어주기
    // 수정도 가능. 안되는 줄 알았는데 가능함. 공부가 더 필요    
    */
    printf("%d\n", sizeof(p_abc[0])); // 포인터 p_abc의 하나의 배열의 크기 나옴 64bit 컴 기준 8byte
    printf("%d\n", sizeof(p_abc));    // 포인터 p_abc의 전체배열의 크기 나옴 64bit 컴 기준 32byte

    //배열 사이즈 구하는
    size = sizeof(p_abc) / sizeof(p_abc[0]); //전체에서 배열 하나 크기를 나눠주면 배열의 개수가 나옴
    printf("%d\n", size);
    user_print(p_abc, size); //포인터로 넘겨줌, size도 넘김

    return 0;
}
