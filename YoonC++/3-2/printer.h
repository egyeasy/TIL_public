#ifndef __PRINTER_H__
#define __PRINTER_H__

namespace PNT_CONST
{
    enum
    {
        STR_LEN=50
    };
}

class Printer
{
    public:
        char string[PNT_CONST::STR_LEN];

        void SetString(char* input);

        void ShowString();
};

#endif