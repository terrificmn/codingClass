#include <stdio.h>
/*
    struct student {   //struct �����ϱ�
        int num;
        double grade;
    };
    // struct���� ���ǵ� ���� �ٽ� ������ 
    typedef struct student Student;  //struct�� ���ǵ� student�� Student�� �ٽ� ������ : typedef-type define
*/

// ���� �ڵ带 �Ʒ� ó�� ������ ���� �ִ�
// �������ϱ� ���� �ڷ����� ���� ����� �ʿ䰡 ���� �� �� ����� ���ÿ� ������ �ϴ� ���
typedef struct {
    int num;
    double grade;
} Student;  // �Ϲ� ������� �����ϱ� ���� �빮�ڷ� �����ϴ°� ����

void print_data(Student *ps); 

int main() {
    Student s1 = { 315, 4.2 };  //typedef�� ���ǵ� Student�� s1������ ����
    print_data(&s1);
    return 0;
}
void print_data(Student *ps) {
    printf("�й�: %d\n", ps->num);
    printf("����: %.1lf\n", ps->grade);
}