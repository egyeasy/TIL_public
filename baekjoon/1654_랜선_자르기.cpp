#include <iostream>

using namespace std;

int K, N;
int nums[10000] = {0};
int max_num = 0;

int search(int start, int end, int* answer)
{
    if (start > end)
        return *answer;
    int mid = (start + end) / 2;
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
        int num;
        cin >> num;
        nums[i] = num;
        if (num > max_num)
            max_num = num;
    }

    int start = 1;
    int end = max_num;
    int answer = -1;

    answer = search(start, end, &answer);

    cout << answer << endl;


}