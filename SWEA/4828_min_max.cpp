#include <iostream>

using namespace std;

int nums[1001];

int main() {
    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++)
    {
        int N;
        cin >> N;
        int min = 1000001;
        int max = 0;
        for (int i = 0; i < N; i++)
        {
            int input;
            cin >> input;
            if (input < min)
                min = input;
            if (input > max)
                max = input;
        }
        cout << "#" << tc << " " << max - min << endl;

    }

    return 0;
}