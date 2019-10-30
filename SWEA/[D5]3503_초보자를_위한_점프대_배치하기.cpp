#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int TC;
    int N;
    int nums[10001] = {0};

    cin >> TC;

    for (int tc = 1; tc <= TC; tc++)
    {
        cin >> N;

        for (int i = 0; i < N; i++)
            cin >> nums[i];
        
        sort(nums, nums + N);

        int idx = 2;
        int max_diff = -1;
        int curr_diff;

        while (idx < N)
        {
            curr_diff = nums[idx] - nums[idx - 2];
            if (curr_diff > max_diff)    
                max_diff = curr_diff;
            idx++;
        }

        curr_diff = nums[N - 1] - nums[N - 2];
        if (curr_diff > max_diff)
            max_diff = curr_diff;

        curr_diff = nums[1] - nums[0];
        if (curr_diff > max_diff)
            max_diff = curr_diff;

        cout << "#" << tc << " " << max_diff << endl;
    }

    return 0;
}
