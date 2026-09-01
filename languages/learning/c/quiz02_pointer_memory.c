#include <stdio.h>
#include <stdlib.h>

//연습문제 https://dojang.io/mod/page/view.php?id=322
//포인터에 할당된 메모리를 3차원 배열처럼 사용하기
//다음 소스 코드를 완성하여 포인터에 할당된 메모리를
//높이 2, 세로 크기 3, 가로 크기 5인 3차원 배열처럼 사용할 수 있도록 만드세요.

int main()
{
    //높이(depth) 만큼 3중포인터 선언 후 높이(depth) 만큼 메모리에 할당
    long long ***m = malloc(sizeof(long long **) * 2); //m[0[0]

    for (int depth = 0; depth < 2; depth++)
    {
        //면의(depth) 개수만큼 반복하면서 세로 공간(row)에 할당하는 메모리 할당: m[0][0] 요런개 3개
        m[depth] = malloc(sizeof(long long *) * 3);
        /*
        m[0][0] m[0][1] m[0][2]
        m[1][0] m[1][1] m[1][2]
        */

        for (int row = 0; row < 3; row++)
        {
            //세로 크기만큼 (row)반복하면서 가로 공간에 해당하는 메모리를 할당 (5개씩): m[0][0][0] 요런개 5개
            /*
            m[0][0][0]  m[0][0][1]  m[0][0][2]  m[0][0][3]  m[0][0][4]  m[0][0][5]
            m[0][1][0]  m[0][1][1]  m[0][1][2]  m[0][1][3]  m[0][1][4]  m[0][1][5]
            m[0][2][0]  m[0][2][1]  m[0][2][2]  m[0][2][3]  m[0][2][4]  m[0][2][5]
            */

            m[depth][row] = malloc(sizeof(long long *) * 5);
        }
    }
    m[1][2][4] = 100;

    //메모리에서 제거
    for (int depth = 0; depth < 2; depth++)
    {
        for (int row = 0; row < 3; row++)
        {
            free(m[depth][row]);
        }
        free(m[depth]);
    }

    free(m);
    return 0;
}
