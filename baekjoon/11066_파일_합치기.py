# 리스트 하나 만들어서 계속해서 바뀌게 만들어주기

import sys
sys.stdin = open('11066.txt', 'r')

def binary_divide(start, end):
    global total_cost
    if start == end:
        return nums[start]
    min_sum = 10000000000
    for k in range(start, end):
        left = binary_divide(start, k)
        right = binary_divide(k + 1, end)
        this_sum = left + right
        if this_sum < min_sum:
            min_sum = this_sum
    total_cost += min_sum
    return min_sum

TC = int(input())
for tc in range(TC):
    K = int(input())
    nums = list(map(int, input().split()))
    print(nums)
    
    total_cost = 0

    binary_divide(0, K - 1)

    print(total_cost)