#include <stdio.h>
int main() {
/* �迭�� ������
    int arr[5];
    int a;
    int *ptr;
    ptr = &a;
    ptr = arr; //�迭��ü�� �迭�� ù��° ��Ҹ� ����Ű�� �ּҰ�: &�� �ʿ����
    // &arr[0] == arr == ptr
    // arr[0] == ptr[0]
    // ������ ������ ���ڸ� ���ؼ� ����
    //(ptr + 0) == (arr + 0)  :ù ���� ���
    //(ptr + 1) == (arr + 1) : �� ��° ���
    //. *(ptr + 0) == (arr +0) == arr[0] //���� ���� ������ (* asterisk)�� ����ص� ���� ���
    //. *(ptr + 0) == (arr +0) == arr[0]  
    // ���������ڵ� ��밡��
    //. *(ptr +0) �ϳ� ������ *(ptr +1) �� ptr++ ������ ó�� ���� : �ּҰ��� �ٲ�� �� �׷��Ƿ� ����
    // ��, arr�� �迭�ε� *(arr + 0)�� �����ϳ� 1= arr++ �� �Ұ����ϴ� (arr++��ü�� ������ ��ü�� ��ȭ��Ű�� ������ �ȵ�): �迭���� ���� �ٲ� �� ����
    // ��: int a = 10
    // ��: a + 1 �� a +1 �� �������� a ��ü�� �ٲ��� ����
    // ��: a++�� a�� +1 �ؼ� a��ü�� �ٲٴ� �� 

*/
    int ary[3];
    int i;

    *(ary + 0) = 10;  //. *(ary + 0)�� ������ ������̶�� �ϸ� ary�� �迭�̹Ƿ� �迭 �ּҰ��� �����Ƿ� +0 �̸� ary[0] ����
    *(ary + 1) = *(ary + 0) + 10;

    printf("�� ��° �迭 ��ҿ� Ű���� �Է�: ");
    scanf("%d", ary + 2);

    for(i=0; i< 3; i++){  // �Ǵ� for(i=0; i<ary[i]; i++)
        printf("%5d", *(ary + i));
    }
    
    return 0;

}