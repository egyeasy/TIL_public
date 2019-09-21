#include <iostream>

using namespace std;

void add_one(int &num);
void change_plus(int &num);

int main(void) {
    int number = 1;
    add_one(number);
    change_plus(number);
    add_one(number);
    change_plus(number);
    add_one(number);
    change_plus(number);
    return 0;
}

void add_one(int &num) {
    num += 1;
    cout << num << endl;
}

void change_plus(int &num) {
    num = -num;
    cout << num << endl;
}