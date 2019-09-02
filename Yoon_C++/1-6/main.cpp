#include "functions.h"
using namespace std;

void createAccount(int* accountId);
void send();
void drawOut();
void totalInfo();
void exit();

int main(void) {
    cout << "-----Menu------" << endl;
    cout << "1. making account" << endl;
    cout << "2. drawin" << endl;
    cout << "3. drawout" << endl;
    cout << "4. accounts info" << endl;
    cout << "5. exit" << endl;
    cout << "choose one: ";

    int number;
    cin >> number;

    int accountId = 1;
    
    if (number == 1) {
        createAccount(&accountId);
    } else if (number == 2) {
        send();
    } else if (number == 3) {
        drawOut();
    } else if (number == 4) {
        totalInfo();
    } else if (number == 5) {
        exit();
    } else {
        cout << "plz type right" << endl;
    }

    return 0;
}

void createAccount(int* accountId) {
    cout << "[계좌개설]" << endl;
    *accountId += 1;
    
    
}

void send() {

}

void drawOut() {

}

void totalInfo() {

}

void exit() {
    
}