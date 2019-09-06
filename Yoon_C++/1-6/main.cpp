#include "functions.h"
using namespace std;

const int NAME_LEN = 20;

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
    char name[NAME_LEN];
    int deposit;
    cout << "[Create Account]" << endl;
    cout << "Account ID: " << *accountId << endl;
    cout << "Name: "; cin >> name;
    cout << "Deposit: "; cin >> deposit;
    
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