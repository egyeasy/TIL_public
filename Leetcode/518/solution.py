from typing import List
from math import gcd

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        s = [[0] * (amount + 1) for _ in range(N + 1)]
        
        if not coins:
            gcd_ = 1
        else:
            gcd_ = coins[0]
            for coin in coins:
                gcd_ = gcd(gcd_, coin)
        
        for i in range(N + 1):
            s[i][0] = 1

        for i in range(1, N + 1):
            value = coins[i - 1]
            for k in range(gcd_, amount + 1, gcd_):
                s[i][k] = sum([s[i - 1][j] for j in range(k, -1, -value)])

        return s[N][amount]

if __name__ == "__main__":
    sol = Solution()
    print(sol.change(5, [1, 2, 5]))
    print(sol.change(3, [2]))
    print(sol.change(10, [10]))