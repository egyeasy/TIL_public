// int를 long long으로 취급해야하는 문제. K가 2^31 - 1까지 가능함.
#include <iostream>

using namespace std;

int K, N;
long long nums[10000] = {0};
long long max_num = 0;

void search(long long start, long long end, long long* answer)
{
    // cout << "start: " << start << " " << end << endl;
    if (start > end)
    {
        // cout << "answer: " << *answer << endl;
        return;
    }
        
    long long mid = (start + end) / 2;
    int count = N;
    
    for (int i = 0; i < K; i++)
        count -= nums[i] / mid;
    
    if (count <= 0)
    {
        if (mid > *answer)
            *answer = mid;
        search(mid + 1, end, answer);
    } else
        search(start, mid - 1, answer);
}


int main(void)
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> K >> N;
    for (int i = 0; i < K; i++)
    {
        long long num;
        cin >> num;
        nums[i] = num;
        if (num > max_num)
            max_num = num;
    }

    long long start = 1;
    long long end = max_num;
    long long result = -1;

    search(start, end, &result);

    cout << result << endl;


}