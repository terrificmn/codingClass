#include <stdio.h>
int main() {
    char *pDessert = "apple"; //���ڿ� ��ü�� �ּҰ�
    char str[10] ="mango";
    char *pa;

    int age; 
    char name[20];

    //str = "mg"; //�̷����� ������    // str = "�����Է½ÿ���";
    //** ���ڿ� �迭���� ���ʿ� �ΰ� = �ؼ� "���ڿ�"�� ���� �Ҵ��ϴ� ���� �ϴ� ������� �����ϱ�
    //str[0] = 'a';  //?�迭�� �ϳ��� �ܾ� �ϳ��� �Է� ���� ('�̱� �����̼����� ����� ��)
    str[3] = 'G';
    printf("%s\n", str);


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