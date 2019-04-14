// long long 사용, 출력 옵션 필요
#include <iostream>

using namespace std;

int main(){
    ios::sync_with_stdio(0); // c++ stream과 c stream 사이의 sync 끄기(cout만 사용해야 함. no printf)
    cin.tie(0); // cin과 cout이 번갈아 나올 때마다 flush하지 않도록 하는 명령 -> 줄바꿈은 \n으로 써야함. no endl
    long long a, b;
    cin >> a >> b;
    if (a < b){
        cout << b - a - 1 << "\n";
        for (long long i = a + 1; i < b; i++){
            cout << i << " ";
        }
    }
    else if (a > b){
        cout << a - b - 1 << "\n";
        for (long long i = b + 1; i < a; i++){
            cout << i << " ";
        }
    }
    else{
        cout << "0";
    }
    if ((a + 1 != b) and (a != b + 1)){
        cout << "\n";
    }

    return 0;
}
