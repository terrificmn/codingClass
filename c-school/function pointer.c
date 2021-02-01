#include <stdio.h>

void func(int (*fp)(int, int)); //�Լ������� ����
// ����Ÿ�� �����͸� (������type (�����ͺ���) (�Ķ���� type, ...) )
//void user_func(int (*fp)(int, int))
int sum(int a, int b);
int mul(int a, int b);
int max(int a, int b);

int main () {
    int sel;

    printf("����1: �� ������ ��\n");
    printf("����2: �� ������ ��\n");
    printf("����3: �� ���� �߿��� ū �� ���\n");
    printf("1~3 �� ���ϴ� ������ �����ϼ���: ");
    scanf("%d", &sel);

    switch(sel) {
        case 1: func(sum); break;
        case 2: func(mul); break;
        case 3: func(max); break; 
    }    
    return 0;
}

void func(int (*fp)(int, int)) { // �Լ������ͷ� *fp �� �Լ������ �ް� �Ǵµ�, (�����ʹ� �ּҸ� �����Ƿ� �Լ��� �ּҸ� ����)
    //�̴� �Լ����� �˸� �Լ��ּҸ� �ƴ� ���̾ �Լ��� ã�� �� �� ���� , ��: *fp �����Ϳ� sum�̶�� �Լ��� �ּҸ� ����
    int a, b, res;
    printf("�� ������ ���� �Է��ϼ���: ");
    scanf("%d%d", &a, &b);
    res = fp(a, b);  //** �Լ������ͷ� ���� ���� (�Է��� ���� ���� �Լ������� �޾��� ��: sum �̸� sum �Լ��� �ּҰ��� �޾ƿ�)
    //** ��������� sel ���� ���� �´� �Լ��� ȣ���� �� ��� ���� ���� ����
    printf("���: %d\n", res);
}

int sum(int a, int b) {
    return (a + b);
}
int mul(int a, int b) {
    return (a * b);
}
int max(int a, int b) {
    if(a > b) return a;
    else return b;
}
