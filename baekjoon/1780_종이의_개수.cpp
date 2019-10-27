#include <iostream>
#include <math.h>
#include <typeinfo>

using namespace std;

int N;
int mat[2200][2200];
int counts[3] = {0};

double intlog(double base, double x)
{
    return (log(x) / log(base));
}

void go_into(int s_row, int s_col, int log_size)
{
    int size = (int) pow(3, log_size);
    int start = mat[s_row][s_col];
    bool is_same = true;

    for (int i = s_row; i < s_row + size; i++)
    {
        for (int j = s_col; j < s_col + size; j++)
        {
            if (mat[i][j] != start)
            {
                is_same = false;
                break;
            }
        }
        if (!is_same)
        {
            break;
        }
    }
    if (is_same)
        counts[start + 1]++;
    else
    {
        int next_size = (int) pow(3, log_size - 1);
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
                go_into(s_row + i * next_size, s_col + j * next_size, log_size - 1);
        }
    }

}

int main()
{
    cin >> N;

    for (int i = 0; i < N; i ++)
    {
        for (int j = 0; j < N; j ++)
            cin >> mat[i][j];
    }

    int n = (int) floor(intlog(3, N) + 0.5);
    // cout << typeid(n).name() << endl;
    cout << "n: " << n << endl;

    go_into(0, 0, n);

    for (int i = 0; i < 3; i ++)
        cout << counts[i] << endl;

    return 0;
}