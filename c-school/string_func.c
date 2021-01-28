#include <stdio.h>
#include <string.h>
//문자열 기본 활용 함수들 
// <string.h> 인크루드 해야함
int main() {
    char str[80];
    strcpy(str, "wine");
    strcat(str, "apple");
    strncpy(str, "pear", 1);
    printf("%s, %d\n", str, strlen(str));
    return 0;
}

