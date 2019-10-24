import sys
sys.stdin = open('2293.txt', 'r')

n, k = map(int, input().split())
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)

former_result = [0] * (k + 1)
result = [0] * (k + 1)

former_result[0] = 1
result[0] = 1

coin_idx = 0

while coin_idx < n:
    for target in range(1, k + 1):
        if nums[coin_idx] > target:
            result[target] = former_result[target]
        else:
            result[target] = result[target - nums[coin_idx]] + former_result[target]
    former_result = result
    coin_idx += 1
    
print(result[k])
        
    

    

