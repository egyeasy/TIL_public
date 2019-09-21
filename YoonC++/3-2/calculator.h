#ifndef __CALCULATOR_H__
#define __CALCULATOR_H__

#include <iostream>
using namespace std;

class Calculator
{
    private:
        int num_add;
        int num_sub;
        int num_mul;
        int num_div;
    public:
        void Init();
        float Add(float a, float b);
        float Min(float a, float b);
        float Mul(float a, float b);
        float Div(float a, float b);
        void ShowOpCount();
};

#endif