#include <stdio.h>
int main() {
    int a = 10, b = 15, total;
    double avg;
    int *pa, *pb; //*������ ������ �����Ͱ� ����Ű�� �������� Ÿ���� ��ġ�ؾ��Ѵ�. 
    int *pt = &total;
    double *pg = &avg;

    int num1 = 10;
    printf("%p", &num1); // %p�� �ּҸ� ������

    pa = &a; //pointer���� pa�� ����Ű�� a������ Ÿ���� ��ġ�ؾ���
    pb = &b;

    *pt = *pa + *pb;
    *pg = *pt / 2.0;

    printf("�� ������ ��: %d, %d\n", *pa, *pb);
    printf("�� ������ ��: %d\n", *pt);
    printf("�� ������ ���: %.1lf\n", *pg);

    printf("\n\n");

    char ch = 'A';
    int in = 10;
    double db = 3.4;

    char *pch = &ch;
    int *pin = &in;
    double *pdb = &db;

    printf("ch,in,db ������ �ּҰ�\n");
    printf("ch �ּ� %p\t", &ch);  //%p �ּҸ� ������
    printf("in �ּ� %p\t", &in);
    printf("db �ּ� %p\n", &db);
    printf("ch,in,db�� �� �ּҸ� ���� pch,pin,pdb �������� �ּҰ�\n");
    printf("pch ������ %p\t", pch);
    printf("pin ������ %p\t", pin);
    printf("pdb ������ %p\t", pdb);

    printf("\n�������� ��\n");
    printf("pch ������ %c\t", *pch);
    printf("pin ������ %d\t", *pin);
    printf("pdb ������ %lf\t", *pdb);


//// swap�� ��: �ּҰ� �ѱ��� �� ���� ����� ������!!!!
    int a1 = 10, b1 = 50;
    int *ptr1 = &a1, *ptr2 = &b1;
    int *temp; //temp�� �����ͺ����� �����ϸ� ptr1�� �ּҰ��� �ٷ� �Ҵ��� �ִ°� ���� //?(��, �������� �ּҰ��� ��ȯ! ���� �� �ٲ�)
    temp = ptr1; 
    ptr1 = ptr2;
    ptr2 = temp;
    printf("%d\t%d\n", *ptr1, *ptr2);

    int tmp; //���� tmp�� �Ϲݺ����� �����ϸ�, ����Ʈ������ �ƴϾ �ּҸ� ���� �� ����, ���� ����
    // ��� �����Ͱ��� �����ؼ� //? ������ ���� ���� �ٲ���� �� ���� (�ּҴ� �� �ٲ�, ��� ���� �ٲ�)
    tmp = *ptr1; //tmp�� �Ϲ� ������ ���
    *ptr1 = *ptr2;
    *ptr2 = tmp;
    printf("%d\t%d\n", *ptr1, *ptr2);

    return 0;
}