#include <stdio.h>
struct cracker {
    int price, calories;
};

int main() {
    struct cracker basasak; //구조체 변수 선언
    printf("바사삭의 가격과 열량을 입력하세요 :");
    scanf("%d%d", &basasak.price, &basasak.calories); 
    printf("바사삭의 가격: %d원\n", basasak.price);
    printf("바사삭의 열량: %dkcal\n", basasak.calories);
    return 0;
}