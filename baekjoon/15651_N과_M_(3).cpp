// scanf, printf가 여기서는 더 빠르다. auto 문법도 참고해볼 것
#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;
int N, M;
void make_product(int depth, vector<int>& product)
{
    if (depth == M)
    {
        for (auto num : product)
        // for (int i = 0; i < M; i++)
            // cout << num << " ";
            printf("%d ", num);
        // cout << endl;
        printf("\n");
        return;
    }
    for (int i = 1; i <= N; i++)
    {
        product.push_back(i);
        make_product(depth + 1, product);
        product.pop_back();
    }
}
int main()
{
    // cin >> N >> M;
    scanf("%d %d", &N, &M);
    for (int i = 1; i <= N; i++)
    {
        vector<int> product;
        product.push_back(i);
        make_product(1, product);
    }
    return 0;
}