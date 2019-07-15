#include <iostream>
using namespace std;

int BoxVolume(int length) {
    return length;
}

int BoxVolume(int length, int width) {
    return length * width;
}

int BoxVolume(int length, int width, int height) {
    return length * width * height;
}

int SimpleFunc(int a=10) {
    return a + 1;
}

int SimpleFunc(void) {
    return 10;
}
int main(void) {
    int a = 0;
    cout << "[3, 3, 3] : " << BoxVolume(3, 3, 3) << endl;
    cout << SimpleFunc(5) << endl;
    // cout << SimpleFunc(); // 에러
    return 0;
}
