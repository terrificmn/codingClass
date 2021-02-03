#include <stdio.h>
int main() {
//file open �⺻
/*
    FILE *fp; //FILE ���̺귯���� �̿��ؼ� ������ ����
    fp = fopen("a.txt", "r");
    if (fp == NULL) {
        printf("������ ������ �ʾҽ��ϴ�.\n");
        return 1;  //�����ϰ� ����
    }
    printf("������ ���Ƚ��ϴ�.\n");
    fclose(fp);
*/

    FILE *fp1; //�ٽ� ����
    int ch;

    fp1 = fopen("C:\\Users\\5-20\\Desktop\\a.txt", "r");  // ���丮 ������ \\ ���������� 2���� ���
    if (fp1 == NULL) { 
        printf("������ ������ �ʾҽ��ϴ�.");
        return 1;
    }

    while (1) {
        ch = fgetc(fp1);  //fp1 �����ͷ� ����� ���Ͽ� �о�ͼ� ��ȯ�ؼ� ch������ �Ҵ� //** �� �̻� �������� ���� EOF ��ȯ
        // *����: -1�� ���� ����� ���� ������ �ý��ۿ� ���� EOF���ǰ� �ٸ� �� �־ ȣȯ���� ���� EOF ����� ����ϴ°� ����
        if (ch == EOF) {  //EOF End Of File�� ����� -1�� �̸� ���ǵǾ� �ִ�. ������ ���� �����ϸ� -1�� ��ȯ�Ѵٰ� ��
            break;  
        }
        putchar(ch);  //���� �� ���
    }
    fclose(fp1);  //������ ���� �Ŀ��� �� fclose�� �ؾ��Ѵ�. �޸𸮿��� ����

    return 0;
}