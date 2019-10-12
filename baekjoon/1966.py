import sys
sys.stdin = open('1966.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, target_M = map(int, input().split())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    # print()
    # print(nums)
    # print(N, target_M)

    t_priority = nums[target_M]

    new_nums = []

    for idx,num in enumerate(nums):
        new_nums.append((idx, num))

    # print(new_nums)

    reversed_nums = nums[::-1]
    is_larger = False
    larger_idx = -1

    for idx, num in enumerate(reversed_nums):
        if num > t_priority:
            is_larger = True
            larger_idx = N - idx - 1
            break


    if is_larger:
        new_nums.sort(reverse=True, key=lambda x: (x[1], 1 if x[0] > larger_idx else 0, -x[0]))
    else:
        new_nums.sort(reverse=True, key=lambda x: (x[1], -x[0]))

    # print(new_nums)
    
    for idx, num in enumerate(new_nums):
        if num[0] == target_M:
            print(idx + 1)
            break
