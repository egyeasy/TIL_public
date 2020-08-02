# https://leetcode.com/problems/coin-change-2/discuss/99210/python-O(n)-space-dp-solution
# O(N) solution
# overwrite -> no need to calculate again
from typing import List
from math import gcd

class Solution:    
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
               if j >= i:
                   dp[j] += dp[j - i]
        return dp[amount]