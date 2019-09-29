#include <iostream>

void swap(int* a, int* b) {
    int temp = *b;
    *b = *a;
    *a = temp;
}

void swap(char* a, char* b) {
    char temp = *b;
    *b = *a;
    *a = temp;
}

void swap(double* a, double* b) {
    double temp = *b;
    *b = *a;
    *a = temp;
}

int main(void) {
    int num1 = 20, num2 = 30;
    swap(&num1, &num2);
    std::cout<<num1<<' '<<num2<<std::endl;

    char ch1='A', ch2='Z';
    swap(&ch1, &ch2);
    std::cout<<ch1<<' '<<ch2<<std::endl;

    double dbl1=1.111, dbl2=5.555;
    swap(&dbl1, &dbl2);
    std::cout<<dbl1<<' '<<dbl2<<std::endl;
    return 0;
}