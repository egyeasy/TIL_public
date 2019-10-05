import sys
sys.stdin = open('1966.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, target_M = map(int, input().split())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    print()
    print(nums)
    print(N, target_M)

    t_priority = nums[target_M]

