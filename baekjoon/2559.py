import sys
sys.stdin = open('2559.txt', 'r')

N, K = map(int, input().split())
nums = list(map(int, input().split()))

one_sum = sum(nums[0:K])
former_idx = 0
max_sum = one_sum
# print(one_sum)
for i in range(1, N - K + 1):
    one_sum = one_sum - nums[former_idx] + nums[i + K - 1]
    # print(i, one_sum)
    if one_sum > max_sum:
        max_sum = one_sum
    former_idx += 1

print(max_sum)