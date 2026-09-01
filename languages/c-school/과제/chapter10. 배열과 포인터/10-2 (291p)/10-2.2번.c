#include <stdio.h>
void print_month(int *mp);

int main() {
    int month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    print_month(month);
}

void print_month(int *mp) {
        int i;
        int size;
        
        for (i=0; i < 12; i++) {
            //printf("%d ", mp[i]); //주소자체이므로 배열의 i번째를 가리킴, 아래와 같음
            printf("%d ", *(mp + i));
            if ((i+1) % 5 == 0) {
                printf("\n");
            }
        }
        
    }
