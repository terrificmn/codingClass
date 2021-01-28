#include <stdio.h>
int main() {
    int ch, cntLower = 0, cntUpper ;
    ch = getchar();

    while (ch != '\n') {
        if (ch >= 97 && ch <= 122) cntLower++;  //소문자의 아스키 코드 a=97, z=122
        if (ch >= 65 && ch <= 90) cntUpper++;  //소문자의 아스키 코드 a=65, z=90
        ch = getchar();
    }
    printf("소문자의 개수: %d\n", cntLower);
    printf("대문자의 개수: %d", cntUpper);
    return 0;
}