#include <iostream>
#include "NameCard.h"

using namespace std;

namespace COMP_POS
{
    void showClass(int pos)
    {
        if (pos == CLERK) {
            cout << "sawon" << endl;
        } else if (pos == SENIOR) {
            cout << "juim" << endl;
        } else if (pos == ASSIST) {
            cout << "daeri" << endl;
        } else if (pos == MANAGER) {
            cout << "gwajang" << endl;
        }
    }
}

NameCard::NameCard(char *inName, char *inCompany, char *inPhoneNum, int inMember)
    :member(inMember)
{
    name = new char[strlen(inName) + 1];
    company = new char[strlen(inCompany) + 1];
    phoneNum = new char[strlen(inPhoneNum) + 1];
    strcpy(name, inName);
    strcpy(company, inCompany);
    strcpy(phoneNum, inPhoneNum);
}

void NameCard::ShowNameCardInfo()
{
    cout << "name: " << name << endl;
    cout << "company: " << company << endl;
    cout << "phoneNum: " << phoneNum << endl;
    cout << "class: "; COMP_POS::showClass(member);
    cout << endl;
}

NameCard::~NameCard()
{
    delete []name;
    delete []company;
    delete []phoneNum;
}