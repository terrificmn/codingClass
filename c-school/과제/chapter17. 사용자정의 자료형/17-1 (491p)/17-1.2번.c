#include <stdio.h>
struct cracker {
    int price, calories;
};

int main() {
    struct cracker basasak; //����ü ���� ����
    printf("�ٻ���� ���ݰ� ������ �Է��ϼ��� :");
    scanf("%d%d", &basasak.price, &basasak.calories); 
    printf("�ٻ���� ����: %d��\n", basasak.price);
    printf("�ٻ���� ����: %dkcal\n", basasak.calories);
    return 0;
}