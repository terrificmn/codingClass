#include <stdio.h>
#include <string.h>
/*
int get_num(void);

int main() {
    int result;
    result = get_num();
    printf("��ȯ ��: %d\n", result);
    return 0;
}

int get_num(void) {
    int num;
    printf("��� �Է�: ");
    scanf("%d", &num);

    return num;
*/


/*
void print_char(char ch, int count);
int main(void) {
    print_char('@', 5);
    return 0;

}

void print_char(char ch, int count) {
    int i;

    for (i=0; i < count; i++) {
        printf("%c", ch);

    }
    return;
}
*/
void print_str(char **pps, int cnt);

int main() {
/*
    int ch;

    //getchar()�� putchar()
    printf("���� �Է�: ");
    ch = getchar(); // getchar()�� integer���·� �ƽ�Ű�ڵ�� ����
    putchar(ch);    //putchar(���ڿ�����) �� getchar�� ���� �Է°��� ����� �� ����
    printf("%d", ch); // integer�̱⶧���� ����ϸ� ���ڰ� �����µ� �ٷ� �ƽ�Ű�ڵ��̴�
*/

/*
    char str[80];
    char str1[80];
    // printf("�Է� ���� ����: ");
    // fgets(str, sizeof(str), stdin); // �������� \n �� �߰���
    // printf("%s\n", str);
*/
    
/*
    scanf("%s", str);
    printf("�� �Է�: ");
    scanf("%*c");  //���� ������ 
    gets(str1);
    
    printf("%s\n", str1);
*/

/*
//������ ���� Ȱ�� ����
    int num1 = 10, num2 = 20;
    int *ptr1, *ptr2; 
    ptr1 = &num1;
    ptr2 = &num2;

    printf("%d\t%d\n", *ptr1, *ptr2);
    *ptr1 += 10;
    *ptr2 -= 10;

    printf("%d\t%d\n", num1, num2);
    
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
*/

/*
    //�����͸� �̿��ؼ� ������ 
    int arr[6] = {1,2,3,4,5,6};
    printf("%d\n", arr[0]);
    int *fp = &arr[0];  //�����Ϳ� �ּҰ��� �־��ش�, 
    //** (�迭���� �ּҸ� �ǹ�������, �ε����� �ƴ� �迭���̿��� �Ѵ�) ������ ���⿡�� ���� �ƴ� �ּҰ��� �־��ش�, �ε��� ���
    // int *fp = arr; ������ ���� �ڵ�
    // int *fp = arr[0]; �̷��� �ϸ� ������ ��, �迭���� �ּҰ��� ã���� arr[0]��°�� �� �� �����Ƿ� ����
    int *lp = &arr[5];  
    int temp, i;
    
    for(i=0; i< 3; i++) {
        temp = *fp;
        *fp = *lp;
        *lp = temp;
        fp += 1;
        lp -= 1;
    }

    for(i=0; i< 6; i++) {
        printf("%d ", arr[i]); //���
    }
*/
    char *ptr_ary[] = {"eagle", "tiger", "lion", "squirrel"};
    int count;

    count = sizeoff(ptr_ary) / sizeof(ptr_ary[0]);
    print_str(ptr_ary, count);  //ptr_ary�� ������ �������� �ּҰ��� �ѱ� �� ����
    
    return 0;
}

void print_str(char **pps, int cnt) {
    int i;
    for (i=0; i < cnt; i++) {
        printf("%s\n", pps[i]);
    }
}

