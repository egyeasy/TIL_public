#include <iostream>
#include <cstring>
#include "printer.h"

using namespace std;

void Printer::SetString(char* input) {
    // string = input;
    strcpy(string, input);
}

void Printer::ShowString() {
    cout << string << endl;
}