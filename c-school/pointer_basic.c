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

    return 0;
}