#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//struct ���� // ����ü
//����ü �⺻
struct student {   
    int num;
    double grade;
};

// ����ü Ȱ��
struct profile {
    char name[20];
    int age;
    double height;
    char *intro;
};

int main() {
    //����ü �⺻
    struct student s1; //s1�� ������ struct student������ ����, 
    //���� s1�̶�� �̸����� ����� �� ���� (�ణ Ŭ���� �Ǵ� ��� ���� ����)
    s1.num = 2;
    s1.grade = 2.7;
    printf("�й�: %d\n", s1.num); // (.)���� ����
    printf("����: %.1lf\n", s1.grade);
    printf("\n\n");

    // ����ü Ȱ��
    struct profile yun;
    strcpy(yun.name, "������"); //���ڿ��� �迭�� ���� ���� �� �����Ƿ� strcpy�� �̿�
    yun.age = 17;
    yun.height = 164.5;

    yun.intro = (char *)malloc(80); //**�����ͺ����� (profile ����ü�� ������ ������ intro) ���ڿ��� �־��� �� �����Ƿ� 
    //** �޸𸮿� ���� �Ҵ��� ���� ����� ��, �Ǵ� �ʱ�ȭ�ÿ� �����Ҵ�
    printf("�ڱ�Ұ�: ");
    gets(yun.intro);

    printf("�̸�: %s\n", yun.name);
    printf("����: %d\n", yun.age);
    printf("Ű: %.1lf\n", yun.height);
    printf("�ڱ�Ұ�: %s\n", yun.intro);
    free(yun.intro); //�������� �Ҵ��� �޸� ���� ��ȯ

    return 0;
}

