#include <stdio.h>
#include <string.h>
//���ڿ� �⺻ Ȱ�� �Լ��� 
//* <string.h> ��ũ��� �ؾ���
int main() {
    char str[80];
    strcpy(str, "wine"); //ī��: str�� wine�� �����ؼ� ����
    strcat(str, "apple"); //���� - ���� str �ڿ� apple�� ����
    strncpy(str, "pear", 1); //strncpy�� source ���ڿ�(2��° �Ķ����)���� n��ŭ�� ���ս�Ŵ
    
    printf("%s, %d\n", str, strlen(str)); //strlen() ���ڿ��� ���� ��ȯ


    char source[30] = "example";
    char destination[30]; //���� �ٲ� ���ڿ� 
    
    strncpy(destination, source + 0, 5); //? strncpy() �Լ��� ù ��° �Ķ���ʹ� destination, �� ��°�� source, �� ��°�� size(����)
    // 2��° �Ķ� source + 0 ��ü�� ù��° �ּҸ� ����Ŵ, �� ��° �Ķ���ʹ� 2��° �ҽ����� 5�ڸ����� �޾ƿ�

    printf("strncpy()�Լ��� ���: %s", destination); //examp���� ǥ���ϴ� ���� Ȯ��!

    destination[strlen(destination)] = '\0'; //*�ι��� �־��ֱ�, �����Ⱚ�� �о���� ����
    // �ʱ� ���ڿ��迭 ���� �����ϸ鼭 ���ڿ��� �־��ְų�(�迭�ʱ�ȭ) 
    // scanf������ �Է��� ���� ��찡 �ƴ� ���� ������ ���� �� �� �ִٰ� ��
    


}

