#include <stdio.h>
int main() {
    FILE *fp;
    char str[] = "What do you want?";
    int i;

    fp = fopen("C:\\Users\\5-20\\Desktop\\b.txt", "w");  // 'w'은 쓰기 전용, 파일이 있으면 overwrite 

    if (fp == NULL) { 
        printf("파일을 만들지 못했습니다.");
        return 1;
    }

    i = 0;
    while (str[i] != '\0') {  // \0이 아니면 무한반복
        fputc(str[i], fp);  //fputc()함수로 str배열에 맞게 할당 후, 포인터에 넘겨줌
        i++;
    }
    fputc('\n', fp);  
    fclose(fp);
    // b가
    return 0;
}