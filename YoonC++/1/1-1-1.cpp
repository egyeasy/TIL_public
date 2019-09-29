// 사용자로부터 5개의 정수를 입력 받아서, 그 합을 출력하는 프로그램
#include <iostream>
using namespace std;

int main() {
    int total = 0;
    int a;
    for (int i=0; i<5; i++) {
        cout << i + 1 << "번째 정수 입력: ";
        cin >> a;
        total += a;
    }
    cout << "합계: " << total << endl;
}