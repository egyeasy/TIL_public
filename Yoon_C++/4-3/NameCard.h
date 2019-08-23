#ifndef __NAMECARD_H__
#define __NAMECARD_H__

#include <iostream>
#include <cstring>

using namespace std;

namespace COMP_POS
{
    enum
    {
        CLERK,
        SENIOR,
        ASSIST,
        MANAGER
    };

    void showClass(int pos);
}

class NameCard
{
    private:
        char * name;
        char * company;
        char * phoneNum;
        int member;

    public:
        NameCard(char *inName, char *inCompany, char *inPhoneNum, int inMember);

        void ShowNameCardInfo();

        ~NameCard();
};

#endif