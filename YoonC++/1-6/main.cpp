#include <iostream>
#include <cstring>
using namespace std;

const int NAME_LEN = 20;

bool showMenu();
void createAccount(int* accountId);
void send();
void drawOut();
void totalInfo();
void exit();

struct Account
{
    int accountId;
    char name[NAME_LEN];
    int deposit;
};

Account accArr[100];
int accountId = 0;

int main(void) {
    bool isExit = false;

    while (!isExit)
    {
        isExit = showMenu();
    }

    return 0;
}

bool showMenu() {
    bool isExit = false;

    cout << "-----Menu------" << endl;
    cout << "1. making account" << endl;
    cout << "2. drawin" << endl;
    cout << "3. drawout" << endl;
    cout << "4. accounts info" << endl;
    cout << "5. exit" << endl;
    cout << "choose one: ";

    int number;
    cin >> number;\
    
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
        isExit = true;
    } else {
        cout << "plz type right" << endl;
    }

    return isExit;
}

void createAccount(int* accountId) {
    char name[NAME_LEN];
    int deposit;
    cout << "[Create Account]" << endl;
    cout << "Account ID: " << *accountId << endl;
    cout << "Name: "; cin >> name;
    cout << "Deposit: "; cin >> deposit;

    accArr[*accountId].accountId = *accountId;
    strcpy(accArr[*accountId].name, name);
    accArr[*accountId].deposit = deposit;
    
    *accountId += 1;
    
}

void send() {
    int sendId;
    int amount;
    cout << "[Send Money]" << endl;
    cout << "Account ID: "; cin >> sendId;
    cout << "Amount: "; cin >> amount;

    for (int i=0; i<100; i++)
    {
        if (accArr[i].accountId == sendId)
        {
            accArr[i].deposit += amount;
            break;
        }
    }

    cout << "Send Completed" << endl;
}

void drawOut() {
    int drawId;
    int amount;
    cout << "[Drawout Money]" << endl;
    cout << "Account ID: "; cin >> drawId;
    cout << "Amount: "; cin >> amount;

    for (int i=0; i<100; i++)
    {
        if (accArr[i].accountId == drawId)
        {
            if (amount > accArr[i].deposit)
            {
                cout << "Not enough money" << endl;
            } else
            {
                accArr[i].deposit -= amount;
                cout << "Drawout Completed" << endl;
            }
            break;
        }
    }
}

void totalInfo() {
    int infoId;

    cout << "[Total Information]" << endl;
    cout << "Account ID: "; cin >> infoId;

    for (int i=0; i<100; i++)
    {
        if (accArr[i].accountId == infoId)
        {
            cout << "Name: " << accArr[i].name << endl;
            cout << "Deposit: " << accArr[i].deposit << endl;
            break;
        }
    }
}

void exit() {
    cout << "exit" << endl;
}