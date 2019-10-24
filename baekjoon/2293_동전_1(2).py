# reference : https://debuglog.tistory.com/78
# 메모리 초과

import sys
sys.stdin = open('2293.txt', 'r')

n, k = map(int, input().split())
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)

result = [[0] * (k + 1) for _ in range(n + 1)]

for coin_idx in range(n):
    result[coin_idx][0] = 1

for coin_idx in range(n):
    for target in range(1, k + 1):
        if nums[coin_idx] > target:
            result[coin_idx][target] = result[coin_idx - 1][target]
        else:
            result[coin_idx][target] = result[coin_idx][target - nums[coin_idx]] + result[coin_idx - 1][target]
    
print(result[n - 1][k])
        
    

    

