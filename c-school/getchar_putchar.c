#include <stdio.h>
/*
//?getchar()�� putchar()
int main() {

    int ch;

    printf("���� �Է�: ");
    ch = getchar(); // getchar()�� integer���·� �ƽ�Ű�ڵ�� ����
    putchar(ch);    //putchar(���ڿ�����) �� getchar�� ���� �Է°��� ����� �� ����
    printf("%d", ch); // integer�̱⶧���� ����ϸ� ���ڰ� �����µ� �ٷ� �ƽ�Ű�ڵ��̴�

    return 0;
}
*/

/*
//?���� �����ϱ�
int main() {
    int num, grade;

    printf("�й� �Է�: ");
    scanf("%d", &num); //scanf �� �Է��� ������ �Է� ���� �� (��: 123����) �ϸ� 123\n���� ���ۿ� ����ǰ� 123�� int�� �ٲ�� num�� �Ҵ��
    // ���ۿ��� ����'\n'���� �����ְ� �Ǵµ�, ���ۿ� �����ִ� ä�� 
    //getchar()�� �ް� �Ǹ� ���ۿ� �����ִ� \n ���� �Է��� �Ǿ���, �ᱹ ���ϴ� ��� ���� ���� ����
    //scanf()�� �������� ��, (�ٽ� scanf�� �ᵵ ���۰��� ����ִ� ���� �о��)
    //scanf("%d", &grade);

    getchar(); //getchar()�� ���ָ� ���ۿ� �ִ� ���� �о�� (���ۿ� �����ִ� '\n' ������ ���� ȿ��)
    
    printf("���� �Է�: ");
    grade = getchar(); //���� �ٽ� getchar()�� �����ϸ� ���ϴ� ����� ����
    printf("�й�: %d, ����: %c", num, grade);

    return 0;
}
*/


//? �Լ��� getchar()�� �ݺ��Ͽ� �迭������ �־��ֱ� (�Ķ���ͷ� �����ͷ� ����)
void my_gets(char *str, int size);

int main() {
    char str[7];

    my_gets(str, sizeof(str)); //���ڿ��迭 ũ�⵵ �Ѱ���  //����� �Լ�
    printf("�Է��� ���ڿ�: %s\n", str); 
    

    return 0;
}

// �ݺ������� ���ۿ��� ���ڸ� �޾Ƽ� 
void my_gets(char *str, int size) {
    int ch, i = 0;

    printf("�Է��ϼ���: ");
    ch = getchar(); //getchar�� ���۸� ����ϴ� ���� �Է� �Լ� (scanf�� ���ۻ��)
    
    while ((ch != '\n') && (i < size -1)) { 
        // \n�� ���͸� �ǹ��ϹǷ� ����ģ�� �ƴϸ� ��� �ݺ� , size�� -1�� �������� \0�� �־���ϱ� ����
        str[i] = ch;
        i++;
        ch = getchar();
    }
    str[i] = '\0'; //�������� �� ���� �־��ֱ�

}
