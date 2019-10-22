#include <algorithm>
#include <iostream>
#include <deque>
#include <stdio.h>
#include <string.h>
#include <math.h>

using namespace std;

int main(void)
{
    int TC;
    cin >> TC;
    
    while (TC--)
    {
        bool cont = false;
        char query[100001];
        deque<int> D;
        scanf("%s", query);
        int n;
        scanf("%d", &n);
        char t;
        scanf("%c", &t); // enter
        scanf("%c", &t); // [

        for (int i = 0; i < n; i++)
        {
            int tmp;
            scanf("%d", &tmp);
            D.push_back(tmp);
            if (i != n - 1)
                scanf("%c", &t); // ,
        }
        scanf("%c", &t); // ]
        if (TC != 1)
            scanf("%c", &t); // enter
        bool isreverse = false;
        int len = strlen(query);
        for (int i = 0; i < len; i++)
        {
            if (query[i] == 'R')
                isreverse ^= 1;
            if (query[i] == 'D')
            {
                if (D.empty())
                {
                    cont = true; // 모순 발생
                    break;
                }
                if (!isreverse) // 뒤집지 않은 경우
                    D.pop_front();
                else // 뒤집은 경우
                    D.pop_back();
            }
        }
        
        if (cont)
        {
            printf("error\n");
            continue;
        }
        if (!isreverse)
        {
            printf("[");
            for (int i = 0; i < D.size(); i++)
            {
                if (i != (int)D.size() - 1)
                    printf("%d,", D[i]);
                else
                    printf("%d", D[i]);
            }
            printf("]\n");
        }
        if (isreverse)
        {
            printf("[");
            for (int i = (int)D.size() - 1; i >= 0; i--)
            {
                if (i != 0)
                    printf("%d,", D[i]);
                else
                    printf("%d", D[i]);
            }
            printf("]\n");
        }
    }
    return 0;
}









