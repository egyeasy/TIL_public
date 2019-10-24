// 배열 초기화 하지 않으면 쓰레기값이 들어간다.
#include <iostream>

using namespace std;

int main()
{
    int n, k;
    int coins[101];

    cin >> n >> k;

    for (int i = 0; i < n; i++)
    {
        cin >> coins[i];
    }

    int result[10001] = {0};
    result[0] = 1;

    int coin_idx = 0;

    while (coin_idx < n)
    {
        for (int target = 1; target <= k; target++)
        {
            if (coins[coin_idx] <= target)
                result[target] += result[target - coins[coin_idx]];
        }
        coin_idx++;
    }

    cout << result[k] << endl;

    return 0;
}