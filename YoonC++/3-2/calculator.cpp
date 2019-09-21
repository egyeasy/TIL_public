#include "calculator.h"

void Calculator::Init() {
    num_add = 0;
    num_sub = 0;
    num_mul = 0;
    num_div = 0;
}

float Calculator::Add(float a, float b) {
    num_add++;
    return a + b;
}
float Calculator::Min(float a, float b) {
    num_sub++;
    return a - b;
}
float Calculator::Mul(float a, float b) {
    num_mul++;
    return a * b;
}
float Calculator::Div(float a, float b) {
    num_div++;
    return a / b;
}
void Calculator::ShowOpCount() {
    cout << "add: " << num_add << " sub: " << num_sub << " mul: " << num_mul << " div: " << num_div;
}