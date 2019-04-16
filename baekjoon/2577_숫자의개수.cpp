// long long 사용, 출력 옵션 필요
#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    long long a, b, c;
    cin >> a >> b >> c;

    long long abc = a * b * c;

    int num_cnt[10];

    for (int i = 0; i < 10; i++){
        num_cnt[i] = 0;
    }

    while (abc > 0){
        // cout << abc << "\n";
        num_cnt[abc % 10]++;
        abc /= 10;
    }

    for (int i = 0; i < 10; i++){
        cout << num_cnt[i] << "\n";
    }
    

    return 0;
}
