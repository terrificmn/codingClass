#include <stdio.h>
int main() {
    int ch, cntLower = 0, cntUpper ;
    ch = getchar();

    while (ch != '\n') {
        if (ch >= 97 && ch <= 122) cntLower++;  //�ҹ����� �ƽ�Ű �ڵ� a=97, z=122
        if (ch >= 65 && ch <= 90) cntUpper++;  //�ҹ����� �ƽ�Ű �ڵ� a=65, z=90
        ch = getchar();
    }
    printf("�ҹ����� ����: %d\n", cntLower);
    printf("�빮���� ����: %d", cntUpper);
    return 0;
}