// ���� ������
#include <stdio.h>
void swap_ptr(char **ppa, char **ppb);

int main() {
    int a = 10;
    int *singleP = &a; //�����Ϳ� a�ּҸ� �Ҵ�
    int **doubleP = &singleP; //���������Ϳ� singleP�� �ּҸ� �Ҵ� == a�� �ּ�
    
    printf("����\t|\t������\t|\t&����\t|\t*����\t|\t**����\n");    
    printf("-----------------------------------------------------------------------\n");   
    printf("    a   |%13d  |%13u  |\n", a, &a);    
    printf("singleP |%13d  |%13u  |%10d    |\n", singleP, &singleP, *singleP);    
    printf("doubleP |%13d  |%13u  |%10d    |%10d    |\n", doubleP, &doubleP, *doubleP, **doubleP);    

    printf("\n");
    
    
    char *pa = "success"; //������ ����pa ���ڿ� ��� �ʱ�ȭ
    char *pb = "failure"; //������ ����pb ���ڿ� ��� �ʱ�ȭ

    printf("�ٲٱ� ��: pa ---> %s, pb ---> %s\n", pa, pb); 

    swap_ptr(&pa, &pb); //swap_ptr()�Լ��� ȣ���ϸ鼭 args�� �ּҰ��� �Ѱ��ش� (&pa, &pb) 
    
    printf("�ٲ�  ��:  pa ---> %s, pb ---> %s\n", pa, pb); //�ٲ� ��

    return 0;
}

void swap_ptr(char **ppa, char **ppb) {  //* �Ķ���ʹ� douple pointer�� �����ؼ� �޴´�
    char *pTemp; //�ٲ��� �ӽ� ���� (������ ����)

    // �ٲٱ� (�ּҰ��� �����ؼ� �ٲ��ش�)
    pTemp = *ppa; //pTemp�� �̿��ؼ� �ٲ�
    *ppa = *ppb;  //���������� ppa�� �̱������ʹ� pa�� �ּҸ� �ǹ��ϴµ�, ���⿡ pb�� �ּҸ� �־ �ٲ�
    *ppb = pTemp; //���������� ppb�� �̱������ʹ� pb�� �ּҸ� �ǹ��ϴµ�, �ٲ� pTemp�� ���� �־����鼭 pa�� �ּҷ� �ٲ�
}