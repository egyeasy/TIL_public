#include "1-6-1.cpp"

int main(void) {
    cout << "-----Menu------" << endl;
    cout << "1. 계좌개설" << endl;
    cout << "2. 입 금" << endl;
    cout << "3. 출 금" << endl;
    cout << "4. 계좌정보 전체 출력" << endl;
    cout << "5. 프로그램 종료" << endl;
    cout << "선택: ";

    int number;
    cin >> number;

    int accountId = 1;
    
    if (number == 1) {
        createAccount();
    } else if (number == 2) {
        send();
    } else if (number == 3) {
        drawOut();
    } else if (number == 4) {
        totalInfo();
    } else if (number == 5) {
        exit();
    } else {
        cout << "똑바로 입력하세요." << endl;
    }
}