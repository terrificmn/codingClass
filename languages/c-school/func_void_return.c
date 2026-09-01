#include <stdio.h>

// void 함수 관련 
void print_char(char ch, int count);

int main() {
    print_char('@', 11); //사용자 함수
    return 0;
}

void print_char(char ch, int count) {
    int i;

    if(count > 10) return;  //** void함수에서 함수를 강제 종료 시킬 때는 return 으로 함수를 종료시킬 수 있음 
    for (i=0; i < count; i++) {
        printf("%c", ch);
    }
    return;
}

