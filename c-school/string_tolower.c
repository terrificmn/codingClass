#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[100];
    int i, count =0;

    printf("문장 입력: ");
    gets(str);
    
    for (i=0; i< str[i]; i++) {
        if (isupper(str[i])) {
            count += 1;
            str[i] = tolower(str[i]);
        }
    }

    puts(str);
    printf("바뀐 문자 수: %d", count);
    
    return 0;
}