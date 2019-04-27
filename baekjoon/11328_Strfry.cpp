#include <iostream>
using namespace std;

int main() {
    int TC;
    cin >> TC;
    for (int tc = 0; tc < TC; tc++) {
        char a[1000], b[1000];
        int a_alpha[26], b_alpha[26];
        for (int i = 0; i < 26; i++) {
            a_alpha[i] = 0;
            b_alpha[i] = 0;
        }

        cin >> a >> b;
        for (int i = 0; i < 1000; i++) {
            if (!a[i] && !b[i]) {
                break;
            }
            
        }
    }

    return 0;
}