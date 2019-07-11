#include <iostream>
using namespace std;

int main(void) {
    bool is_alright = true;
    while (is_alright) {
        try {
            int a, b;
            cin >> a >> b;
            cout << a + b << endl;
        } catch(int expn) {
            is_alright = false;
            return 0;
        }
    }
}