#include <stdio.h>
int main() {
    char *pDessert = "apple"; //���ڿ� ��ü�� �ּҰ�
    char str[10] ="mango";
    char *pa;

    int age; 
    char name[20];

    //todo: ���ڿ� ���� �ʿ�
    //str = "�����Է½ÿ���";
    //str[0] = "a";  // ���ڿ��� ���� ���� �ִ� ���� �Ұ�����, ���� //*ó���� ���������� �� �ʱ�ȭ ���־����
    //todo: pa = str �غ� ��
    pa = str;
    pa = "oldmango"; //������ ������ str�� ���� �ٲٴ� ���� ����. ��, ��Ȯ���� �ٲ�� ���� �ƴϰ� �ּҰ� ����Ǵ� ��
    printf("%s\n", pa);
    pa = "newmango";
    printf("%s\n", pa + 5);
    
    printf("%c\n", str[0]);

    printf("���� �Ľ��� %s �Դϴ�\n", pDessert);
    pDessert = "banana";
    printf("���� �Ľ��� %s �Դϴ�\n", pDessert);


    printf("--------------------\n");
    printf("���� �Է�: ");
    scanf("%d", &age);
    getchar(); //���ۿ� ���� '\n' ���๮�� ����
    //* ���� ������δ� scanf("%*c") �Ǵ� fgetc(stdin) �� ���ۿ��� �ϳ��� ���ڸ� �о ����

    printf("�̸� �Է�: ");
    gets(name);
    printf("����: %d, �̸�: %s\n", age, name);
    
    
    return 0;

}