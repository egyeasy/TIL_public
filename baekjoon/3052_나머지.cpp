#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    vector<int> v, remains;
    v.reserve(10);
    int count;

    for (int i=0; i < 10; i++) {
        cin >> v[i];
        bool isIn = false;
        int this_remain = v[i] % 42;
        for (vector<int>::size_type j=0; j < remains.size(); j++) {
            if (remains[j] == this_remain) {
                count++;
                // cout << "겹침: " << this_remain << " " << v[i] << endl;
                break;
            }
        }
        if (!isIn) {
            remains.push_back(this_remain);
        }
    }
    cout << 10 - count << endl;
}