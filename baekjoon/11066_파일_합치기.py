# 리스트 하나 만들어서 계속해서 바뀌게 만들어주기

import sys
sys.stdin = open('11066.txt', 'r')

TC = int(input())
for tc in range(TC):
    K = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(nums)
    
    total_cost = 0

    while len(nums) > 1:
        print(nums)
        added_cost = nums[0] + nums[1]
        total_cost += added_cost
        nums[0] = added_cost
        nums.pop(1)
        nums.sort()
        print("added: ", added_cost)
        print("total: ", total_cost)
    
    print(total_cost)
        